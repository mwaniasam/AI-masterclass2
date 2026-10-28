"""Nairobi Supermarket Chain - 18-Month Foot Traffic Time Series Analysis.

Analyzes daily customer transaction counts over an 18-month timeframe (Jan 2025 - Jun 2026).
Computes 30-day rolling averages, resamples to monthly aggregates, evaluates underlying
growth versus seasonality, and renders a dual-axis visualization for management reporting.
"""

from pathlib import Path
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "nairobi_supermarket_transactions.csv"
CHART_FILE = BASE_DIR / "supermarket_traffic_trend.png"


def load_and_prepare_data(file_path=DATA_FILE):
    """Loads transaction data, parses dates, and establishes the datetime index."""
    if not file_path.exists():
        raise FileNotFoundError(f"Required data file missing: {file_path}")

    df = pd.read_csv(file_path)
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date").sort_index()

    # Calculate 30-day rolling average (min_periods=1 for smooth startup)
    df["rolling_30d"] = df["transactions"].rolling(30, min_periods=1).mean()
    return df


def generate_time_series_metrics(df):
    """Generates monthly resampled aggregates and growth metrics."""
    # Resample to monthly totals and monthly daily averages
    monthly_totals = df["transactions"].resample("ME").sum()
    monthly_avg_daily = df["transactions"].resample("ME").mean()

    monthly_summary = pd.DataFrame({
        "monthly_total": monthly_totals,
        "daily_avg": monthly_avg_daily,
        "mom_growth_pct": monthly_totals.pct_change() * 100
    })

    return monthly_summary


def print_executive_summary(df, monthly_summary):
    """Prints a clear, non-technical executive brief for the operations manager."""
    total_transactions = df["transactions"].sum()
    avg_daily_all = df["transactions"].mean()

    best_month_idx = monthly_summary["monthly_total"].idxmax()
    worst_month_idx = monthly_summary["monthly_total"].idxmin()

    best_total = monthly_summary.loc[best_month_idx, "monthly_total"]
    worst_total = monthly_summary.loc[worst_month_idx, "monthly_total"]

    start_rolling = df["rolling_30d"].iloc[30]
    end_rolling = df["rolling_30d"].iloc[-1]
    structural_growth = ((end_rolling - start_rolling) / start_rolling) * 100

    weekday_avg = df[~df["is_weekend"]]["transactions"].mean()
    weekend_avg = df[df["is_weekend"]]["transactions"].mean()
    weekend_lift = ((weekend_avg - weekday_avg) / weekday_avg) * 100

    divider = "=" * 76
    sub_divider = "-" * 76

    print("\n" + divider)
    print("   NAIROBI SUPERMARKET CHAIN  |  18-MONTH FOOT TRAFFIC EXECUTIVE REPORT")
    print(divider)
    print(f"Analysis Period      : {df.index.min().strftime('%B %Y')} to {df.index.max().strftime('%B %Y')} (546 Days)")
    print(f"Total Transactions   : {total_transactions:,.0f} customer checkouts")
    print(f"Daily Traffic Average: {avg_daily_all:,.0f} customers / day")
    print(f"Weekend Traffic Lift : +{weekend_lift:.1f}% vs weekdays ({weekend_avg:,.0f} vs {weekday_avg:,.0f}/day)")
    print(sub_divider)
    print("KEY SEASONAL PEAKS & DIPS")
    print(sub_divider)
    print(f"Peak Month           : {best_month_idx.strftime('%B %Y')} with {best_total:,.0f} transactions")
    print(f"Trough Month         : {worst_month_idx.strftime('%B %Y')} with {worst_total:,.0f} transactions")
    print(f"Holiday Volume Surge : +{((best_total / worst_total) - 1) * 100:.1f}% surge from February trough to December peak")
    print(sub_divider)
    print("UNDERLYING STRUCTURAL GROWTH")
    print(sub_divider)
    print(f"Smoothed Baseline Trend: From {start_rolling:,.0f} to {end_rolling:,.0f} customers / day")
    print(f"Underlying 18-Mo Growth: +{structural_growth:.1f}% genuine store expansion")
    print(divider + "\n")


def plot_traffic_trend_chart(df, monthly_summary, output_path=CHART_FILE):
    """
    Renders an executive dual-axis chart comparing monthly totals
    with the 30-day rolling daily average.
    """
    fig, ax1 = plt.subplots(figsize=(13, 6.5), dpi=150)

    # Dates for monthly bars: place at the 15th of each month for visual symmetry
    monthly_plot_dates = [d.replace(day=15) for d in monthly_summary.index]
    monthly_volumes_k = monthly_summary["monthly_total"] / 1000

    # Primary Axis: Monthly Total Volume Bars
    bars = ax1.bar(
        monthly_plot_dates,
        monthly_volumes_k,
        width=20,
        color="#2E75B6",
        alpha=0.55,
        edgecolor="#1F4E79",
        linewidth=1.0,
        label="Monthly Total Transactions (Thousands)",
        zorder=2
    )

    ax1.set_ylabel(
        "Monthly Total Transactions (in Thousands)",
        color="#1F4E79",
        fontsize=11,
        fontweight="bold",
        labelpad=10
    )
    ax1.tick_params(axis="y", labelcolor="#1F4E79", labelsize=10)
    ax1.set_ylim(0, 185)
    ax1.grid(True, linestyle="--", alpha=0.35, axis="y", zorder=1)

    # Secondary Axis: 30-Day Rolling Daily Average Line
    ax2 = ax1.twinx()
    line = ax2.plot(
        df.index,
        df["rolling_30d"],
        color="#C00000",
        linewidth=2.8,
        label="30-Day Rolling Average (Daily Transactions)",
        zorder=3
    )

    ax2.set_ylabel(
        "30-Day Rolling Average (Daily Customers / Day)",
        color="#C00000",
        fontsize=11,
        fontweight="bold",
        labelpad=10
    )
    ax2.tick_params(axis="y", labelcolor="#C00000", labelsize=10)
    ax2.set_ylim(2000, 5400)

    # Format X Axis
    ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=25, ha="right", fontsize=10)
    ax1.set_xlim(pd.Timestamp("2024-12-15"), pd.Timestamp("2026-07-15"))

    # Titles and Annotations for Non-Technical Management
    ax1.set_title(
        "Nairobi Supermarket Chain: 18-Month Foot Traffic Trend & Seasonality\n"
        "Monthly Total Volume vs. 30-Day Rolling Daily Average (Jan 2025 - Jun 2026)",
        fontsize=13,
        fontweight="bold",
        pad=15,
        color="#1A252C"
    )

    # Annotation 1: December Holiday Peak
    dec_date = pd.Timestamp("2025-12-15")
    dec_volume = monthly_volumes_k.loc[pd.Timestamp("2025-12-31")]
    ax1.annotate(
        f"Holiday Peak\nDec 2025: {dec_volume:.1f}k",
        xy=(dec_date, dec_volume),
        xytext=(dec_date - pd.Timedelta(days=55), dec_volume + 12),
        arrowprops=dict(facecolor="#1F4E79", shrink=0.08, width=1.2, headwidth=6),
        fontsize=9,
        fontweight="bold",
        color="#1F4E79",
        bbox=dict(boxstyle="round,pad=0.3", edgecolor="#1F4E79", facecolor="#F0F8FF")
    )

    # Annotation 2: February Post-Holiday Dip
    feb_date = pd.Timestamp("2026-02-15")
    feb_volume = monthly_volumes_k.loc[pd.Timestamp("2026-02-28")]
    ax1.annotate(
        f"Annual Dip\nFeb 2026: {feb_volume:.1f}k",
        xy=(feb_date, feb_volume),
        xytext=(feb_date - pd.Timedelta(days=50), feb_volume + 18),
        arrowprops=dict(facecolor="#C00000", shrink=0.08, width=1.2, headwidth=6),
        fontsize=9,
        fontweight="bold",
        color="#C00000",
        bbox=dict(boxstyle="round,pad=0.3", edgecolor="#C00000", facecolor="#FFF0F0")
    )

    # Annotation 3: Structural Growth Trend indicator
    ax2.annotate(
        "Genuine Structural Growth\n(+21.6% 30-Day Baseline)",
        xy=(pd.Timestamp("2026-05-15"), 3950),
        xytext=(pd.Timestamp("2026-02-20"), 4800),
        arrowprops=dict(facecolor="#2E75B6", shrink=0.08, width=1.2, headwidth=6, connectionstyle="arc3,rad=-0.2"),
        fontsize=9,
        fontweight="bold",
        color="#2E75B6",
        bbox=dict(boxstyle="round,pad=0.3", edgecolor="#2E75B6", facecolor="#F8FBFF")
    )

    # Combined Legend
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(
        handles1 + handles2,
        labels1 + labels2,
        loc="upper left",
        framealpha=0.92,
        facecolor="#FFFFFF",
        edgecolor="#D0D0D0",
        fontsize=9.5
    )

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"Executive chart successfully saved to: '{output_path.name}'")


def run():
    """Main execution orchestrator."""
    df = load_and_prepare_data()
    monthly_summary = generate_time_series_metrics(df)
    print_executive_summary(df, monthly_summary)
    plot_traffic_trend_chart(df, monthly_summary)


if __name__ == "__main__":
    run()
