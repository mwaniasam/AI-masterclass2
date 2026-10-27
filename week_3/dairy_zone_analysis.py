"""Nakuru Dairy Cooperative - Monthly Zone Milk & Payout Analysis.

Merges daily farmer milk collection records with farmer master details,
calculates total volume and financial payout by geographic zone,
identifies top producers per zone, and prints an executive summary table.
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
COLLECTION_FILE = BASE_DIR / "daily_collection.csv"
FARMERS_FILE = BASE_DIR / "farmer_details.csv"
OUTPUT_SUMMARY_FILE = BASE_DIR / "zone_monthly_summary.csv"


def load_data(collection_path=COLLECTION_FILE, farmers_path=FARMERS_FILE):
    """Loads daily collection and farmer details spreadsheets."""
    if not collection_path.exists():
        raise FileNotFoundError(f"Missing required input file: {collection_path}")
    if not farmers_path.exists():
        raise FileNotFoundError(f"Missing required input file: {farmers_path}")

    collection_df = pd.read_csv(collection_path)
    farmers_df = pd.read_csv(farmers_path)
    return collection_df, farmers_df


def process_dairy_summary(collection_df, farmers_df):
    """
    Merges collections with farmer details, calculates payouts,
    and aggregates totals and top performers by zone.
    """
    # 1. Merge datasets on farmer_name using an inner join
    merged = pd.merge(collection_df, farmers_df, on="farmer_name", how="inner")

    # 2. Compute individual delivery payout
    merged["payout_kes"] = merged["litres"] * merged["rate_per_litre"]

    # 3. Aggregate totals per zone
    zone_aggregates = merged.groupby("zone").agg(
        total_litres=("litres", "sum"),
        total_payout_kes=("payout_kes", "sum"),
        active_farmers=("farmer_name", "nunique"),
        collection_count=("litres", "count")
    ).reset_index()

    # 4. Determine top farmer per zone (by cumulative milk volume)
    farmer_totals = (
        merged.groupby(["zone", "farmer_name"])
        .agg(total_litres=("litres", "sum"), total_payout=("payout_kes", "sum"))
        .reset_index()
    )

    # Sort descending by volume and select the highest producer per zone
    top_producers = (
        farmer_totals.sort_values(["zone", "total_litres"], ascending=[True, False])
        .groupby("zone")
        .first()
        .reset_index()
    )

    top_producers["top_farmer"] = (
        top_producers["farmer_name"]
        + " ("
        + top_producers["total_litres"].map(lambda x: f"{x:,.1f} L")
        + ")"
    )

    # 5. Merge zone aggregates with top farmer information
    summary_df = pd.merge(
        zone_aggregates[["zone", "total_litres", "total_payout_kes"]],
        top_producers[["zone", "top_farmer"]],
        on="zone"
    )

    # Sort zones alphabetically
    summary_df = summary_df.sort_values("zone").reset_index(drop=True)

    return merged, summary_df


def print_executive_report(summary_df, merged_df):
    """Prints a clean, formatted executive summary table for client presentation."""
    divider = "=" * 78
    sub_divider = "-" * 78

    total_litres_all = summary_df["total_litres"].sum()
    total_payout_all = summary_df["total_payout_kes"].sum()
    num_farmers = merged_df["farmer_name"].nunique()
    date_min = merged_df["date"].min()
    date_max = merged_df["date"].max()

    print("\n" + divider)
    print("      NAKURU DAIRY CO-OPERATIVE SOCIETY  |  MONTHLY ZONE SUMMARY")
    print(divider)
    print(f"Reporting Period : {date_min} to {date_max}")
    print(f"Active Farmers   : {num_farmers} producers across {len(summary_df)} zones")
    print(f"Total Milk Pool  : {total_litres_all:,.1f} litres")
    print(f"Total Payout     : KES {total_payout_all:,.2f}")
    print(sub_divider)
    print(
        f"{'Zone':<12} | {'Total Litres':>15} | {'Total Payout (KES)':>20} | {'Top Farmer (Volume)':<22}"
    )
    print(sub_divider)

    for _, row in summary_df.iterrows():
        zone_name = str(row["zone"])
        litres_str = f"{row['total_litres']:>15,.1f}"
        payout_str = f"KES {row['total_payout_kes']:>16,.2f}"
        top_str = f"{row['top_farmer']:<22}"
        print(f"{zone_name:<12} | {litres_str} | {payout_str} | {top_str}")

    print(sub_divider)
    print(
        f"{'TOTAL / CO-OP':<12} | {total_litres_all:>15,.1f} | KES {total_payout_all:>16,.2f} | {'--':<22}"
    )
    print(divider + "\n")


def run():
    """Main execution function."""
    collection_df, farmers_df = load_data()
    merged_df, summary_df = process_dairy_summary(collection_df, farmers_df)

    # Print the terminal dashboard
    print_executive_report(summary_df, merged_df)

    # Export clean summary table to CSV for downstream reporting
    summary_df.to_csv(OUTPUT_SUMMARY_FILE, index=False)
    print(f"Exported client summary table to: '{OUTPUT_SUMMARY_FILE.name}'")


if __name__ == "__main__":
    run()
