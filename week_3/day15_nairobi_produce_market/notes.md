# Week 3, Day 15: Complex Analysis Project

**Track**: Data Analyst (Phase II, Week 3)  
**Project**: Nairobi Produce Market — 6-Month Vegetable Price Volatility & Seasonality  
**Report**: [`README.md`](README.md)

---

## 1. What This Project Combines

Day 15 pulls together the main skills practiced across Days 11 to 14 into one full workflow:

- **Merging and pivots (Day 11)**: Joined daily wholesale prices (`data/produce_daily_prices.csv`) with crop metadata (`data/vegetable_metadata.csv`) and built a monthly average price matrix.
- **Time series (Day 12)**: Indexed records by date, calculated 14-day rolling averages to smooth daily noise, and pinned down exact peak dates and peak months.
- **Statistics (Day 13)**: Measured price volatility using Coefficient of Variation (CV%), checked IQR spike outliers, and ran a correlation between shelf life and volatility ($r = -0.73$).
- **Data cleaning (Day 14)**: Aligned mismatched column names (`produce_item` to `vegetable`), fixed 6 casing and spelling errors, dropped 2 duplicate entries, and filled 4 missing daily prices with time-based interpolation.

---

## 2. Key Analytical Choices

### Why Use Coefficient of Variation Instead of Standard Deviation Alone
Standard deviation is measured in KES/kg, so comparing raw values across crops at different price levels can mislead you:

- **Red Onions**: Mean = KES 137.7/kg, Std Dev = KES 15.3/kg
- **Sukuma Wiki**: Mean = KES 43.3/kg, Std Dev = KES 12.0/kg

On raw standard deviation alone, Red Onions look more volatile ($15.3 > 12.0$). In practice, a KES 12 swing on a KES 43 item hits a buyer's budget far harder than a KES 15 swing on a KES 138 item. Dividing by the mean gives a scale-free measure:

$$\text{CV} = \left(\frac{s}{\bar{x}}\right) \times 100\%$$

Ranked by CV%:
1. **Tomatoes**: 33.5% (most volatile)
2. **Sukuma Wiki**: 27.7%
3. **Irish Potatoes**: 16.1%
4. **Red Onions**: 11.1%
5. **Cabbages**: 10.5% (most stable)

### Why Time Interpolation Instead of Filling With the Mean
When a single day's price is missing (for example, Tomatoes on March 19), filling it with the 6-month average (KES 121.1/kg) would inject a fake spike into a quiet March period (~KES 93/kg). Using `interpolate(method="time")` per crop connects the day before and the day after, keeping the rolling averages honest.

---

## 3. Summary of Findings

Tomatoes exhibit the highest wholesale price volatility in Nairobi (CV = 33.5%), peaking sharply in May 2026 at KES 220.3/kg (May 8), when heavy long rains and farm-road disruptions push monthly average prices 106% above January levels. Sukuma Wiki ranks second in volatility (CV = 27.7%), following an opposite seasonal cycle that peaks across late February and early March (KES 76.0/kg on March 1; February average KES 58.8/kg) during dry-season irrigation shortages before falling rapidly in April. Although Red Onions command the highest average price (KES 137.7/kg), their 45-day ambient shelf life allows wholesalers to buffer supply shocks, keeping relative volatility much lower (CV = 11.1%) alongside Cabbages, the most stable staple (CV = 10.5%). Across all five staples, shorter crop shelf life strongly tracks higher price risk (r = -0.73), meaning restaurants and institutional buyers should lock in supplier contracts ahead of late February for leafy greens and ahead of late April for tomatoes.

---

## 4. Files Produced

- Data: [`data/produce_daily_prices.csv`](data/produce_daily_prices.csv), [`data/vegetable_metadata.csv`](data/vegetable_metadata.csv)
- Script: [`produce_market_analysis.py`](produce_market_analysis.py)
- Charts: [`charts/vegetable_price_trends.png`](charts/vegetable_price_trends.png), [`charts/volatility_comparison.png`](charts/volatility_comparison.png), [`charts/monthly_seasonality.png`](charts/monthly_seasonality.png)
- Project README: [`README.md`](README.md)

*Release tag note*: Since `v1.0` was already used on Week 2 Day 10, this Week 3 project is tagged as `week3-v1.0`.
