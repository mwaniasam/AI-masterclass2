# Nairobi Produce Market: 6-Month Vegetable Price Volatility & Seasonality Analysis

**Client Domain**: Wholesale Produce Procurement & Institutional Food Supply (Wakulima Market, Nairobi)  
**Observation Window**: January 1, 2026 to June 30, 2026 (181 calendar days, 5 staple vegetables)  
**Primary Business Question**: Which vegetable exhibits the highest price volatility in Nairobi wholesale markets, and when does each crop reach its seasonal price peak?

---

## Executive Findings Summary

> Tomatoes exhibit the highest wholesale price volatility in Nairobi (CV = 33.5%), peaking sharply in May 2026 at KES 220.3/kg (May 8), when heavy long rains and farm-road disruptions push monthly average prices 106% above January levels. Sukuma Wiki ranks second in volatility (CV = 27.7%), following an opposite seasonal cycle that peaks across late February and early March (KES 76.0/kg on March 1; February average KES 58.8/kg) during dry-season irrigation shortages before falling rapidly in April. Although Red Onions command the highest average price (KES 137.7/kg), their 45-day ambient shelf life allows wholesalers to buffer supply shocks, keeping relative volatility much lower (CV = 11.1%) alongside Cabbages, the most stable staple (CV = 10.5%). Across all five staples, shorter crop shelf life strongly tracks higher price risk (r = -0.73), meaning restaurants and institutional buyers should lock in supplier contracts ahead of late February for leafy greens and ahead of late April for tomatoes.

---

## Key Quantitative Results

### 1. Volatility and Peak Timing Summary (Ranked by Coefficient of Variation)

| Rank | Vegetable | Mean (KES/kg) | Std Dev (KES/kg) | Volatility (CV %) | Min (KES/kg) | Peak (KES/kg) | Peak Date | Peak Month | Shelf Life | Primary Source |
|:---:|:---|---:|---:|---:|---:|---:|:---:|:---:|:---:|:---|
| 1 | **Tomatoes** | 121.1 | 40.5 | **33.5%** | 79.5 | 220.3 | 2026-05-08 | May 2026 | 5 days | Kirinyaga |
| 2 | **Sukuma Wiki** | 43.3 | 12.0 | **27.7%** | 24.0 | 76.0 | 2026-03-01 | Feb 2026 | 2 days | Kiambu |
| 3 | **Irish Potatoes** | 76.6 | 12.3 | **16.1%** | 56.3 | 103.6 | 2026-04-22 | Apr 2026 | 30 days | Nyandarua |
| 4 | **Red Onions** | 137.7 | 15.3 | **11.1%** | 110.5 | 175.8 | 2026-03-09 | Mar 2026 | 45 days | Kajiado |
| 5 | **Cabbages** | 48.8 | 5.1 | **10.5%** | 38.2 | 59.0 | 2026-03-13 | Mar 2026 | 14 days | Nyandarua |

### 2. Monthly Average Wholesale Prices (KES / kg)

| Vegetable | Jan 2026 | Feb 2026 | Mar 2026 | Apr 2026 | May 2026 | Jun 2026 |
|:---|---:|---:|---:|---:|---:|---:|
| **Tomatoes** | 90.9 | 91.0 | 93.5 | 150.5 | **186.9** | 111.6 |
| **Sukuma Wiki** | 41.7 | **58.8** | 56.3 | 38.5 | 32.9 | 32.9 |
| **Irish Potatoes** | 70.5 | 70.0 | 78.3 | **97.3** | 80.3 | 62.8 |
| **Red Onions** | 131.9 | 144.3 | **162.3** | 141.5 | 124.9 | 121.3 |
| **Cabbages** | 48.7 | 52.9 | **56.0** | 47.9 | 44.1 | 43.2 |

---

## Visual Evidence

### Chart 1: 6-Month Daily Price Trends & 14-Day Rolling Averages per Vegetable
Answers: *How does each vegetable move day-to-day, and on what exact dates do price spikes peak?*

![Vegetable Price Trends](charts/vegetable_price_trends.png)

### Chart 2: Scale-Adjusted Price Volatility (CV%) & Perishability Analysis
Answers: *Which crop carries the greatest proportional price risk, and why do high-priced onions fluctuate less than cheaper sukuma wiki?*

![Volatility Comparison](charts/volatility_comparison.png)

### Chart 3: Seasonal Peak Calendar Heatmap & Distribution Risk Spread
Answers: *Which months pose the sharpest procurement budget exposure for each commodity?*

![Monthly Seasonality](charts/monthly_seasonality.png)

---

## Project Architecture

```text
nairobi_produce_market/
|-- data/
|   |-- produce_daily_prices.csv      # 907 raw daily wholesale records (with naming, duplicate, and gap imperfections)
|   \-- vegetable_metadata.csv        # Crop origin county, category, ambient shelf life, and perishability tier
|-- charts/
|   |-- vegetable_price_trends.png    # 5-panel daily + 14-day rolling trend chart with peak annotations
|   |-- volatility_comparison.png     # CV% volatility rankings and shelf-life regression plot
|   \-- monthly_seasonality.png       # Monthly peak heatmap and distribution boxplots
|-- produce_market_analysis.py        # End-to-end cleaning, merging, statistical, and charting pipeline
\-- README.md                         # Executive summary and project guide
```

---

## Data Hygiene & Engineering Steps Executed

1. **Schema & Name Harmonization**: Renamed `produce_item` to `vegetable` in metadata and standardized 6 raw spelling/casing/whitespace errors (`"  tomatoes "`, `"sukuma wiki"`, `"Red Onion"`).
2. **Deduplication**: Detected and removed 2 duplicate market clerk entries on identical `(date, vegetable)` pairs.
3. **Time-Aware Imputation**: Interpolated 4 missing daily wholesale prices using chronological linear interpolation per crop (`interpolate(method="time")`), resulting in 905 verified daily observations (181 days x 5 vegetables).
4. **Scale-Normalized Volatility**: Used Coefficient of Variation ($\text{CV} = \frac{s}{\bar{x}} \times 100\%$) rather than raw standard deviation alone so crops with different price scales (KES 43/kg vs KES 138/kg) could be compared rigorously.

---

## Actionable Procurement Recommendations

1. **Forward Contract Tomatoes Ahead of April**: Institutional kitchens and grocers should secure fixed-price greenhouse contracts or process tomato paste reserves by late March to avoid the +106% May long-rains surge.
2. **Diversify Leafy Green Sourcing in February**: Establish secondary irrigated suppliers in Kiambu or Naivasha prior to mid-February to hedge against the dry-season Sukuma Wiki spike.
3. **Bulk-Buy Storage Crops During Off-Peak Windows**: Use warehouse storage for Red Onions (45-day shelf life) and Irish Potatoes (30-day shelf life) in January–February and June to capture trough pricing.

---

## How to Run

```bash
pip install pandas numpy scipy matplotlib
python3 produce_market_analysis.py
```
