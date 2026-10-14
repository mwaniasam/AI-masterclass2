# Week 1: API Integration, Authentication & CLI Tools

This repository contains the command-line tools and exercises built during Week 1. It covers making HTTP requests, securing API keys with `.env`, handling HTTP and network errors gracefully, chaining multiple API calls together, and caching responses locally as JSON.

---

## Project Structure

```text
├── .env                       # Local environment variables (ignored by git)
├── .gitignore                 # Ignores .env, __pycache__, and cached JSON files
├── README.md                  # Week 1 documentation
└── week-1/
    ├── day1_api_basics.py     # Day 1: Basic API requests & JSON parsing
    ├── day2_exercise.py       # Day 2: Authenticated ExchangeRate-API CLI
    ├── day3_travel_info.py    # Day 3: Travel Weather & Country Info Tool (with JSON cache)
    └── day3_exercise.py       # Day 3: Book & Author Explorer CLI (Chained APIs)
```

---

## Setup & Installation

### 1. Install Dependencies

Make sure your virtual environment is active, then install the required packages:

```bash
pip install requests python-dotenv
```

### 2. Configure Environment Variables

Create a `.env` file in the root directory and add your API keys:

```text
EXCHANGE_RATE_KEY=your_exchangerate_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
RESTCOUNTRIES_API_KEY=your_restcountries_v5_api_key
```

*(Note: `.env` is listed in `.gitignore` so secret keys are never committed to GitHub).*

---

## Week 1 Scripts & Exercises

### 1. Day 1: API Fundamentals (`week-1/day1_api_basics.py`)

- **What It Does**: Introduces making GET requests to public endpoints, inspecting status codes, and extracting specific fields from nested JSON responses.
- **How to Run**:
  ```bash
  python week-1/day1_api_basics.py
  ```

### 2. Day 2 Exercise: Live Currency Exchange CLI (`week-1/day2_exercise.py`)

- **Problem It Solves**: Checking live foreign exchange rates across major currencies (USD, EUR, GBP, KES, JPY) directly from the terminal without exposing API credentials in source code.
- **Key Features**:
  - Loads `EXCHANGE_RATE_KEY` securely from `.env`.
  - Explicitly handles HTTP 401/403 (invalid/unauthorized key), HTTP 404 (unsupported currency code), and network timeouts.
  - Formats conversion rates into a clean, aligned terminal table.
- **How to Run**:
  ```bash
  python week-1/day2_exercise.py
  ```

### 3. Day 3 Lesson: Travel Weather & Country Info Tool (`week-1/day3_travel_info.py`)

- **Problem It Solves**: Travelers need both current local weather and essential country context (region, population, currency) in one place without hitting API rate limits on repeated lookups.
- **Key Features**:
  - **Chained APIs**: Fetches live weather and the 2-letter country code from OpenWeatherMap, then passes that code to REST Countries v5 (Bearer authentication).
  - **Local JSON Caching**: Saves weather responses to `<city>_weather.json` and loads from the local cache on repeat queries to save API calls.
- **How to Run**:
  ```bash
  python week-1/day3_travel_info.py
  ```

### 4. Day 3 Exercise: Book & Author Explorer CLI (`week-1/day3_exercise.py`)

- **Problem It Solves**: Looking up a book's publication history alongside its author's biography usually requires searching multiple pages. This tool combines both into a single terminal lookup and saves the complete record for offline use.
- **Key Features**:
  - **Chained API Calls**: Queries the Open Library Search API by book title to get publication year, edition count, and the unique `author_key`, then chains that key into the Open Library Authors API to pull the author's birth date and biography.
  - **Offline Record**: Saves the combined book and author payload into `<book_title>_record.json`.
  - **Error Handling**: Gracefully handles empty inputs, unfound book titles, and network connection failures.
- **How to Run**:
  ```bash
  python week-1/day3_exercise.py
  ```
