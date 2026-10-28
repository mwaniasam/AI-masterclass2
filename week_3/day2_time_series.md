# Phase II - Track B: Data Analyst - Week 3 - Day 12: Time Series Analysis

Course Day: Day 12 of 40  
Track: Track B (Data Analyst)  
Focus: Date-Indexed Data, Rolling Averages, Resampling, and Trend Visualization  
Project: Nairobi Supermarket Chain 18-Month Foot Traffic Trend Analysis  

---

## 1. Core Concepts & Techniques

### Step 1: Datetime-Indexed DataFrames
Time series analysis requires timestamps to be parsed into pandas `DatetimeIndex` structures. Once indexed by time, pandas unlocks time-aware slicing, rolling statistics, and resampling.

```python
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date").sort_index()
```

### Step 2: Growth Metrics & Rolling Averages
- **Percentage Change (`.pct_change()`)**: Measures period-over-period momentum.
- **Rolling Windows (`.rolling(window).mean()`)**: Smooths high-frequency daily noise and weekend spikes to reveal the true underlying trend.

```python
df["growth_pct"] = df["revenue_kes"].pct_change() * 100
df["rolling_30d"] = df["transactions"].rolling(30, min_periods=1).mean()
```

### Step 3: Frequency Resampling (`.resample()`)
Aggregates time series data across granularities (e.g. daily to weekly `W`, or daily to monthly `ME`):

```python
monthly_totals = df["transactions"].resample("ME").sum()
monthly_daily_avg = df["transactions"].resample("ME").mean()
```

### Step 4: Visualizing Trends for Non-Technical Stakeholders
Visualizations designed for executives should clearly decouple high-level monthly performance from smoothed daily trends. Using a dual-axis format allows plotting monthly aggregate volumes (bar chart) alongside the continuous 30-day moving average (line chart) without scale distortion.

### Step 5: Detecting Peaks, Dips, and Outliers
Identifying turning points using `.idxmax()` and `.idxmin()` allows analysts to correlate anomalies with calendar events, promotions, or macroeconomic shifts.

```python
best_month = monthly_totals.idxmax()
worst_month = monthly_totals.idxmin()
```

---

## 2. Practical Case Study: Nairobi Supermarket Chain

### The Business Context
The operations manager of a Nairobi supermarket chain wanted to understand whether store foot traffic was genuinely growing or simply fluctuating randomly. They required an analysis of 18 months of daily customer checkout counts (January 2025 to June 2026), resampled to monthly totals and smoothed with a 30-day rolling average.

### Dataset Overview (`nairobi_supermarket_transactions.csv`)
- **Period**: 546 consecutive days (January 1, 2025 to June 30, 2026)
- **Total Transactions**: 1,987,606 customer checkouts
- **Average Daily Traffic**: 3,640 customers/day
- **Day-of-Week Effect**: Weekends average +26.3% higher foot traffic (4,276 customers/day) compared to weekdays (3,386 customers/day)

---

## 3. Executive Report to the Operations Manager

### Two-Sentence Trend Assessment
> Foot traffic demonstrates genuine underlying growth of approximately 32.3% over the 18-month period (expanding from ~2,990 to ~3,960 baseline daily transactions on a 30-day rolling average), proving that customer volume is genuinely expanding rather than merely fluctuating. While baseline foot traffic is trending steadily upward, the business experiences predictable calendar seasonality characterized by a recurring post-holiday dip in February and an explosive ~100% volume surge during the December holiday shopping peak.

---

## 4. Key Quantitative Findings

| Metric | Value | Business Context |
|:---|:---|:---|
| **Peak Month** | **December 2025** (156,632 checkouts) | Holiday gift shopping, festive food stocking, and family gatherings |
| **Annual Trough** | **February 2025** (75,703 checkouts) | Post-holiday liquidity crunch ("Njaanuary" recovery) and Q1 school fee deadlines |
| **Holiday Volume Surge** | **+106.9%** | December checkout volume more than doubles February baseline |
| **Smoothed Baseline Start** | **2,992 customers/day** | 30-day rolling average in early 2025 |
| **Smoothed Baseline End** | **3,958 customers/day** | 30-day rolling average in mid 2026 |
| **Net Structural Growth** | **+32.3%** | Verifiable expansion in recurring daily shopper base |

---

## 5. Visual Artifact

The high-resolution visualization is saved in the repository at [`supermarket_traffic_trend.png`](file:///home/mwaniasamuel/AI-masterclass2/week_3/supermarket_traffic_trend.png):

- **Blue Bars (Left Axis)**: Total monthly customer transactions in thousands.
- **Red Line (Right Axis)**: 30-day rolling daily average, highlighting the smooth upward trajectory and seasonal peaks.
- **Callout Annotations**: Explicitly tag the December holiday spike, February post-holiday trough, and structural trendline for quick non-technical comprehension.

---

## 6. Actionable Operational Recommendations

1. **Staffing and Cashier Rostering**:
   - Schedule peak cashier shifts on Friday evenings and Saturdays to accommodate the recurring +26.3% weekend traffic surge.
   - Plan seasonal temporary hiring 4 to 6 weeks ahead of December to absorb the 100%+ holiday volume spike.

2. **Inventory and Supply Chain Planning**:
   - Draw down safety stock in late January and plan promotional clearance sales in February to offset the predictable annual dip.
   - Lock in distributor supply agreements in October and November to prevent stockouts during December's peak checkout rush.
