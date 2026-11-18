# Week 3: Advanced Data Analysis

Five data analysis projects from Week 3 (Track B: Data Analyst), covering multi-table joins, time-series trends, descriptive statistics, data cleaning, and market volatility analysis.

---

## Folder Contents

```text
week_3/
|-- daily_collection.csv                        # Day 11: Daily milk collection logs
|-- farmer_details.csv                          # Day 11: Farmer profiles, zones, and rates
|-- dairy_zone_analysis.py                      # Day 11: Merge, aggregation, and zone report
|-- zone_monthly_summary.csv                    # Day 11: Exported monthly summary table
|-- day1_advanced_pandas.md                     # Day 11: Notes on merges, joins, and pivots
|-- nairobi_supermarket_transactions.csv        # Day 12: 18 months of daily checkout counts
|-- supermarket_traffic_analysis.py             # Day 12: Rolling average and resampling script
|-- supermarket_traffic_trend.png               # Day 12: Monthly totals and 30-day rolling chart
|-- day2_time_series.md                         # Day 12: Notes on time-series analysis
|-- mombasa_mfi_loans.csv                       # Day 13: 150 loan records across 3 coastal counties
|-- loan_statistical_analysis.py                # Day 13: Descriptive stats, IQR outliers, correlation
|-- loan_amount_distribution.png                # Day 13: Loan size distribution histogram
|-- day3_statistical_analysis.md                # Day 13: Notes on statistics and hypothesis testing
|-- kisumu_school_attendance.csv                # Day 14: School attendance records (with dirty data)
|-- kisumu_school_infrastructure.csv            # Day 14: Classroom counts and water access survey
|-- school_infrastructure_attendance_analysis.py # Day 14: Cleaning, merging, and correlation script
|-- school_attendance_vs_classrooms.png         # Day 14: Classrooms vs attendance scatter plot
|-- day4_multi_dataset_analysis.md              # Day 14: Notes on combining messy datasets
|-- nairobi_produce_market/                     # Day 15: 6-month Nairobi produce price analysis
|   |-- data/                                   # Daily prices and crop metadata CSVs
|   |-- charts/                                 # Trends, volatility, and seasonality charts
|   |-- produce_market_analysis.py              # Full cleaning, volatility, and plotting script
|   \-- README.md                               # Client report with charts and findings
|-- day5_complex_analysis_project.md            # Day 15: Notes on volatility and methodology
\-- README.md                                   # Week 3 overview
```

---

## Day 11: Nakuru Dairy Co-op Zone Analysis

Joins daily milk delivery logs with farmer master records to compute total litres, payouts, and top producers across Bahati, Njoro, and Rongai (5,776.7 litres and KES 321,595.20 across 12 farmers).

```bash
python3 dairy_zone_analysis.py
```

---

## Day 12: Nairobi Supermarket Foot Traffic (Time Series)

Evaluates 18 months (546 days) of daily customer checkouts using monthly resampling and a 30-day rolling average to separate long-term growth from seasonal swings.

**Finding for Operations Manager**:
> Foot traffic grew by roughly 32.3% over 18 months (moving from ~2,990 to ~3,960 daily checkouts on a 30-day rolling average), showing genuine expansion rather than random noise. Around that upward trend, traffic follows predictable seasonality with a recurring dip in February and a surge of over 100% during December holiday shopping.

```bash
python3 supermarket_traffic_analysis.py
```

---

## Day 13: Mombasa Microfinance Loan Portfolio (Statistics)

Analyzes 150 loan records across Mombasa, Kilifi, and Kwale using descriptive statistics, Tukey's $1.5 \times \text{IQR}$ outlier rule, and Pearson correlation.

- **Median vs Mean**: KES 32,750.00 median vs KES 40,176.67 mean (pulled up by 8 commercial-sized loans above KES 69,937.50).
- **Correlation**: $r = 0.570$ ($p < 0.001$) between loan amount and days to first repayment.

**Finding for Board Meeting**:
> Borrowers taking larger loans take moderately longer to make their first repayment (correlation = 0.57, p < 0.001), indicating that larger working capital disbursements require more time to generate initial cash returns.

```bash
python3 loan_statistical_analysis.py
```

---

## Day 14: Kisumu Schools Attendance and Infrastructure (Multi-Dataset)

Cleans naming differences, removes a duplicate row, handles missing values, and merges attendance logs with infrastructure records across 17 public schools in Kisumu County.

- **Classrooms vs Attendance**: Positive correlation ($r = 0.740, p = 0.0010$, $N = 16$ complete records).
- **Water Access Impact**: Schools with reliable clean water average 87.2% attendance compared to 75.6% for schools without water ($t = 5.04, p = 0.0002$).

**Finding for Education Officer**:
> School classroom capacity has a clear positive link with student attendance (r = 0.74, p = 0.001), though clean water access is just as critical, with water-enabled schools averaging 11.6 percentage points higher daily attendance than schools without water.

```bash
python3 school_infrastructure_attendance_analysis.py
```

---

## Day 15: Nairobi Produce Market Price Volatility (Complex Analysis)

Combines 6 months of daily Wakulima Market prices (January to June 2026) with crop metadata for Tomatoes, Sukuma Wiki, Irish Potatoes, Red Onions, and Cabbages. Full report and charts are in [`nairobi_produce_market/README.md`](nairobi_produce_market/README.md).

**Summary of Findings**:
> Tomatoes show the highest wholesale price volatility in Nairobi (CV = 33.5%), peaking in May 2026 at KES 220.3/kg (May 8) when heavy rains and muddy farm roads push monthly average prices 106% above January levels. Sukuma Wiki is the second most volatile crop (CV = 27.7%), peaking earlier across late February and early March (KES 76.0/kg on March 1; February average KES 58.8/kg) during dry-season irrigation shortages before dropping in April. Although Red Onions have the highest average price (KES 137.7/kg), their 45-day shelf life lets wholesalers smooth out supply shocks, keeping volatility low (CV = 11.1%) right next to Cabbages, the most stable crop (CV = 10.5%). Across all five crops, shorter shelf life lines up strongly with higher price swings (r = -0.73), so restaurants and grocers should lock in supplier agreements before late February for leafy greens and before late April for tomatoes.

```bash
python3 nairobi_produce_market/produce_market_analysis.py
```

---

## Dependencies

```bash
pip install pandas numpy scipy matplotlib
```
