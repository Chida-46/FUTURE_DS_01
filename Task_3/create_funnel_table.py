import duckdb
from pathlib import Path
import shutil

# ============================================================
# PATHS
# ============================================================

CLEANED_DIR = Path(
    r"C:\Users\Kavya m\OneDrive\Desktop\tsts3\ecommerce_analysis_20260930_215352\cleaned_parquet"
)

OUTPUT_DIR = Path(
    r"C:\Users\Kavya m\OneDrive\Desktop\tsts3\powerbi_funnel"
)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "funnel_table.parquet"

TEMP_DIR = OUTPUT_DIR / "temp"
TEMP_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# CLEAN OLD OUTPUT
# ============================================================

if OUTPUT_FILE.exists():
    OUTPUT_FILE.unlink()

# Remove old temporary files
for item in TEMP_DIR.iterdir():
    if item.is_file() or item.is_symlink():
        item.unlink()
    elif item.is_dir():
        shutil.rmtree(item)


# ============================================================
# GET PARQUET FILES
# ============================================================

parquet_files = sorted(CLEANED_DIR.rglob("*.parquet"))

print(f"Found {len(parquet_files)} Parquet files.")
print()


# ============================================================
# DUCKDB
# ============================================================

con = duckdb.connect()

con.execute("SET memory_limit='2GB'")
con.execute("SET threads=1")
con.execute("SET preserve_insertion_order=false")
con.execute(
    f"SET temp_directory='{TEMP_DIR.as_posix()}'"
)


# ============================================================
# CREATE EMPTY RESULT TABLE
# ============================================================

con.execute("""
CREATE TABLE funnel_result (
    user_id VARCHAR,
    user_session VARCHAR,
    product_id BIGINT,
    first_view TIMESTAMP,
    first_cart TIMESTAMP,
    first_purchase TIMESTAMP,
    category_code VARCHAR,
    brand VARCHAR,
    viewed INTEGER,
    added_to_cart INTEGER,
    purchased INTEGER
)
""")


# ============================================================
# PROCESS EACH PARQUET FILE
# ============================================================

for i, parquet_file in enumerate(parquet_files, start=1):

    print(
        f"[{i}/{len(parquet_files)}] Processing: "
        f"{parquet_file.name}"
    )

    file_path = parquet_file.as_posix()

    query = f"""
    INSERT INTO funnel_result

    WITH events AS (

        SELECT
            event_time,
            event_type,
            product_id,
            category_code,
            brand,
            user_id,
            user_session

        FROM read_parquet(
            '{file_path}',
            union_by_name=true
        )

        WHERE event_type IN ('view', 'cart', 'purchase')

          AND user_id IS NOT NULL
          AND user_session IS NOT NULL
          AND product_id IS NOT NULL
    ),

    views AS (

        SELECT
            user_id,
            user_session,
            product_id,

            MIN(event_time) AS first_view,

            arg_min(category_code, event_time)
                AS category_code,

            arg_min(brand, event_time)
                AS brand

        FROM events

        WHERE event_type = 'view'

        GROUP BY
            user_id,
            user_session,
            product_id
    ),

    carts AS (

        SELECT
            v.user_id,
            v.user_session,
            v.product_id,

            MIN(e.event_time) AS first_cart

        FROM views v

        JOIN events e

            ON e.user_id = v.user_id
            AND e.user_session = v.user_session
            AND e.product_id = v.product_id

        WHERE e.event_type = 'cart'
          AND e.event_time >= v.first_view

        GROUP BY
            v.user_id,
            v.user_session,
            v.product_id
    ),

    purchases AS (

        SELECT
            c.user_id,
            c.user_session,
            c.product_id,

            MIN(e.event_time) AS first_purchase

        FROM carts c

        JOIN events e

            ON e.user_id = c.user_id
            AND e.user_session = c.user_session
            AND e.product_id = c.product_id

        WHERE e.event_type = 'purchase'
          AND e.event_time >= c.first_cart

        GROUP BY
            c.user_id,
            c.user_session,
            c.product_id
    )

    SELECT

        v.user_id,
        v.user_session,
        v.product_id,

        v.first_view,

        c.first_cart,

        p.first_purchase,

        v.category_code,
        v.brand,

        1 AS viewed,

        CASE
            WHEN c.first_cart IS NOT NULL
            THEN 1
            ELSE 0
        END AS added_to_cart,

        CASE
            WHEN p.first_purchase IS NOT NULL
            THEN 1
            ELSE 0
        END AS purchased

    FROM views v

    LEFT JOIN carts c

        ON c.user_id = v.user_id
        AND c.user_session = v.user_session
        AND c.product_id = v.product_id

    LEFT JOIN purchases p

        ON p.user_id = v.user_id
        AND p.user_session = v.user_session
        AND p.product_id = v.product_id
    """

    con.execute(query)


# ============================================================
# REMOVE DUPLICATES ACROSS PARTITIONS
# ============================================================

print()
print("Removing duplicate funnel rows...")

con.execute("""
CREATE TABLE final_funnel AS

SELECT
    user_id,
    user_session,
    product_id,
    MIN(first_view) AS first_view,
    MIN(first_cart) AS first_cart,
    MIN(first_purchase) AS first_purchase,
    arg_min(category_code, first_view) AS category_code,
    arg_min(brand, first_view) AS brand,
    1 AS viewed,
    MAX(added_to_cart) AS added_to_cart,
    MAX(purchased) AS purchased

FROM funnel_result

GROUP BY
    user_id,
    user_session,
    product_id
""")


# ============================================================
# WRITE FINAL PARQUET
# ============================================================

print("Writing final funnel table...")

con.execute(f"""
COPY final_funnel
TO '{OUTPUT_FILE.as_posix()}'
(FORMAT PARQUET, COMPRESSION ZSTD)
""")


# ============================================================
# SHOW RESULT
# ============================================================

row_count = con.execute(
    "SELECT COUNT(*) FROM final_funnel"
).fetchone()[0]

print()
print("==========================================")
print("FUNNEL TABLE CREATED SUCCESSFULLY")
print("==========================================")
print()
print(f"Rows: {row_count:,}")
print(f"Output: {OUTPUT_FILE}")
print()


con.close()