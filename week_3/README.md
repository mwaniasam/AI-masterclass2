# Phase II - Track B: Data Analyst - Week 3: Advanced Data Analysis

A collection of commercial data engineering, aggregation, time series, and statistical analysis projects developed during Week 3 of the AI Masterclass (Track B: Data Analyst).

---

## Repository Contents

```
week_3/
|-- daily_collection.csv                  # Day 11: Granular daily milk collection records
|-- farmer_details.csv                    # Day 11: Farmer master profiles, zones, and rates
|-- dairy_zone_analysis.py                # Day 11: Multi-file merge, aggregation, and reporting script
|-- zone_monthly_summary.csv              # Day 11: Exported monthly executive summary table
|-- day1_advanced_pandas.md               # Day 11: Detailed notes on merges, joins, and pivots
|-- nairobi_supermarket_transactions.csv  # Day 12: 18 months of daily customer checkout counts
|-- supermarket_traffic_analysis.py       # Day 12: Time series pipeline and visualization script
|-- supermarket_traffic_trend.png         # Day 12: Dual-axis trend chart for operations manager
|-- day2_time_series.md                   # Day 12: Detailed notes on rolling averages and resampling
|-- mombasa_mfi_loans.csv                 # Day 13: 150 loan facilities across Mombasa, Kilifi, Kwale
|-- loan_statistical_analysis.py          # Day 13: Descriptive stats, IQR outliers, and correlation script
|-- loan_amount_distribution.png          # Day 13: Publication-grade loan distribution histogram
|-- day3_statistical_analysis.md          # Day 13: Statistical foundations, formulas, and board brief
\-- README.md                             # Module documentation and executive summaries
```

---

## Project 1: Nakuru Dairy Co-op Zone Analytics (Day 11)

### Business Context
Merges daily milk collection records with farmer master files to compute gross volumes, financial payouts, and top producers across three Nakuru County agricultural zones (Bahati, Njoro, and Rongai).

### How to Run
```bash
python3 dairy_zone_analysis.py
```

### Sample Output
```text
==============================================================================
      NAKURU DAIRY CO-OPERATIVE SOCIETY  |  MONTHLY ZONE SUMMARY
==============================================================================
Reporting Period : 2026-10-01 to 2026-10-14
Active Farmers   : 12 producers across 3 zones
Total Milk Pool  : 5,776.7 litres
Total Payout     : KES 321,595.20
------------------------------------------------------------------------------
Zone         |    Total Litres |   Total Payout (KES) | Top Farmer (Volume)   
------------------------------------------------------------------------------
Bahati       |         1,959.6 | KES       113,656.80 | David Mwangi (719.5 L)
Njoro        |         1,815.0 | KES        99,825.00 | Mary Wanjiku (663.9 L)
Rongai       |         2,002.1 | KES       108,113.40 | Samuel Korir (803.2 L)
------------------------------------------------------------------------------
TOTAL / CO-OP |         5,776.7 | KES       321,595.20 | --                    
==============================================================================
```

---

## Project 2: Nairobi Supermarket Chain Time Series (Day 12)

### Business Context
An 18-month time series analysis evaluating 546 consecutive days of customer transaction data (January 2025 to June 2026) for a Nairobi supermarket chain. The operations manager needed to distinguish genuine structural customer growth from recurring calendar seasonality.

### Executive Trend Report to the Client
> Foot traffic demonstrates genuine underlying growth of approximately 32.3% over the 18-month period (expanding from ~2,990 to ~3,960 baseline daily transactions on a 30-day rolling average), proving that customer volume is genuinely expanding rather than merely fluctuating. While baseline foot traffic is trending steadily upward, the business experiences predictable calendar seasonality characterized by a recurring post-holiday dip in February and an explosive ~100% volume surge during the December holiday shopping peak.

### Technical Pipeline
- **Datetime Indexing**: Parses date columns into indexed timestamps for rolling statistics.
- **30-Day Rolling Average**: Eliminates daily variance and weekend surges to reveal true trajectory.
- **Monthly Resampling**: Computes monthly aggregate transactions and month-over-month growth.
- **Dual-Axis Chart**: Generates `supermarket_traffic_trend.png` plotting monthly total bars alongside the 30-day rolling daily average curve.

### How to Run
```bash
python3 supermarket_traffic_analysis.py
```

---

## Project 3: Mombasa Microfinance Loan Portfolio Statistical Analysis (Day 13)

### Business Context
A statistical investigation of 150 loan facilities disbursed by a microfinance institution across Mombasa, Kilifi, and Kwale counties. Prepared for an executive board meeting to evaluate loan size dispersion, detect commercial-scale outlier credit risks, and test the relationship between loan amounts and repayment velocity.

### Board Plain-Language Finding on Correlation
> "Borrowers taking larger loans take moderately longer to make their first repayment (correlation = 0.57, p < 0.001), indicating that larger working capital disbursements require a longer initial operational ramp-up period before cash returns begin."

### Key Quantitative Findings
- **Typical Loan Size (Median)**: KES 32,750.00 (representative of core micro-borrowers).
- **Arithmetic Average (Mean)**: KES 40,176.67 (skewed rightward by +KES 7,426.67 due to commercial credit lines).
- **Standard Deviation**: KES 36,149.96.
- **Interquartile Range (IQR)**: Q1 = KES 24,625.00, Q3 = KES 42,750.00, Spread = KES 18,125.00.
- **Outlier Threshold**: Above KES 69,937.50 ($Q_3 + 1.5 \times \text{IQR}$).
- **Outliers Detected**: 8 accounts (5.3% of portfolio count, comprising 21.0% of total loan value).
- **Correlation**: Pearson $r = 0.570$ ($p = 2.59 \times 10^{-14}$), statistically significant.

### How to Run
```bash
python3 loan_statistical_analysis.py
```

### Sample Output
```text
==============================================================================
   MOMBASA MICROFINANCE INSTITUTION  |  BOARD STATISTICAL BRIEF
==============================================================================
Total Portfolio Loans Analyzed : 150 active facilities
Typical Loan Size (Median)     : KES 32,750.00
Arithmetic Average (Mean)      : KES 40,176.67
Standard Deviation             : KES 36,149.96
Interquartile Range (IQR)      : KES 24,625.00 to KES 42,750.00 (Spread: KES 18,125.00)
------------------------------------------------------------------------------
1. OUTLIER ANALYSIS (IQR METHOD)
------------------------------------------------------------------------------
Threshold for Unusually Large Loans : Above KES 69,937.50
Number of Outlier Loans Detected    : 8 loans (5.3%)

Identified Outlier Accounts:
Loan ID    | Borrower County |  Loan Amount (KES) |  Days to 1st Repayment
--------------------------------------------------------------------------
LN-1089    | Mombasa         |         290,000.00 |                     54 days
LN-1043    | Mombasa         |         240,000.00 |                     53 days
LN-1135    | Mombasa         |         220,000.00 |                     60 days
LN-1016    | Kwale           |         185,000.00 |                     47 days
LN-1114    | Kwale           |          99,500.00 |                     24 days
LN-1126    | Mombasa         |          88,000.00 |                     34 days
LN-1107    | Mombasa         |          77,000.00 |                     38 days
LN-1032    | Mombasa         |          75,500.00 |                     22 days
------------------------------------------------------------------------------
2. CORRELATION FINDING (LOAN SIZE VS. DAYS TO FIRST REPAYMENT)
------------------------------------------------------------------------------
Pearson Correlation (r) : 0.570
Statistical Significance: p = 2.5870e-14 (p < 0.001, highly significant)

Board One-Sentence Plain Summary:
 "Borrowers taking larger loans take moderately longer to make their first repayment
  (correlation = 0.57, p < 0.001), indicating that larger working capital disbursements
  require a longer initial operational ramp-up period before cash returns begin."
==============================================================================
```

---

## Technical Stack & Requirements

- Python 3.8+
- `pandas` (>= 2.0.0)
- `numpy` (>= 1.24.0)
- `scipy` (>= 1.11.0)
- `matplotlib` (>= 3.8.0)

Install dependencies:
```bash
pip install pandas numpy scipy matplotlib
```
