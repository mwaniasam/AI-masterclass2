# Phase II - Track B: Data Analyst - Week 3 - Day 15: Project - Complex Analysis

Course Day: Day 15 of 40  
Track: Track B (Data Analyst)  
Focus: End-to-End Multi-Table Time Series, Volatility Modeling, Publication Visualization, and GitHub Release Tagging  
Capstone Project: Nairobi Produce Market (Wakulima) — 6-Month Vegetable Price Volatility & Seasonality Study  

---

## 1. Capstone Integration of Week 3 Skills

Day 15 synthesizes every advanced analytical technique learned across Week 3 into a single reproducible portfolio project:

| Week 3 Module | Skill Applied in Day 15 Capstone | Implementation Detail |
|:---|:---|:---|
| **Day 11: Advanced Pandas** | Multi-table relational join (`pd.merge`), pivot tables (`pivot_table`), grouped aggregations | Merged `produce_daily_prices.csv` with `vegetable_metadata.csv` and generated the 5x6 monthly price pivot matrix |
| **Day 12: Time Series Analysis** | `DatetimeIndex`, 14-day rolling averages, monthly aggregation, chronological peak detection | Computed smoothed 14-day trendlines per crop and pinpointed exact daily peak dates |
| **Day 13: Statistical Analysis** | Descriptive statistics, IQR outlier detection, Pearson correlation, scale-adjusted volatility | Computed Coefficient of Variation ($\text{CV}\%$), IQR spike distributions, and shelf-life correlation ($r = -0.73$) |
| **Day 14: Multi-Dataset Hygiene** | Schema harmonization, string canonicalization, deduplication, missing-value imputation | Renamed `produce_item` -> `vegetable`, fixed 6 naming typos, removed 2 duplicates, interpolated 4 missing daily prices |

---

## 2. Mathematical First Principles Behind the Analysis

### Why Coefficient of Variation ($\text{CV}$) Beats Raw Standard Deviation ($s$) for Volatility
A common mistake when comparing volatility across commodities is ranking items by raw standard deviation ($s$). Standard deviation carries the same measurement unit as the variable (KES/kg), making direct comparison across different price tiers misleading:

- **Red Onions**: $\bar{x} = \text{KES } 137.7/\text{kg}$, $s = \text{KES } 15.3/\text{kg}$.
- **Sukuma Wiki**: $\bar{x} = \text{KES } 43.3/\text{kg}$, $s = \text{KES } 12.0/\text{kg}$.

Looking at raw standard deviation alone would falsely suggest Red Onions are more volatile than Sukuma Wiki ($15.3 > 12.0$). However, a KES 12 swing on a KES 43 commodity represents a massive proportional shock to a buyer's budget, whereas a KES 15 swing on a KES 138 commodity is relatively mild.

Normalizing standard deviation by the arithmetic mean produces the dimensionless **Coefficient of Variation**:

$$\text{CV} = \left(\frac{s}{\bar{x}}\right) \times 100\%$$

Applying $\text{CV}$ reveals the true economic risk ordering:
- **Tomatoes**: $\frac{40.5}{121.1} \times 100\% = 33.5\%$ (Highest volatility)
- **Sukuma Wiki**: $\frac{12.0}{43.3} \times 100\% = 27.7\%$ (Second highest volatility)
- **Irish Potatoes**: $\frac{12.3}{76.6} \times 100\% = 16.1\%$ (Moderate volatility)
- **Red Onions**: $\frac{15.3}{137.7} \times 100\% = 11.1\%$ (Low volatility)
- **Cabbages**: $\frac{5.1}{48.8} \times 100\% = 10.5\%$ (Most stable)

### Why Time-Aware Linear Interpolation Beats Mean Imputation
When a daily price series has a missing observation on a single day (e.g. a market clerk skipped logging Tomatoes on March 19), replacing the gap with the 6-month column mean (KES 121.1) would inject an artificial vertical spike during a KES 93 March baseline!

Instead, grouping by crop and running `series.interpolate(method="time")` fills the gap along the straight line connecting March 18 and March 20, preserving local temporal continuity and avoiding distortion in 14-day rolling averages.

---

## 3. Four-Sentence Executive Findings Summary

> Tomatoes exhibit the highest wholesale price volatility in Nairobi (CV = 33.5%), peaking sharply in May 2026 at KES 220.3/kg (May 8), when heavy long rains and farm-road disruptions push monthly average prices 106% above January levels. Sukuma Wiki ranks second in volatility (CV = 27.7%), following an opposite seasonal cycle that peaks across late February and early March (KES 76.0/kg on March 1; February average KES 58.8/kg) during dry-season irrigation shortages before falling rapidly in April. Although Red Onions command the highest average price (KES 137.7/kg), their 45-day ambient shelf life allows wholesalers to buffer supply shocks, keeping relative volatility much lower (CV = 11.1%) alongside Cabbages, the most stable staple (CV = 10.5%). Across all five staples, shorter crop shelf life strongly tracks higher price risk (r = -0.73), meaning restaurants and institutional buyers should lock in supplier contracts ahead of late February for leafy greens and ahead of late April for tomatoes.

---

## 4. Portfolio Deliverables

All standalone project assets live inside [`nairobi_produce_market/`](file:///home/mwaniasamuel/AI-masterclass2/week_3/nairobi_produce_market):
- Data tables: [`produce_daily_prices.csv`](file:///home/mwaniasamuel/AI-masterclass2/week_3/nairobi_produce_market/data/produce_daily_prices.csv) and [`vegetable_metadata.csv`](file:///home/mwaniasamuel/AI-masterclass2/week_3/nairobi_produce_market/data/vegetable_metadata.csv)
- Pipeline script: [`produce_market_analysis.py`](file:///home/mwaniasamuel/AI-masterclass2/week_3/nairobi_produce_market/produce_market_analysis.py)
- Chart 1 (Trends & Peaks): [`vegetable_price_trends.png`](file:///home/mwaniasamuel/AI-masterclass2/week_3/nairobi_produce_market/charts/vegetable_price_trends.png)
- Chart 2 (Volatility & Shelf Life): [`volatility_comparison.png`](file:///home/mwaniasamuel/AI-masterclass2/week_3/nairobi_produce_market/charts/volatility_comparison.png)
- Chart 3 (Seasonal Heatmap & Boxplots): [`monthly_seasonality.png`](file:///home/mwaniasamuel/AI-masterclass2/week_3/nairobi_produce_market/charts/monthly_seasonality.png)
- Client Report: [`nairobi_produce_market/README.md`](file:///home/mwaniasamuel/AI-masterclass2/week_3/nairobi_produce_market/README.md)

---

## 5. Git Release Tagging Note

Because this monorepo (`AI-masterclass2`) already contains an earlier `v1.0` tag pointing to the Week 2 Day 10 milestone (`2e8048b`), Week 3 Day 15 is tagged cleanly as **`week3-v1.0`** rather than overwriting shared remote tag history. This preserves immutable release auditability across all weeks of the program.
