# Phase II - Track B: Data Analyst - Week 3 - Day 11: Advanced pandas Operations

Course Day: Day 11 of 40  
Track: Track B (Data Analyst)  
Focus: Merges, Joins, Pivots, Apply Functions, and Multi-Aggregation Groupbys  
Project: Nakuru Dairy Co-op Zone Milk and Payout Analysis  

---

## 1. Core Concepts & Techniques

### Step 1: Merging DataFrames (`pd.merge`)
In business analytics, data is routinely normalized across multiple spreadsheets or tables (e.g. daily transactional records in one file, customer/entity profiles in another).

```python
merged = pd.merge(orders, customers, on="customer_id", how="inner")
```

### Step 2: Join Types & Business Use Cases

| Join Type | Records Retained | Typical Business Use Case |
|:---|:---|:---|
| **inner** | Only records that match in both DataFrames | Validating transactions that have corresponding registered profiles |
| **left** | All records from left DataFrame + matches from right | Retaining all daily deliveries even if a farmer profile is unassigned |
| **right** | All records from right DataFrame + matches from left | Identifying all registered farmers who made zero deliveries this month |
| **outer** | All records from both tables (NaN on mismatches) | Complete data reconciliation and anomaly audits |

### Step 3: Reshaping with Pivot Tables (`pd.pivot_table`)
Transforms long-format time series into multi-dimensional matrices for reporting:

```python
pivot = pd.pivot_table(
    sales,
    values="revenue_kes",
    index="county",
    columns="month",
    aggfunc="sum"
)
```

### Step 4: Row-Level Logic with `.apply()`
Applies arbitrary business rules and categorization when built-in vector functions do not suffice:

```python
def classify_sale(amount):
    if amount >= 100000:
        return "Large"
    elif amount >= 50000:
        return "Medium"
    else:
        return "Small"

merged["sale_size"] = merged["amount_kes"].apply(classify_sale)
```

### Step 5: Multi-Metric Aggregations (`groupby().agg()`)
Computes comprehensive statistical summaries in a single vectorized operation:

```python
summary = merged.groupby("county").agg(
    total_revenue=("amount_kes", "sum"),
    order_count=("order_id", "count"),
    avg_order=("amount_kes", "mean"),
    largest_order=("amount_kes", "max")
)
```

---

## 2. Practical Case Study: Nakuru Dairy Co-operative

### The Business Problem
A Nakuru dairy co-operative manager receives two spreadsheets:
1. `daily_collection.csv`: Daily weighbridge drop-offs per farmer (`farmer_name`, `date`, `litres`).
2. `farmer_details.csv`: Farmer profiles, cooperative collection zones, and commercial buying rate per litre (`farmer_name`, `zone`, `rate_per_litre`).

The manager requires a unified monthly executive summary table showing:
- Total litres per zone
- Total financial payout per zone
- Top farmer (highest milk supplier) per zone

### Implementation Pipeline (`dairy_zone_analysis.py`)

1. **Data Ingestion**: Reads both CSV datasets using `pandas.read_csv`.
2. **Inner Join**: Merges collections with farmer master records on `farmer_name`.
3. **Payout Derivation**: Vectorized multiplication `litres * rate_per_litre`.
4. **Zone Aggregations**: Groups by `zone` to sum volume and gross payout.
5. **Sub-group Ranking**: Groups by `['zone', 'farmer_name']` to compute cumulative deliveries, then isolates the top producer per zone.
6. **Executive Presentation**: Renders an aligned ASCII table and exports `zone_monthly_summary.csv`.

---

## 3. Executive Output Table

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
```

### Key Business Insights
- **Highest Volume Zone**: **Rongai** produced the largest volume of milk at `2,002.1 litres` (34.7% of total co-op supply), driven by Samuel Korir who supplied `803.2 litres` individually.
- **Highest Payout Zone**: **Bahati** received the largest total financial payout at `KES 113,656.80` due to its premium rate of `KES 58.00/litre`.
- **Co-op Summary**: 12 active farmers delivered `5,776.7 litres` over the 14-day sample period, representing `KES 321,595.20` in total farmer disbursements.
