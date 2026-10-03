# E-Commerce Customer Funnel & Conversion Analysis

## Project Overview

This project analyzes e-commerce customer behavior and builds a **View →
Cart → Purchase** conversion funnel using Python, DuckDB, Parquet, and
Power BI.

The analysis identifies funnel drop-offs, measures conversion rates,
compares performance across available dimensions, and provides
actionable business recommendations.

## Objectives

-   Clean and structure raw e-commerce event data
-   Analyze View → Cart conversion
-   Analyze Cart → Purchase conversion
-   Identify funnel drop-off points
-   Compare performance across time, product categories, and brands
-   Build a professional Power BI dashboard
-   Provide actionable business recommendations

## Funnel Definition

**View → Cart → Purchase**

  Stage      Meaning
  ---------- ----------------------------
  View       Product interest / traffic
  Cart       Purchase intent
  Purchase   Customer conversion

## Dataset

The original dataset contains approximately **67.5 million event
records**.

Main fields include:

`event_time`, `event_type`, `product_id`, `category_id`,
`category_code`, `brand`, `price`, `user_id`, `user_session`

Event types include `view`, `cart`, `remove_from_cart`, and `purchase`.

The raw dataset and large intermediate files are excluded from the
repository because of their size.

## Data Processing

Python and DuckDB were used to process the large dataset efficiently.

Processing included:

1.  Data validation
2.  Missing-value handling
3.  Data type conversion
4.  Event validation
5.  Duplicate handling
6.  Date/month extraction
7.  Funnel construction
8.  Parquet export
9.  Power BI visualization

The final funnel table is structured at the **user-session-product**
level.

## Key Dashboard Results

  Metric                         Result
  ---------------------------- --------
  Total Views                       42M
  Total Cart Additions               2M
  Total Purchases                  705K
  View → Cart Conversion          4.85%
  Cart → Purchase Conversion     34.65%
  View → Purchase Conversion      1.68%
  View → Cart Drop-off           95.15%
  Cart → Purchase Drop-off       65.35%

## Key Insights

### 1. View-to-Cart Drop-off

The View → Cart conversion rate is **4.85%**, with a **95.15%
drop-off**. This is the largest funnel loss and an important area for
further investigation.

### 2. Cart-to-Purchase Drop-off

The Cart → Purchase conversion rate is **34.65%**, with a **65.35%
drop-off**, indicating substantial abandonment after cart addition.

### 3. Overall Conversion

The overall View → Purchase conversion rate is **1.68%**.

### 4. Category and Brand Performance

Conversion performance varies across product categories and brands,
allowing lower- and higher-performing areas to be investigated.

### 5. Time-Based Performance

Monthly funnel performance is included to monitor changes in views, cart
additions, purchases, and conversion rates.

## Business Recommendations

### Improve Product-Page Engagement

-   Improve product information and images
-   Make pricing information clear
-   Strengthen calls-to-action
-   Investigate products with high views but low cart additions

### Reduce Cart Abandonment

Investigate potential friction related to:

-   Checkout complexity
-   Unexpected costs
-   Shipping information
-   Payment options
-   Purchase-flow usability

### Investigate Category Differences

Examine lower-converting categories for differences in pricing, product
presentation, availability, and customer experience.

### Monitor Funnel Trends

Track conversion rates over time and investigate significant changes in
views, cart additions, purchases, and funnel conversion.

## Data Limitations

The dataset does **not contain explicit marketing channel or campaign
fields**. Therefore, channel- and campaign-level comparisons were not
performed.

The analysis instead uses the available dimensions:

-   Time
-   Product category
-   Brand

Future versions could incorporate source, medium, channel, campaign, or
UTM attribution data.

## Tools & Technologies

-   Python
-   DuckDB
-   Jupyter Notebook
-   Parquet
-   Power BI
-   GitHub
-   Git LFS

## Project Structure

``` text
Task_3/
├── README.md
├── create_funnel_table.py
├── ecommerce_funnel_analysis.ipynb
├── Task_3.pbix
└── Screenshots/
    ├── dashboard_page_1.png
    └── business_insights_page_2.png
```

Large raw datasets, cleaned Parquet files, temporary DuckDB files, and
other intermediate files are excluded because of their size.

## Power BI Dashboard

### Page 1 --- E-Commerce Customer Funnel & Conversion Analysis

Includes KPI cards, funnel analysis, monthly performance, category
analysis, brand analysis, conversion rates, and drop-off metrics.

### Page 2 --- Business Insights & Recommendations

Includes key findings, actionable recommendations, data limitations, and
analysis scope.

## Conclusion

The analysis identifies the largest customer drop-off between **product
view and cart addition**, while also showing substantial abandonment
between cart addition and purchase.

The Power BI dashboard provides a structured view of the customer funnel
and highlights areas for further product, checkout, category, and
brand-level investigation.

## Author
Chidananda M
