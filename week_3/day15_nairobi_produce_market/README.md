# Nairobi Produce Market: Vegetable Price Volatility Analysis

An analysis of 6 months of daily wholesale prices (January to June 2026) for five staple vegetables at Wakulima Market in Nairobi. The goal is to find out which vegetable has the sharpest price swings and when each crop peaks so buyers can plan purchasing around seasonal spikes.

---

## Key Findings

Tomatoes show the highest wholesale price volatility in Nairobi (CV = 33.5%), peaking in May 2026 at KES 220.3/kg (May 8) when heavy rains and muddy farm roads push monthly average prices 106% above January levels. Sukuma Wiki is the second most volatile crop (CV = 27.7%), peaking earlier across late February and early March (KES 76.0/kg on March 1; February average KES 58.8/kg) during dry-season irrigation shortages before dropping in April. Although Red Onions have the highest average price (KES 137.7/kg), their 45-day shelf life lets wholesalers smooth out supply shocks, keeping volatility low (CV = 11.1%) right next to Cabbages, the most stable crop (CV = 10.5%). Across all five crops, shorter shelf life lines up strongly with higher price swings (r = -0.73), so restaurants and grocers should lock in supplier agreements before late February for leafy greens and before late April for tomatoes.

---

## Volatility and Peak Summary

| Rank | Vegetable | Mean (KES/kg) | Std Dev | CV % | Min | Peak | Peak Date | Peak Month | Shelf Life | Main Source |
|:---:|:---|---:|---:|---:|---:|---:|:---:|:---:|:---:|:---|
| 1 | **Tomatoes** | 121.1 | 40.5 | **33.5%** | 79.5 | 220.3 | 2026-05-08 | May 2026 | 5 days | Kirinyaga |
| 2 | **Sukuma Wiki** | 43.3 | 12.0 | **27.7%** | 24.0 | 76.0 | 2026-03-01 | Feb 2026 | 2 days | Kiambu |
| 3 | **Irish Potatoes** | 76.6 | 12.3 | **16.1%** | 56.3 | 103.6 | 2026-04-22 | Apr 2026 | 30 days | Nyandarua |
| 4 | **Red Onions** | 137.7 | 15.3 | **11.1%** | 110.5 | 175.8 | 2026-03-09 | Mar 2026 | 45 days | Kajiado |
| 5 | **Cabbages** | 48.8 | 5.1 | **10.5%** | 38.2 | 59.0 | 2026-03-13 | Mar 2026 | 14 days | Nyandarua |

### Monthly Average Wholesale Prices (KES / kg)

| Vegetable | Jan | Feb | Mar | Apr | May | Jun |
|:---|---:|---:|---:|---:|---:|---:|
| **Tomatoes** | 90.9 | 91.0 | 93.5 | 150.5 | **186.9** | 111.6 |
| **Sukuma Wiki** | 41.7 | **58.8** | 56.3 | 38.5 | 32.9 | 32.9 |
| **Irish Potatoes** | 70.5 | 70.0 | 78.3 | **97.3** | 80.3 | 62.8 |
| **Red Onions** | 131.9 | 144.3 | **162.3** | 141.5 | 124.9 | 121.3 |
| **Cabbages** | 48.7 | 52.9 | **56.0** | 47.9 | 44.1 | 43.2 |

---

## Charts

### 1. Daily Price Trends and 14-Day Rolling Averages
Tracks day-to-day movement for each vegetable and marks exact peak dates.

![Vegetable Price Trends](charts/vegetable_price_trends.png)

### 2. Volatility Ranking (CV%) and Shelf-Life Relationship
Compares proportional volatility across crops and shows how perishability drives price swings.

![Volatility Comparison](charts/volatility_comparison.png)

### 3. Monthly Peak Heatmap and Price Spread
Highlights peak procurement months alongside 6-month price distributions and IQR outliers.

![Monthly Seasonality](charts/monthly_seasonality.png)

---

## Data Cleaning and Methodology

- **Files merged**: Joined 907 daily price records (`data/produce_daily_prices.csv`) with crop metadata (`data/vegetable_metadata.csv`) after renaming `produce_item` to `vegetable`.
- **Cleaned issues**: Fixed 6 naming/whitespace typos (`"  tomatoes "`, `"sukuma wiki"`, `"Red Onion"`), dropped 2 duplicate rows, and filled 4 missing daily prices using time interpolation per crop, leaving 905 clean records (181 days x 5 vegetables).
- **Volatility metric**: Ranked crops by Coefficient of Variation (`Std Dev / Mean * 100`) instead of raw standard deviation so cheaper and pricier items are compared fairly.

---

## Recommendations for Buyers

1. **Lock in tomato supply by late March**: Use fixed-price greenhouse contracts or paste reserves ahead of the April–May rains.
2. **Add irrigated leafy-green suppliers before February**: Hedge against dry-season Sukuma Wiki shortages in late February.
3. **Stock up on storage crops during low months**: Buy Red Onions and Irish Potatoes in bulk during January–February and June when prices sit near their floor.

---

## How to Run

```bash
pip install pandas numpy scipy matplotlib
python3 produce_market_analysis.py
```
