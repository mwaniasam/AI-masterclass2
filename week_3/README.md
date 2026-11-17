# Phase II - Track B: Data Analyst - Week 3: Advanced Data Analysis

A collection of commercial data engineering, aggregation, time series, statistical modeling, and multi-dataset integration projects developed during Week 3 of the AI Masterclass (Track B: Data Analyst).

---

## Repository Contents

```
week_3/
|-- daily_collection.csv                       # Day 11: Granular daily milk collection records
|-- farmer_details.csv                         # Day 11: Farmer master profiles, zones, and rates
|-- dairy_zone_analysis.py                     # Day 11: Multi-file merge, aggregation, and reporting script
|-- zone_monthly_summary.csv                   # Day 11: Exported monthly executive summary table
|-- day1_advanced_pandas.md                    # Day 11: Detailed notes on merges, joins, and pivots
|-- nairobi_supermarket_transactions.csv       # Day 12: 18 months of daily customer checkout counts
|-- supermarket_traffic_analysis.py            # Day 12: Time series pipeline and visualization script
|-- supermarket_traffic_trend.png              # Day 12: Dual-axis trend chart for operations manager
|-- day2_time_series.md                        # Day 12: Detailed notes on rolling averages and resampling
|-- mombasa_mfi_loans.csv                      # Day 13: 150 loan facilities across Mombasa, Kilifi, Kwale
|-- loan_statistical_analysis.py               # Day 13: Descriptive stats, IQR outliers, and correlation script
|-- loan_amount_distribution.png               # Day 13: Publication-grade loan distribution histogram
|-- day3_statistical_analysis.md               # Day 13: Statistical foundations, formulas, and board brief
|-- kisumu_school_attendance.csv               # Day 14: Daily attendance percentages with naming inconsistencies
|-- kisumu_school_infrastructure.csv           # Day 14: Classroom capacity and water access survey data
|-- school_infrastructure_attendance_analysis.py # Day 14: Multi-dataset deduplication, merge, and OLS regression
|-- school_attendance_vs_classrooms.png        # Day 14: Publication-grade scatter plot with trendline
|-- day4_multi_dataset_analysis.md             # Day 14: Entity resolution, deduplication, and officer report
\-- README.md                                  # Module documentation and executive summaries
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

---

## Project 4: Kisumu County School Infrastructure & Student Attendance Analysis (Day 14)

### Business Context
A multi-dataset investigation merging student attendance registers with infrastructure surveys across 17 public secondary schools in Kisumu County. Prepared for the County Education Officer to resolve institutional naming discrepancies, clean duplicate administrative submissions, evaluate the relationship between classroom capacity and student attendance, and examine the confounding impact of clean water access.

### Education Officer One-Sentence Finding
> "School classroom capacity exhibits a moderate positive correlation with student attendance rates (r = 0.74, p = 0.001), though reliable clean water access serves as a critical co-factor, with water-enabled schools averaging 11.6 percentage points higher daily attendance than water-deprived facilities."

### Structured Findings
1. **Classroom Capacity Correlation**: Student attendance rates positively correlate with classroom counts ($r = 0.740, p = 0.0010$). OLS regression indicates an expected attendance gain of ~0.71 percentage points per additional classroom ($y = 0.71x + 68.7, R^2 = 0.55$).
2. **Water Access Gap**: Clean on-site water access accounts for an 11.6 percentage point attendance premium (87.2% vs. 75.6%, $t = 5.04, p = 0.0002$).
3. **Capacity Without WASH Fails**: Kasagam Secondary has 21 classrooms but only 77.2% attendance due to lack of water, whereas Chemelil Sugar Academy achieves 89.5% attendance with only 14 classrooms with reliable water and feeding programs.

### How to Run
```bash
python3 school_infrastructure_attendance_analysis.py
```

### Sample Output
```text
================================================================================
   KISUMU COUNTY DEPARTMENT OF EDUCATION | MULTI-DATASET ANALYSIS BRIEF
================================================================================
Data Sources Merged         : Attendance Logs (File A) & Infrastructure Survey (File B)
Duplicates Removed          : 1 duplicate row(s) identified and deduplicated
Total Unique Institutions   : 17 educational institutions
Valid Analysis Population   : 16 schools with complete infrastructure & attendance data
Incomplete Records          : 1 school with missing attendance (Miwani Secondary),
                              1 school with unrecorded water access (Kudho Secondary)
--------------------------------------------------------------------------------
CANONICAL MERGED SCHOOL INVENTORY TABLE:
--------------------------------------------------------------------------------
School Name                      | Classrooms | Water Access | Attendance %
--------------------------------------------------------------------------------
Ahero Girls Secondary School     |         18 |          Yes |        83.4%
Chemelil Sugar Academy           |         14 |          Yes |        89.5%
Dr. Aloo Gumbi Secondary School  |         11 |           No |        72.8%
Joel Omino Secondary School      |         22 |          Yes |        84.0%
Kasagam Secondary School         |         21 |           No |        77.2%
Kisumu Boys High School          |         32 |          Yes |        90.8%
Kisumu Day High School           |         27 |          Yes |        86.8%
Koru Girls High School           |         16 |          Yes |        85.0%
Kudho Secondary School           |         10 |   Unrecorded |        71.0%
Lions High School                |         24 |          Yes |        91.5%
Maseno School                    |         35 |          Yes |        94.5%
Miwani Secondary School          |         13 |           No |      Missing
Nyabondo High School             |         25 |          Yes |        88.5%
Ojolla Secondary School          |         12 |           No |        74.0%
Otieno Oyoo Secondary School     |         26 |          Yes |        79.5%
Rae Girls Secondary School       |         15 |           No |        78.5%
Sinyolo Girls Secondary School   |         20 |          Yes |        86.2%
--------------------------------------------------------------------------------
STATISTICAL FINDINGS & INFERENCE:
--------------------------------------------------------------------------------
Classroom Capacity Range     : 10 to 35 classrooms (Mean: 20.5)
Attendance Rate Range        : 71.0% to 94.5% (Mean: 83.3%)
Pearson Correlation (r)      : 0.740
Statistical Significance (p) : p = 0.0010 (p < 0.01, highly significant)
Water Access Attendance Gap  : Water-enabled (87.2%) vs Water-deprived (75.6%)
                              Difference: +11.6 percentage points (t = 5.04, p = 0.0002)
--------------------------------------------------------------------------------
OFFICER REPORT ONE-SENTENCE FINDING:
--------------------------------------------------------------------------------
 "School classroom capacity exhibits a moderate positive correlation with student attendance
  rates (r = 0.74, p = 0.001), though reliable clean water access serves as a critical co-factor,
  with water-enabled schools averaging 11.6 percentage points higher daily attendance than water-deprived facilities."
================================================================================
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
