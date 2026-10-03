# FUTURE_DS_01

This repository contains projects completed as part of the **FUTURE INTERNS** program. Each task folder contains the files required for the project, including datasets, dashboards, analysis files, reports, and screenshots.

---

# TASK 1: SALES PERFORMANCE DASHBOARD

## Project Overview

This project analyzes business sales data using Microsoft Power BI to identify revenue trends, top-selling products, and high-performing categories or regions.

## Objectives

- Analyze revenue trends over time.
- Identify top-selling products.
- Find high-value categories and regions.
- Build an interactive sales dashboard.
- Provide business insights and recommendations.

## Tools Used

- Microsoft Power BI
- Microsoft Excel
- DAX

## Deliverables

- Sales performance dashboard
- Data analysis and business insights
- Project report and screenshots

---

# TASK 2: TELCO CUSTOMER CHURN ANALYSIS

## Project Overview

This project analyzes customer churn patterns using the **IBM Telco Customer Churn dataset**. The dashboard identifies high-risk customer segments and provides recommendations to improve customer retention.

## Objectives

- Analyze customer churn and retention rates.
- Identify high-risk customer segments.
- Study churn patterns across contract types, tenure, payment methods, and services.
- Build an interactive Power BI dashboard.
- Develop customer retention strategies.

## Tools Used

- Microsoft Power BI
- Microsoft Excel
- DAX

## Key Findings

- Overall churn rate: **26.54%**
- Month-to-month contract churn: **42.71%**
- First-year customer churn: **47.44%**
- Electronic check churn: **45.29%**

## Recommendations

- Improve first-year customer onboarding.
- Encourage longer-term contracts.
- Improve fiber service quality.
- Strengthen technical support.
- Review payment and security service options.

## Deliverables

- Customer churn analysis dashboard
- Business insights and recommendations
- Project report and screenshots

---

# TASK 3: E-COMMERCE CUSTOMER FUNNEL ANALYSIS

## Project Overview

This project analyzes e-commerce user behavior and builds a customer conversion funnel using a large-scale e-commerce event dataset.

The analysis focuses on the funnel:

**View → Cart → Purchase**

The project identifies conversion rates, funnel drop-offs, time-based performance, product category performance, and brand-level performance.

## Objectives

- Clean and structure large-scale e-commerce event data.
- Analyze traffic/product-view to cart conversion.
- Analyze cart to purchase conversion.
- Identify major funnel drop-off points.
- Compare funnel performance across available dimensions.
- Build an interactive Power BI funnel dashboard.
- Provide actionable business recommendations.

## Dataset

The original dataset contains approximately **67.5 million event records**.

Important fields include:

- `event_time`
- `event_type`
- `product_id`
- `category_id`
- `category_code`
- `brand`
- `price`
- `user_id`
- `user_session`

The main event types are:

- `view`
- `cart`
- `remove_from_cart`
- `purchase`

## Data Processing

Python and DuckDB were used to process the large dataset efficiently.

The workflow included:

- Data validation
- Missing-value handling
- Data type conversion
- Event validation
- Duplicate handling
- Date and month extraction
- Funnel construction
- Parquet data generation
- Power BI analysis

The final funnel table was structured at the **user-session-product** level.

## Tools Used

- Python
- DuckDB
- Jupyter Notebook
- Parquet
- Microsoft Power BI
- DAX
- GitHub

## Key Results

| Metric | Result |
|---|---:|
| Total Views | 42M |
| Total Cart Additions | 2M |
| Total Purchases | 705K |
| View → Cart Conversion | 4.85% |
| Cart → Purchase Conversion | 34.65% |
| View → Purchase Conversion | 1.68% |
| View → Cart Drop-off | 95.15% |
| Cart → Purchase Drop-off | 65.35% |

## Key Findings

### View → Cart

The View → Cart conversion rate is **4.85%**, with a **95.15% drop-off**.

This represents the largest drop-off in the analyzed funnel.

### Cart → Purchase

The Cart → Purchase conversion rate is **34.65%**, with a **65.35% drop-off**.

This indicates substantial loss between cart addition and completed purchase.

### Overall Conversion

The overall View → Purchase conversion rate is **1.68%**.

### Category and Brand Performance

Conversion performance varies across product categories and brands, allowing areas of stronger and weaker performance to be investigated.

### Time-Based Performance

Monthly funnel performance is included to monitor changes in views, cart additions, purchases, and conversion rates.

## Recommendations

### 1. Improve Product-Page Engagement

- Improve product information and images.
- Make pricing information clearly visible.
- Strengthen calls-to-action.
- Investigate products with high views but low cart additions.

### 2. Reduce Cart Abandonment

Investigate potential friction related to:

- Checkout complexity
- Shipping information
- Unexpected costs
- Payment options
- Purchase-flow usability

### 3. Investigate Category Performance

Analyze lower-converting categories to identify differences in:

- Pricing
- Product presentation
- Product availability
- Customer experience

### 4. Monitor Funnel Trends

Track changes in:

- Views
- Cart additions
- Purchases
- Conversion rates
- Funnel drop-offs

## Data Limitation

The dataset does **not contain explicit marketing channel or campaign fields**.

Therefore, channel- and campaign-level comparisons were not performed.

The analysis instead uses the available dimensions:

- Time
- Product category
- Brand

Future analysis could incorporate source, medium, channel, campaign, or UTM attribution data.

## Dashboard Pages

### Page 1 — E-Commerce Customer Funnel & Conversion Analysis

Includes:

- KPI cards
- Funnel stage analysis
- Monthly funnel performance
- View → Cart conversion
- Cart → Purchase conversion
- Category analysis
- Brand analysis
- Funnel drop-off metrics

### Page 2 — Business Insights & Recommendations

Includes:

- Key funnel findings
- Actionable recommendations
- Data limitations
- Analysis scope

## Deliverables

- E-commerce funnel analysis
- Python/DuckDB data-processing scripts
- Jupyter Notebook
- Power BI dashboard
- Business insights and recommendations
- Project screenshots

---

# REPOSITORY STRUCTURE

```text
FUTURE_DS_01/
│
├── Task_1/
│   ├── README.md
│   ├── dataset/
│   ├── dashboard/
│   └── screenshots/
│
├── Task_2/
│   ├── README.md
│   ├── dataset/
│   ├── dashboard/
│   └── screenshots/
│
├── Task_3/
│   ├── README.md
│   ├── create_funnel_table.py
│   ├── ecommerce_funnel_analysis.ipynb
│   ├── dashboard/
│   │   └── Task_3.pbix
│   └── screenshots/
│
└── README.md
```

AUTHOR

Chidananda M
