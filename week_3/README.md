# Nakuru Dairy Co-op - Advanced Zone Milk & Payout Analytics

An automated data transformation and analytics pipeline that merges daily milk collection records with farmer master files, calculates gross volume and financial payouts by geographic zone, identifies top producers, and generates an executive summary table.

---

## Business Context

A dairy cooperative manager in Nakuru County receives two separate operational spreadsheets:
1. **Daily Milk Collections**: Logged at the weighbridge each morning per farmer.
2. **Farmer Master Registry**: Zone assignments and agreed buying rates per litre.

This analytics tool merges these two disparate sources, computes monthly zone aggregations, identifies the highest milk supplier in each zone, and formats the output for immediate management review and board reporting.

---

## Required Input Files

The script expects two CSV files in the project directory:

### 1. `daily_collection.csv`
Contains the granular, daily milk drop-off records.
- `farmer_name` (string): Full name of the farmer.
- `date` (string/date): Date of delivery (e.g. `YYYY-MM-DD`).
- `litres` (float): Milk volume delivered in litres.

Example:
```csv
farmer_name,date,litres
John Kamau,2026-10-01,34.1
Mary Wanjiku,2026-10-01,52.3
Peter Njoroge,2026-10-01,20.9
```

### 2. `farmer_details.csv`
Contains member registration metadata and commercial agreements.
- `farmer_name` (string): Full name of the farmer (merge key).
- `zone` (string): Cooperative collection area (`Bahati`, `Njoro`, `Rongai`).
- `rate_per_litre` (float): Payout rate in KES per litre.

Example:
```csv
farmer_name,zone,rate_per_litre
John Kamau,Njoro,55.0
David Mwangi,Bahati,58.0
Samuel Korir,Rongai,54.0
```

---

## Technical Stack & Requirements

- Python 3.8+
- `pandas` (>= 2.0.0)

To install pandas if not already present:
```bash
pip install pandas
```

---

## How to Run

1. Open your terminal and navigate to the `week_3` directory:
   ```bash
   cd week_3
   ```

2. Run the analysis script:
   ```bash
   python3 dairy_zone_analysis.py
   ```

3. The script will render the formatted executive report to the console and export the summary to `zone_monthly_summary.csv`.

---

## Sample Execution Output

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

Exported client summary table to: 'zone_monthly_summary.csv'
```

---

## Pandas Engineering Highlights

- **Inner Merge (`pd.merge`)**: Combines daily collections with farmer profiles on `farmer_name`, matching transactions with corresponding rates and zones.
- **Vectorized Payout Calculation**: Calculates `payout_kes = litres * rate_per_litre` efficiently without explicit row looping.
- **Multi-level Aggregation (`groupby().agg()`)**: Computes zone-level totals (`total_litres`, `total_payout_kes`, active farmers count).
- **Sub-group Ranking**: Computes individual farmer sums by `['zone', 'farmer_name']`, sorts descending, and isolates the top producer per zone.
