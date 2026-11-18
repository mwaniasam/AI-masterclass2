# AI Masterclass — Phase II (Track B: Data Analyst)

Projects, scripts, datasets, and written exercises from Phase II of the AI Masterclass (Data Analyst track). Each week is organized into self-contained folders with consistent naming (`week_1/`, `week_2/`, `week_3/`), a single `requirements.txt`, and relative paths inside every script so any analysis can be reproduced directly from the repository root.

---

## Quick Start

1. Clone the repository and create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. For Week 1 scripts that need API keys (`day2_weather.py`, `day2_exercise.py`, `day3_travel_info.py`), copy the template and fill in your credentials:
   ```bash
   cp .env.example .env
   ```
3. Run any script directly from the repository root (every script resolves its own `data/` and `charts/` paths automatically).

---

## Repository Structure

```text
AI-masterclass2/
|-- .env.example                                     # Template for Week 1 API keys
|-- .gitignore                                       # Ignores .env, caches, venvs, and local scratch files
|-- requirements.txt                                 # Python dependencies for all scripts
|-- README.md                                        # Repository guide
|
|-- week_1/                                          # APIs, CLI tools, and browser fetch
|   |-- exercises/
|   |   |-- day1_api_basics.py                       # Basic GET requests and JSON parsing
|   |   |-- day1_exercise.py                         # Open-Meteo current weather lookup
|   |   |-- day2_weather.py                          # Authenticated OpenWeatherMap script
|   |   |-- day2_exercise.py                         # Currency exchange CLI (.env + HTTP error checks)
|   |   |-- day3_travel_info.py                      # Chained weather + country info with JSON cache
|   |   |-- day3_exercise.py                         # Chained Open Library book and author lookup
|   |   |-- day4_fetch.html                          # Browser fetch() and async/await demo
|   |   \-- day4_exercise.html                       # Live weather explorer web app (Open-Meteo)
|   \-- project_raingaugeke/                         # RainGaugeKE rain onset web app
|       |-- index.html
|       |-- README.md
|       \-- screenshots/
|
|-- week_2/                                          # Client communication and delivery
|   |-- docs/
|   |   |-- day1_brief_analysis.md                   # Breaking down a freelance client brief
|   |   |-- day2_proposal.md                         # Fixed-price MVP proposal
|   |   |-- day3_delivery.md                         # Project handover notes
|   |   |-- day4_project_agreement.md                # Scope and payment agreement
|   |   \-- day5_client_cycle.md                     # End-to-end client delivery notes
|   |-- exchange_rate_tracker.py                     # Live USD/KES rate tracker (stdlib only)
|   \-- dairy_calculator/                            # Kiambu Dairy Co-op payout CLI (tagged v1.0)
|       |-- dairy_calculator.py
|       |-- price.txt
|       \-- README.md
|
\-- week_3/                                          # Advanced data analysis (pandas, stats, charts)
    |-- README.md                                    # Week 3 overview and findings
    |-- day11_nakuru_dairy/
    |   |-- data/                                    # daily_collection.csv, farmer_details.csv, summary CSV
    |   |-- dairy_zone_analysis.py
    |   \-- notes.md
    |-- day12_nairobi_supermarket/
    |   |-- data/                                    # nairobi_supermarket_transactions.csv
    |   |-- charts/                                  # supermarket_traffic_trend.png
    |   |-- supermarket_traffic_analysis.py
    |   \-- notes.md
    |-- day13_mombasa_mfi_loans/
    |   |-- data/                                    # mombasa_mfi_loans.csv
    |   |-- charts/                                  # loan_amount_distribution.png
    |   |-- loan_statistical_analysis.py
    |   \-- notes.md
    |-- day14_kisumu_schools/
    |   |-- data/                                    # kisumu_school_attendance.csv, infrastructure CSV
    |   |-- charts/                                  # school_attendance_vs_classrooms.png
    |   |-- school_infrastructure_attendance_analysis.py
    |   \-- notes.md
    \-- day15_nairobi_produce_market/                # Tagged week3-v1.0
        |-- data/                                    # produce_daily_prices.csv, vegetable_metadata.csv
        |-- charts/                                  # Trends, volatility, and monthly heatmap charts
        |-- produce_market_analysis.py
        |-- notes.md
        \-- README.md
```

---

## Week 1: APIs, CLI Tools, and Browser Fetch

Covers public and authenticated REST APIs, keeping keys in `.env`, error handling, local JSON caching, and client-side `fetch()` with `async/await`.

- **Exercises** ([`week_1/exercises/`](week_1/exercises/)): Python CLI tools for weather, exchange rates, travel info, and Open Library lookups, plus two interactive HTML weather/country apps.
- **RainGaugeKE** ([`week_1/project_raingaugeke/`](week_1/project_raingaugeke/)): Keyless browser app comparing live seasonal rainfall against 20 years of ERA5 history and the ICPAC onset rule to give Kenyan farmers clear **GO**, **GET READY**, or **WAIT** planting signals. Run locally with:
  ```bash
  python3 -m http.server 8000 --directory week_1/project_raingaugeke
  ```

---

## Week 2: Client Delivery and Practical Tools

Covers scoping briefs, writing proposals and agreements, and shipping lightweight tools for non-technical clients.

- **Client Docs** ([`week_2/docs/`](week_2/docs/)): Brief analysis, fixed-price proposal, handover notes, project agreement, and full delivery cycle documentation.
- **Live Exchange Rate Tracker** ([`week_2/exchange_rate_tracker.py`](week_2/exchange_rate_tracker.py)): Standard-library script fetching live USD/KES rates and converting benchmark amounts.
- **Kiambu Dairy Co-op Calculator** ([`week_2/dairy_calculator/`](week_2/dairy_calculator/), tagged `v1.0`): Zero-dependency payout CLI where staff update weekly prices in `price.txt` without editing Python code:
  ```bash
  python3 week_2/dairy_calculator/dairy_calculator.py
  ```

---

## Week 3: Advanced Data Analysis

Five self-contained Kenyan data analysis projects using pandas, NumPy, SciPy, and Matplotlib. Full findings are in [`week_3/README.md`](week_3/README.md).

| Day | Project | Key Result | Run Command |
|:---:|:---|:---|:---|
| 11 | [Nakuru Dairy Co-op](week_3/day11_nakuru_dairy/) | Merged deliveries & farmer rates across 3 zones (5,776.7 L, KES 321,595.20) | `python3 week_3/day11_nakuru_dairy/dairy_zone_analysis.py` |
| 12 | [Nairobi Supermarket Traffic](week_3/day12_nairobi_supermarket/) | 18-month series shows +32.3% baseline growth, Feb dips, and Dec surges | `python3 week_3/day12_nairobi_supermarket/supermarket_traffic_analysis.py` |
| 13 | [Mombasa MFI Loans](week_3/day13_mombasa_mfi_loans/) | 8 commercial outliers above KES 69,938; loan size correlates with repayment lag ($r = 0.57$) | `python3 week_3/day13_mombasa_mfi_loans/loan_statistical_analysis.py` |
| 14 | [Kisumu Schools](week_3/day14_kisumu_schools/) | Cleaned messy names & duplicates; classrooms ($r = 0.74$) and water (+11.6% pts) drive attendance | `python3 week_3/day14_kisumu_schools/school_infrastructure_attendance_analysis.py` |
| 15 | [Nairobi Produce Market](week_3/day15_nairobi_produce_market/) | 6-month Wakulima prices (`week3-v1.0`): Tomatoes most volatile (CV = 33.5%, peak May 8 at KES 220.3/kg) | `python3 week_3/day15_nairobi_produce_market/produce_market_analysis.py` |
