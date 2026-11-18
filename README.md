# AI Masterclass — Phase II (Track B: Data Analyst)

This repository holds my projects, scripts, datasets, and written exercises from Phase II of the AI Masterclass (Data Analyst track). It covers API integration and browser-based apps in Week 1, freelance client delivery in Week 2, and advanced data analysis with pandas, statistics, and visualization in Week 3.

---

## Repository Layout

```text
AI-masterclass2/
|-- .gitignore
|-- README.md
|-- week-1/                                  # APIs, CLI tools, and browser fetch
|   |-- day1_api_basics.py                   # Basic GET requests and JSON parsing
|   |-- day1_exercise.py                     # Open-Meteo current weather lookup
|   |-- day2_weather.py                      # Authenticated OpenWeatherMap script
|   |-- day2_exercise.py                     # Currency exchange CLI with .env and error handling
|   |-- day3_travel_info.py                  # Chained weather + country info with JSON cache
|   |-- day3_exercise.py                     # Chained Open Library book and author lookup
|   |-- day4_fetch.html                      # Browser fetch() and async/await demo
|   |-- day4_exercise.html                   # Live weather explorer web app (Open-Meteo)
|   \-- project/                             # RainGaugeKE rain onset web app
|       |-- index.html
|       |-- README.md
|       \-- screenshots/
|-- week_2/                                  # Client communication and delivery
|   |-- day1_brief_analysis.md               # Breaking down a freelance client brief
|   |-- day2_proposal.md                     # Fixed-price MVP proposal
|   |-- day3_delivery.md                     # Project handover notes
|   |-- day4_project_agreement.md            # Scope and payment agreement (attendance SMS tool)
|   |-- day5_client_cycle.md                 # End-to-end client delivery cycle
|   |-- exchange_rate_tracker.py             # Live USD/KES rate tracker
|   \-- dairy_calculator/                    # Kiambu Dairy Co-op payout CLI (tagged v1.0)
|       |-- dairy_calculator.py
|       |-- price.txt
|       \-- README.md
\-- week_3/                                  # Advanced data analysis (pandas, stats, charts)
    |-- daily_collection.csv                 # Day 11: Nakuru dairy daily deliveries
    |-- farmer_details.csv                   # Day 11: Farmer zones and buying rates
    |-- dairy_zone_analysis.py               # Day 11: Zone merge and payout summary
    |-- zone_monthly_summary.csv             # Day 11: Exported monthly summary
    |-- day1_advanced_pandas.md              # Day 11 notes
    |-- nairobi_supermarket_transactions.csv # Day 12: 18-month daily checkout counts
    |-- supermarket_traffic_analysis.py      # Day 12: Rolling averages and resampling
    |-- supermarket_traffic_trend.png        # Day 12: Dual-axis foot traffic chart
    |-- day2_time_series.md                  # Day 12 notes
    |-- mombasa_mfi_loans.csv                # Day 13: 150 coastal microfinance loan records
    |-- loan_statistical_analysis.py         # Day 13: Descriptive stats, IQR outliers, correlation
    |-- loan_amount_distribution.png         # Day 13: Loan distribution histogram
    |-- day3_statistical_analysis.md         # Day 13 notes
    |-- kisumu_school_attendance.csv         # Day 14: School attendance (with naming/duplicate issues)
    |-- kisumu_school_infrastructure.csv     # Day 14: Classrooms and water access survey
    |-- school_infrastructure_attendance_analysis.py  # Day 14: Cleaning, merging, correlation
    |-- school_attendance_vs_classrooms.png  # Day 14: Attendance vs classrooms scatter plot
    |-- day4_multi_dataset_analysis.md       # Day 14 notes
    |-- nairobi_produce_market/              # Day 15: 6-month Nairobi produce price study (tagged week3-v1.0)
    |   |-- data/                            # Daily wholesale prices and crop metadata
    |   |-- charts/                          # Trends, volatility, and monthly heatmap charts
    |   |-- produce_market_analysis.py       # Full cleaning, volatility, and plotting pipeline
    |   \-- README.md                        # Client-facing report with embedded charts
    |-- day5_complex_analysis_project.md     # Day 15 notes
    \-- README.md                            # Week 3 overview and findings
```

---

## Setup

Install the Python dependencies used across Weeks 1 to 3:

```bash
pip install requests python-dotenv pandas numpy scipy matplotlib
```

For Week 1 scripts that require API keys (`day2_weather.py`, `day2_exercise.py`, `day3_travel_info.py`), add a `.env` file in the project root (ignored by Git):

```text
EXCHANGE_RATE_KEY=your_exchangerate_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
RESTCOUNTRIES_API_KEY=your_restcountries_v5_api_key
```

---

## Week 1: APIs, CLI Tools, and Browser Fetch

Focused on calling public and authenticated REST APIs, keeping credentials out of code with `.env`, handling network errors, caching JSON locally, and fetching live data in the browser.

- **CLI Scripts**:
  - [`day1_api_basics.py`](week-1/day1_api_basics.py) and [`day1_exercise.py`](week-1/day1_exercise.py): GET requests, JSON parsing, and live weather from Open-Meteo.
  - [`day2_weather.py`](week-1/day2_weather.py) and [`day2_exercise.py`](week-1/day2_exercise.py): Authenticated OpenWeatherMap and ExchangeRate-API tools with HTTP status handling.
  - [`day3_travel_info.py`](week-1/day3_travel_info.py) and [`day3_exercise.py`](week-1/day3_exercise.py): Chained multi-API lookups (OpenWeatherMap + REST Countries; Open Library search + author bio) with local JSON caching.
- **Browser Apps**:
  - [`day4_fetch.html`](week-1/day4_fetch.html) and [`day4_exercise.html`](week-1/day4_exercise.html): Client-side `fetch()` and `async/await` with loading spinners and error states.
- **Week 1 Project — RainGaugeKE** ([`week-1/project/`](week-1/project/)):
  A keyless web app that helps Kenyan smallholder farmers avoid false starts to the planting season by checking current rainfall against 20 years of ERA5 historical weather data and the ICPAC onset rule. Outputs clear **GO**, **GET READY**, or **WAIT** signals alongside three Chart.js visualizations. See [`week-1/project/README.md`](week-1/project/README.md).

---

## Week 2: Client Delivery and Practical Tools

Focused on scoping real freelance briefs, writing proposals and agreements, packaging clean deliverables, and shipping working code to non-technical clients.

- **Client Documentation**: Brief analysis ([`day1_brief_analysis.md`](week_2/day1_brief_analysis.md)), fixed-price proposal ([`day2_proposal.md`](week_2/day2_proposal.md)), professional handover ([`day3_delivery.md`](week_2/day3_delivery.md)), project agreement ([`day4_project_agreement.md`](week_2/day4_project_agreement.md)), and full delivery walkthrough ([`day5_client_cycle.md`](week_2/day5_client_cycle.md)).
- **Live Exchange Rate Tracker** ([`week_2/exchange_rate_tracker.py`](week_2/exchange_rate_tracker.py)): Standard-library script pulling live USD/KES rates and converting benchmark amounts.
- **Week 2 Project — Kiambu Dairy Co-op Calculator** ([`week_2/dairy_calculator/`](week_2/dairy_calculator/), tagged `v1.0`):
  A zero-dependency CLI tool for a 30-farmer dairy cooperative. Staff update the weekly buying price in `price.txt` without touching Python code, then enter deliveries to get instant payout summaries. See [`week_2/dairy_calculator/README.md`](week_2/dairy_calculator/README.md).

---

## Week 3: Advanced Data Analysis

Focused on real-world Kenyan datasets using pandas, NumPy, SciPy, and Matplotlib. Full summaries and run commands are in [`week_3/README.md`](week_3/README.md).

- **Day 11 — Nakuru Dairy Co-op Zone Analysis** ([`dairy_zone_analysis.py`](week_3/dairy_zone_analysis.py)): Merges daily milk deliveries with farmer master data to report litres, payouts (KES 321,595.20 across 5,776.7 litres), and top producers by zone.
- **Day 12 — Nairobi Supermarket Foot Traffic** ([`supermarket_traffic_analysis.py`](week_3/supermarket_traffic_analysis.py)): 18-month time-series study using monthly resampling and a 30-day rolling average, separating 32.3% underlying customer growth from February dips and December holiday peaks.
- **Day 13 — Mombasa Microfinance Loan Portfolio** ([`loan_statistical_analysis.py`](week_3/loan_statistical_analysis.py)): Analyzes 150 loans using descriptive statistics, Tukey's IQR outlier rule (8 commercial loans above KES 69,937.50), and Pearson correlation ($r = 0.57, p < 0.001$ between loan size and first-repayment lag).
- **Day 14 — Kisumu Schools Attendance and Infrastructure** ([`school_infrastructure_attendance_analysis.py`](week_3/school_infrastructure_attendance_analysis.py)): Cleans inconsistent school names, removes a duplicate record, handles missing values, and merges attendance with infrastructure data ($r = 0.74$ between classrooms and attendance; +11.6 percentage points higher attendance at schools with clean water).
- **Day 15 — Nairobi Produce Market Price Volatility** ([`week_3/nairobi_produce_market/`](week_3/nairobi_produce_market/), tagged `week3-v1.0`): Combines 6 months of daily Wakulima Market prices with crop shelf-life metadata across five vegetables. Shows Tomatoes are the most volatile crop (CV = 33.5%, peaking at KES 220.3/kg on May 8), Sukuma Wiki peaks in late February/early March (CV = 27.7%), and Cabbages are the most stable (CV = 10.5%). See [`week_3/nairobi_produce_market/README.md`](week_3/nairobi_produce_market/README.md).
