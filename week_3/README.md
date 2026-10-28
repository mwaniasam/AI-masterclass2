# Phase II - Track B: Data Analyst - Week 3: Advanced Data Analysis

A collection of commercial data engineering, aggregation, and time series analytics projects developed during Week 3 of the AI Masterclass (Track B: Data Analyst).

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

## Technical Stack & Requirements

- Python 3.8+
- `pandas` (>= 2.0.0)
- `numpy` (>= 1.24.0)
- `matplotlib` (>= 3.8.0)

Install dependencies:
```bash
pip install pandas numpy matplotlib
```
