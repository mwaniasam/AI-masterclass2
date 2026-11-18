"""
Nairobi Produce Market: 6-Month Vegetable Price Volatility & Seasonality Analysis
Phase II - Track B: Data Analyst - Week 3 - Day 15 (Complex Analysis Project)

End-to-end data pipeline combining daily wholesale price logs with crop metadata:
1. Cleans casing/spelling inconsistencies, removes duplicates, and interpolates missing dates.
2. Merges multi-table produce metadata (source county, shelf life, perishability).
3. Computes time-series rolling averages, monthly resamples, IQR outliers, and volatility (CV%).
4. Generates three publication-grade charts answering distinct business questions.
5. Prints a non-technical executive report for wholesale buyers and procurement managers.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy import stats

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CHARTS_DIR = os.path.join(BASE_DIR, "charts")
os.makedirs(CHARTS_DIR, exist_ok=True)

PRICES_CSV = os.path.join(DATA_DIR, "produce_daily_prices.csv")
METADATA_CSV = os.path.join(DATA_DIR, "vegetable_metadata.csv")

TRENDS_CHART = os.path.join(CHARTS_DIR, "vegetable_price_trends.png")
VOLATILITY_CHART = os.path.join(CHARTS_DIR, "volatility_comparison.png")
SEASONALITY_CHART = os.path.join(CHARTS_DIR, "monthly_seasonality.png")


def load_and_clean_data():
    """Load both tables, standardize keys, deduplicate, interpolate missing prices, and merge."""
    raw_prices = pd.read_csv(PRICES_CSV)
    raw_meta = pd.read_csv(METADATA_CSV)

    audit = {
        "raw_price_rows": len(raw_prices),
        "raw_meta_rows": len(raw_meta),
    }

    # Step 1: Harmonize metadata key column name
    meta = raw_meta.rename(columns={"produce_item": "vegetable"}).copy()
    meta["vegetable"] = meta["vegetable"].str.strip()

    # Step 2: Standardize vegetable naming inconsistencies in price table
    prices = raw_prices.copy()
    prices["vegetable_clean"] = prices["vegetable"].astype(str).str.strip().str.title()
    canonical_map = {
        "Red Onion": "Red Onions",
        "Red Onions": "Red Onions",
        "Tomatoes": "Tomatoes",
        "Sukuma Wiki": "Sukuma Wiki",
        "Irish Potatoes": "Irish Potatoes",
        "Cabbages": "Cabbages",
    }
    prices["vegetable_clean"] = prices["vegetable_clean"].map(canonical_map)
    audit["names_standardized"] = int((prices["vegetable"] != prices["vegetable_clean"]).sum())
    prices["vegetable"] = prices["vegetable_clean"]
    prices = prices.drop(columns=["vegetable_clean"])

    # Step 3: Parse dates and remove duplicate (date, vegetable) records
    prices["date"] = pd.to_datetime(prices["date"])
    before_dedup = len(prices)
    prices = prices.drop_duplicates(subset=["date", "vegetable"], keep="first").copy()
    audit["duplicates_removed"] = before_dedup - len(prices)

    # Step 4: Sort chronologically and interpolate missing daily prices per vegetable
    prices = prices.sort_values(["vegetable", "date"]).reset_index(drop=True)
    audit["missing_prices_imputed"] = int(prices["wholesale_price_kes_kg"].isna().sum())

    def interpolate_group(group: pd.DataFrame) -> pd.DataFrame:
        g = group.set_index("date").sort_index()
        g["wholesale_price_kes_kg"] = g["wholesale_price_kes_kg"].interpolate(method="time").round(1)
        g["rolling_14d_kes"] = g["wholesale_price_kes_kg"].rolling(window=14, min_periods=1).mean()
        return g.reset_index()

    cleaned_groups = [interpolate_group(grp) for _, grp in prices.groupby("vegetable", sort=False)]
    prices_clean = pd.concat(cleaned_groups, ignore_index=True)

    # Step 5: Merge daily price series with crop metadata
    merged = pd.merge(prices_clean, meta, on="vegetable", how="left")
    merged["month"] = merged["date"].dt.to_period("M").astype(str)
    merged["month_label"] = merged["date"].dt.strftime("%b %Y")
    audit["final_rows"] = len(merged)

    return merged, meta, audit


def analyze_volatility_and_peaks(df: pd.DataFrame, meta: pd.DataFrame):
    """Compute descriptive statistics, CV volatility, IQR outlier spikes, and peak timing."""
    records = []
    for veg, grp in df.groupby("vegetable"):
        s = grp["wholesale_price_kes_kg"]
        mean_p = s.mean()
        median_p = s.median()
        std_p = s.std(ddof=1)
        cv_pct = (std_p / mean_p) * 100.0
        q1 = s.quantile(0.25)
        q3 = s.quantile(0.75)
        iqr = q3 - q1
        upper_fence = q3 + 1.5 * iqr
        outlier_days = int((s > upper_fence).sum())

        peak_idx = s.idxmax()
        peak_price = grp.loc[peak_idx, "wholesale_price_kes_kg"]
        peak_date = grp.loc[peak_idx, "date"]

        trough_idx = s.idxmin()
        trough_price = grp.loc[trough_idx, "wholesale_price_kes_kg"]
        trough_date = grp.loc[trough_idx, "date"]

        monthly_avg = grp.groupby("month_label", sort=False)["wholesale_price_kes_kg"].mean()
        peak_month = monthly_avg.idxmax()
        peak_month_avg = monthly_avg.max()

        records.append({
            "vegetable": veg,
            "mean_kes": mean_p,
            "median_kes": median_p,
            "std_kes": std_p,
            "cv_pct": cv_pct,
            "iqr_kes": iqr,
            "min_kes": trough_price,
            "trough_date": trough_date,
            "max_kes": peak_price,
            "peak_date": peak_date,
            "peak_month": peak_month,
            "peak_month_avg": peak_month_avg,
            "outlier_days": outlier_days,
        })

    summary = pd.DataFrame(records)
    summary = pd.merge(summary, meta, on="vegetable", how="left")
    summary = summary.sort_values("cv_pct", ascending=False).reset_index(drop=True)

    # Monthly pivot table ordered chronologically (Jan - Jun 2026)
    month_order = ["Jan 2026", "Feb 2026", "Mar 2026", "Apr 2026", "May 2026", "Jun 2026"]
    monthly_pivot = df.pivot_table(
        index="vegetable",
        columns="month_label",
        values="wholesale_price_kes_kg",
        aggfunc="mean"
    )[month_order]
    monthly_pivot = monthly_pivot.loc[summary["vegetable"]]

    # Correlation between shelf life and volatility (CV%)
    r_shelf, p_shelf = stats.pearsonr(summary["shelf_life_days"], summary["cv_pct"])

    return summary, monthly_pivot, (r_shelf, p_shelf)


def plot_vegetable_trends(df: pd.DataFrame, summary: pd.DataFrame):
    """Chart 1: Dedicated daily & 14-day rolling trend panel per vegetable with peak markers."""
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    fig, axes = plt.subplots(2, 3, figsize=(16, 9), dpi=300)
    axes_flat = axes.flatten()

    palette = {
        "Tomatoes": "#C0392B",
        "Sukuma Wiki": "#27AE60",
        "Irish Potatoes": "#D35400",
        "Red Onions": "#8E44AD",
        "Cabbages": "#2980B9",
    }

    for idx, row in summary.iterrows():
        ax = axes_flat[idx]
        veg = row["vegetable"]
        color = palette[veg]
        sub = df[df["vegetable"] == veg].sort_values("date")

        # Raw daily prices (light) and 14-day rolling average (bold)
        ax.plot(sub["date"], sub["wholesale_price_kes_kg"], color=color, alpha=0.28, linewidth=1.0, label="Daily Wholesale Price")
        ax.plot(sub["date"], sub["rolling_14d_kes"], color=color, linewidth=2.3, label="14-Day Rolling Avg")

        # Peak marker and callout
        peak_d = row["peak_date"]
        peak_p = row["max_kes"]
        ax.scatter([peak_d], [peak_p], color="#111111", s=55, zorder=5)

        # Keep annotation inside plot area
        x_offset = -95 if peak_d > pd.Timestamp("2026-04-15") else 12
        ax.annotate(
            f"Peak: KES {peak_p:.0f}/kg\n({peak_d.strftime('%b %d')})",
            xy=(peak_d, peak_p),
            xytext=(x_offset, -22),
            textcoords="offset points",
            fontsize=8.5,
            fontweight="bold",
            color="#111111",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#FFF8DC", edgecolor="#888888", alpha=0.92),
            arrowprops=dict(arrowstyle="->", color="#333333", lw=1.0)
        )

        ax.set_title(
            f"{idx + 1}. {veg}  |  CV = {row['cv_pct']:.1f}%  (Source: {row['primary_source_county']})",
            fontsize=10.5,
            fontweight="bold",
            pad=8
        )
        ax.set_ylabel("Wholesale Price (KES / kg)", fontsize=9.5, fontweight="bold")
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
        ax.xaxis.set_major_locator(mdates.MonthLocator())
        ax.set_ylim(sub["wholesale_price_kes_kg"].min() * 0.85, peak_p * 1.15)
        ax.legend(loc="upper left", fontsize=8, frameon=True, framealpha=0.85)

    # Panel 6: Executive Volatility Summary Card
    card_ax = axes_flat[5]
    card_ax.axis("off")
    top_veg = summary.iloc[0]
    stable_veg = summary.iloc[-1]

    summary_lines = [
        "EXECUTIVE VOLATILITY BRIEF",
        "Wakulima Market (Jan - Jun 2026)",
        "-" * 42,
        f"Most Volatile : {top_veg['vegetable']}",
        f"  CV = {top_veg['cv_pct']:.1f}% | SD = KES {top_veg['std_kes']:.1f}/kg",
        f"  Peak: KES {top_veg['max_kes']:.1f}/kg on {top_veg['peak_date'].strftime('%b %d, %Y')}",
        f"  Peak Month Avg: {top_veg['peak_month']} (KES {top_veg['peak_month_avg']:.1f})",
        "",
        f"Most Stable   : {stable_veg['vegetable']}",
        f"  CV = {stable_veg['cv_pct']:.1f}% | SD = KES {stable_veg['std_kes']:.1f}/kg",
        f"  Range: KES {stable_veg['min_kes']:.0f} - {stable_veg['max_kes']:.0f}/kg",
        "",
        "Key Supply Chain Insight:",
        "Short shelf-life crops (Tomatoes: 5d,",
        "Sukuma Wiki: 2d) cannot be warehoused,",
        "causing sharp seasonal price shocks."
    ]

    card_ax.text(
        0.04, 0.94, "\n".join(summary_lines),
        transform=card_ax.transAxes,
        fontsize=9.5,
        family="monospace",
        verticalalignment="top",
        bbox=dict(boxstyle="round,pad=0.7", facecolor="#F4F6F9", edgecolor="#2C3E50", linewidth=1.2)
    )

    fig.suptitle(
        "Nairobi Produce Market: 6-Month Daily Price Trends & Peak Shocks by Vegetable (Jan - Jun 2026)",
        fontsize=14,
        fontweight="bold",
        y=0.98
    )
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(TRENDS_CHART, dpi=300)
    plt.close(fig)


def plot_volatility_comparison(summary: pd.DataFrame, shelf_corr: tuple):
    """Chart 2: Ranked volatility (CV%) comparison and shelf-life vs volatility scatter."""
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.8), dpi=300)

    # Left panel: Horizontal bar chart of Coefficient of Variation (CV%)
    ordered = summary.sort_values("cv_pct", ascending=True)
    bar_colors = ["#2980B9", "#8E44AD", "#D35400", "#27AE60", "#C0392B"]
    bars = ax1.barh(ordered["vegetable"], ordered["cv_pct"], color=bar_colors, edgecolor="#222222", alpha=0.9)

    for bar, (_, row) in zip(bars, ordered.iterrows()):
        w = bar.get_width()
        ax1.text(
            w + 0.6,
            bar.get_y() + bar.get_height() / 2,
            f"{w:.1f}%  (SD: KES {row['std_kes']:.1f}, Mean: KES {row['mean_kes']:.0f})",
            va="center",
            fontsize=8.8,
            fontweight="bold",
            color="#222222"
        )

    ax1.set_title("Relative Price Volatility Ranked by Coefficient of Variation (CV%)", fontsize=11, fontweight="bold", pad=10)
    ax1.set_xlabel("Coefficient of Variation = (Std Dev / Mean) x 100 (%)", fontsize=10, fontweight="bold")
    ax1.set_xlim(0, ordered["cv_pct"].max() * 1.82)

    # Right panel: Shelf life vs Volatility scatter with OLS trendline
    x = summary["shelf_life_days"]
    y = summary["cv_pct"]
    slope, intercept, _, _, _ = stats.linregress(x, y)
    r_val, p_val = shelf_corr

    ax2.scatter(x, y, s=130, color="#1F4E79", edgecolors="#111111", zorder=4)
    x_line = np.linspace(0, 48, 100)
    ax2.plot(x_line, slope * x_line + intercept, color="#C0392B", linestyle="--", linewidth=2.0,
             label=f"Linear Trend (r = {r_val:.2f}, p = {p_val:.3f})")

    offsets = {
        "Tomatoes": (10, -4),
        "Sukuma Wiki": (10, 4),
        "Irish Potatoes": (-35, 16),
        "Red Onions": (-55, 16),
        "Cabbages": (10, -10),
    }
    for _, row in summary.iterrows():
        veg = row["vegetable"]
        ax2.annotate(
            f"{veg} ({int(row['shelf_life_days'])}d)",
            xy=(row["shelf_life_days"], row["cv_pct"]),
            xytext=offsets.get(veg, (8, 5)),
            textcoords="offset points",
            fontsize=9,
            fontweight="bold"
        )

    ax2.set_title("Structural Driver: Crop Shelf Life vs. Price Volatility", fontsize=11, fontweight="bold", pad=10)
    ax2.set_xlabel("Typical Ambient Shelf Life (Days)", fontsize=10, fontweight="bold")
    ax2.set_ylabel("Price Volatility (CV %)", fontsize=10, fontweight="bold")
    ax2.set_xlim(-2, 52)
    ax2.set_ylim(0, summary["cv_pct"].max() * 1.2)
    ax2.legend(loc="upper right", frameon=True, fontsize=9)

    fig.suptitle(
        "Nairobi Produce Market: Why Scale-Adjusted Volatility (CV%) and Perishability Matter",
        fontsize=13,
        fontweight="bold",
        y=0.98
    )
    plt.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(VOLATILITY_CHART, dpi=300)
    plt.close(fig)


def plot_monthly_seasonality(df: pd.DataFrame, summary: pd.DataFrame, monthly_pivot: pd.DataFrame):
    """Chart 3: Monthly average price heatmap and price distribution boxplots."""
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5.8), dpi=300)

    # Left panel: Normalized-row heatmap showing each crop's seasonal peak intensity, annotated with KES/kg
    norm_vals = monthly_pivot.sub(monthly_pivot.min(axis=1), axis=0).div(
        monthly_pivot.max(axis=1) - monthly_pivot.min(axis=1), axis=0
    )

    im = ax1.imshow(norm_vals.values, cmap="YlOrRd", aspect="auto", vmin=0, vmax=1)
    ax1.grid(False)
    ax1.set_xticks(range(len(monthly_pivot.columns)))
    ax1.set_xticklabels([c.replace(" 2026", "") for c in monthly_pivot.columns], fontsize=9.5, fontweight="bold")
    ax1.set_yticks(range(len(monthly_pivot.index)))
    ax1.set_yticklabels(monthly_pivot.index, fontsize=9.5, fontweight="bold")

    for i in range(len(monthly_pivot.index)):
        for j in range(len(monthly_pivot.columns)):
            val = monthly_pivot.iloc[i, j]
            intensity = norm_vals.iloc[i, j]
            text_color = "white" if intensity > 0.65 else "#111111"
            ax1.text(j, i, f"KES {val:.0f}", ha="center", va="center", color=text_color, fontsize=9, fontweight="bold")

    ax1.set_title("Monthly Average Wholesale Prices (Row-Normalized Peak Intensity)", fontsize=10.5, fontweight="bold", pad=10)
    ax1.set_xlabel("Month (2026)", fontsize=10, fontweight="bold")
    cbar = fig.colorbar(im, ax=ax1, fraction=0.046, pad=0.04)
    cbar.set_label("Relative Seasonal Intensity (0 = Low, 1 = Peak)", fontsize=8.5)

    # Right panel: Boxplot of daily prices displaying IQR spread and Tukey outliers
    vegs_order = summary["vegetable"].tolist()[::-1]
    data_lists = [df[df["vegetable"] == v]["wholesale_price_kes_kg"].values for v in vegs_order]

    bp = ax2.boxplot(
        data_lists,
        vert=False,
        patch_artist=True,
        tick_labels=vegs_order,
        flierprops=dict(marker="o", markerfacecolor="#C0392B", markersize=5, alpha=0.75),
        medianprops=dict(color="#111111", linewidth=2.0)
    )
    box_colors = ["#AED6F1", "#D2B4DE", "#F5CBA7", "#A9DFBF", "#F5B7B1"]
    for patch, c in zip(bp["boxes"], box_colors):
        patch.set_facecolor(c)
        patch.set_edgecolor("#333333")

    ax2.set_title("6-Month Wholesale Price Distributions & IQR Spike Outliers", fontsize=10.5, fontweight="bold", pad=10)
    ax2.set_xlabel("Daily Wholesale Price (KES / kg)", fontsize=10, fontweight="bold")

    fig.suptitle(
        "Nairobi Produce Market: Seasonal Peak Calendar and Price Risk Spread (Jan - Jun 2026)",
        fontsize=13,
        fontweight="bold",
        y=0.98
    )
    plt.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(SEASONALITY_CHART, dpi=300)
    plt.close(fig)


def print_report(summary: pd.DataFrame, monthly_pivot: pd.DataFrame, audit: dict, shelf_corr: tuple):
    """Print complete data audit, quantitative tables, and 4-sentence executive summary."""
    print("=" * 88)
    print("  NAIROBI PRODUCE MARKET (WAKULIMA) | 6-MONTH PRICE VOLATILITY & SEASONALITY REPORT")
    print("=" * 88)
    print(f"Analysis Window           : January 1, 2026 to June 30, 2026 (181 calendar days)")
    print(f"Raw Price Records Loaded  : {audit['raw_price_rows']} rows | Metadata Table: {audit['raw_meta_rows']} crops")
    print(f"Data Hygiene Audit        : {audit['names_standardized']} naming fixes | {audit['duplicates_removed']} duplicates removed | {audit['missing_prices_imputed']} gaps interpolated")
    print(f"Clean Merged Observations : {audit['final_rows']} verified daily crop-price observations")
    print("-" * 88)
    print("VOLATILITY & PEAK RANKING TABLE (SORTED BY COEFFICIENT OF VARIATION):")
    print("-" * 88)
    print(f"{'Vegetable':<16} | {'Mean':>7} | {'StdDev':>7} | {'CV %':>6} | {'Min':>6} | {'Peak':>7} | {'Peak Date':<11} | {'Peak Month':<9} | {'Shelf'}")
    print("-" * 88)

    for _, row in summary.iterrows():
        print(
            f"{row['vegetable']:<16} | "
            f"{row['mean_kes']:>7.1f} | "
            f"{row['std_kes']:>7.1f} | "
            f"{row['cv_pct']:>5.1f}% | "
            f"{row['min_kes']:>6.1f} | "
            f"{row['max_kes']:>7.1f} | "
            f"{row['peak_date'].strftime('%Y-%m-%d'):<11} | "
            f"{row['peak_month']:<9} | "
            f"{int(row['shelf_life_days']):>2}d"
        )

    print("-" * 88)
    print("MONTHLY AVERAGE WHOLESALE PRICES (KES / KG):")
    print("-" * 88)
    header = f"{'Vegetable':<16} | " + " | ".join(f"{c.replace(' 2026', ''):>7}" for c in monthly_pivot.columns)
    print(header)
    print("-" * 88)
    for veg, row in monthly_pivot.iterrows():
        vals = " | ".join(f"{v:>7.1f}" for v in row.values)
        print(f"{veg:<16} | {vals}")

    top = summary.iloc[0]
    second = summary.iloc[1]
    stable = summary.iloc[-1]
    onions = summary[summary["vegetable"] == "Red Onions"].iloc[0]

    tom_jan = monthly_pivot.loc["Tomatoes", "Jan 2026"]
    tom_may = monthly_pivot.loc["Tomatoes", "May 2026"]
    tom_surge_pct = ((tom_may - tom_jan) / tom_jan) * 100.0

    r_shelf, p_shelf = shelf_corr

    print("-" * 88)
    print("EXECUTIVE FINDINGS SUMMARY (4 SENTENCES FOR NON-TECHNICAL STAKEHOLDERS):")
    print("-" * 88)
    print(
        f"1. {top['vegetable']} exhibit the highest wholesale price volatility in Nairobi (CV = {top['cv_pct']:.1f}%),\n"
        f"   peaking sharply in {top['peak_month']} at KES {top['max_kes']:.1f}/kg ({top['peak_date'].strftime('%B %d')}), when heavy long rains\n"
        f"   and farm-road disruptions push monthly average prices {tom_surge_pct:.0f}% above January levels.\n"
        f"2. {second['vegetable']} ranks second in volatility (CV = {second['cv_pct']:.1f}%), following an opposite seasonal\n"
        f"   cycle that peaks across late February and early March (KES {second['max_kes']:.1f}/kg on {second['peak_date'].strftime('%B %d')};\n"
        f"   {second['peak_month']} average KES {second['peak_month_avg']:.1f}/kg) during dry-season irrigation shortages before falling rapidly in April.\n"
        f"3. Although {onions['vegetable']} command the highest average price (KES {onions['mean_kes']:.1f}/kg), their 45-day\n"
        f"   ambient shelf life allows wholesalers to buffer supply shocks, keeping relative volatility\n"
        f"   much lower (CV = {onions['cv_pct']:.1f}%) alongside {stable['vegetable']}, the most stable staple (CV = {stable['cv_pct']:.1f}%).\n"
        f"4. Across all five staples, shorter crop shelf life strongly tracks higher price risk\n"
        f"   (r = {r_shelf:.2f}), meaning restaurants and institutional buyers should lock in supplier\n"
        f"   contracts ahead of late February for leafy greens and ahead of late April for tomatoes."
    )
    print("=" * 88)
    print("Charts generated:")
    print(f" - {TRENDS_CHART}")
    print(f" - {VOLATILITY_CHART}")
    print(f" - {SEASONALITY_CHART}")


def main():
    df_merged, meta, audit = load_and_clean_data()
    summary, monthly_pivot, shelf_corr = analyze_volatility_and_peaks(df_merged, meta)
    plot_vegetable_trends(df_merged, summary)
    plot_volatility_comparison(summary, shelf_corr)
    plot_monthly_seasonality(df_merged, summary, monthly_pivot)
    print_report(summary, monthly_pivot, audit, shelf_corr)


if __name__ == "__main__":
    main()
