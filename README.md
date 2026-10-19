# Week 1: API Integration, Authentication, CLI Tools & Web Fetch

This repository contains the command-line tools, web applications, and exercises built during Week 1. It covers making HTTP requests, securing API keys with `.env`, handling HTTP and network errors gracefully, chaining multiple API calls together, caching responses locally as JSON, and browser-based asynchronous data fetching with `fetch()` and `async/await`.

---

## Project Structure

```text
├── .env                       # Local environment variables (ignored by git)
├── .gitignore                 # Ignores .env, __pycache__, and cached JSON files
├── README.md                  # Week 1 documentation
├── week-1/
│   ├── day1_api_basics.py     # Day 1: Basic API requests & JSON parsing
│   ├── day2_exercise.py       # Day 2: Authenticated ExchangeRate-API CLI
│   ├── day3_travel_info.py    # Day 3: Travel Weather & Country Info Tool (with JSON cache)
│   ├── day3_exercise.py       # Day 3: Book & Author Explorer CLI (Chained APIs)
│   ├── day4_fetch.html        # Day 4: Browser-based data fetching with fetch() & async/await
│   ├── day4_exercise.html     # Day 4: Live Weather Explorer Web App (loading & error states)
│   └── project/               # Week 1 Project: RainGaugeKE (Rain Onset Analyser)
│       ├── index.html         # Web application
│       ├── README.md          # Project documentation with screenshots
│       └── screenshots/       # Application screenshots
└── week_2/
    └── day1_brief_analysis.md # Day 1: Freelance brief analysis and proposal prep
```

---

## Setup & Installation

### 1. Install Dependencies

Make sure your virtual environment is active, then install the required Python packages:

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

### 5. Day 4 Lesson: Browser-Based Data Fetching (`week-1/day4_fetch.html`)

- **What It Does**: Demonstrates asynchronous HTTP requests from client-side JavaScript in the browser using the Fetch API (`fetch()`) with `async/await`, dynamic DOM updates, and handling CORS-compliant REST endpoints.
- **Key Features**:
  - Fetches country data from an open, CORS-supported countries API.
  - Extracts and displays flag codes, common names, capital, region, and formatted population numbers.
  - Traps and displays network/HTTP errors cleanly within the UI.
- **How to Run**:
  Open `week-1/day4_fetch.html` directly in any web browser, or run a local web server:
  ```bash
  python -m http.server 8000
  # Open in browser: http://localhost:8000/week-1/day4_fetch.html
  ```

### 6. Day 4 Exercise: Live Weather Explorer Web App (`week-1/day4_exercise.html`)

- **Problem It Solves**: Looking up real-time weather information via an interactive, responsive web UI with immediate feedback, robust loading indicators, and error resilience without needing an API key.
- **Key Features**:
  - **Chained Public APIs**: Queries Open-Meteo Geocoding to translate any entered city name into geographic coordinates, then requests live forecast metrics from the Open-Meteo Weather API.
  - **Loading State**: Displays an animated spinner and `"Loading live weather data..."` feedback while temporarily disabling input triggers to prevent redundant requests.
  - **Formatted Output**: Displays temperature (in degrees Celsius), "feels like" temperature, translated WMO weather condition descriptions, humidity (%), wind speed (km/h), and precipitation (mm).
  - **Error State**: Displays a clear, accessible warning card with specific troubleshooting messages when a location cannot be found or if a network interruption occurs.
  - **Interactive Controls**: Supports form submission via Enter key and provides quick-pick city chips (including a bad-value test chip).
- **How to Run**:
  Open `week-1/day4_exercise.html` directly in any web browser, or run a local web server:
  ```bash
  python -m http.server 8000
  # Open in browser: http://localhost:8000/week-1/day4_exercise.html
  ```

---

## Week 1 Project: RainGaugeKE (Rain Onset Analyser)

- **Location**: [`week-1/project/`](week-1/project/)
- **Documentation**: Detailed technical guide, onset formula, and screenshots available in [`week-1/project/README.md`](week-1/project/README.md).
- **Problem Solved**: Helps Kenyan smallholder farmers avoid losing sown seeds to false rainfall starts by evaluating current season rainfall against the official ICPAC onset-of-rains rule and 20 years of historical climate data (ERA5 reanalysis).
- **Key Features**:
  - Clear planting signals: **GO**, **GET READY**, or **WAIT**.
  - Three interactive Chart.js charts comparing current cumulative rain, daily distribution, and 20-year onset dates.
  - 100% keyless integration across three Open-Meteo endpoints (Geocoding, Historical Weather, and Forecast APIs).
- **How to Run**:
  Open `week-1/project/index.html` directly in any web browser, or serve locally:
  ```bash
  python3 -m http.server 8000 --directory week-1/project
  # Open in browser: http://localhost:8000
  ```
