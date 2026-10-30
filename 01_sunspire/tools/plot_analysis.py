#!/usr/bin/env python3
"""Generate detailed time-series and complexity analysis visualizations.

Outputs (to reports/):
- commands_complexity_trend.png    : complexity over time with trend line
- commands_volume_trend.png         : command volume over time
- commands_complexity_distribution.png : histogram of complexity levels
- commands_phase_analysis.png       : box plot by attack phase
"""
from __future__ import annotations
import csv
import json
from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy import stats
import numpy as np


def read_timeseries(path: Path):
    """Read hourly CSV, return lists of datetime, count, avg_complexity."""
    buckets = []
    counts = []
    avgs = []
    with path.open("r", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for r in reader:
            buckets.append(datetime.fromisoformat(r["bucket_start"]))
            counts.append(int(r["count"]))
            avgs.append(float(r["avg_complexity"]))
    return buckets, counts, avgs


def read_events(path: Path):
    """Read JSONL, return list of complexity scores."""
    complexities = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            event = json.loads(line)
            complexities.append(event["complexity"])
    return complexities


def get_phases():
    """Define attack phases with date ranges and labels."""
    return [
        ("Early Recon", datetime(2026, 1, 8), datetime(2026, 1, 12, 23, 59)),
        ("Escalation", datetime(2026, 1, 12), datetime(2026, 1, 13, 23, 59)),
        ("Recon Window", datetime(2026, 1, 14), datetime(2026, 1, 19, 23, 59)),
        ("Active Exploitation", datetime(2026, 1, 20), datetime(2026, 1, 27, 23, 59)),
        ("Advanced Targeting", datetime(2026, 2, 2), datetime(2026, 2, 10, 23, 59)),
    ]


def plot_complexity_trend(buckets, avgs, out_path):
    """Plot complexity over time with linear trend line."""
    fig, ax = plt.subplots(figsize=(14, 6))

    # Plot line
    ax.plot(buckets, avgs, marker="o", linestyle="-", color="tab:red", linewidth=2, markersize=5, label="Avg Complexity")

    # Add trend line
    x_numeric = mdates.date2num(buckets)
    z = np.polyfit(x_numeric, avgs, 1)
    p = np.poly1d(z)
    trend = p(x_numeric)
    ax.plot(buckets, trend, linestyle="--", color="darkred", linewidth=2, label="Trend Line")

    ax.set_xlabel("Time", fontsize=11, fontweight="bold")
    ax.set_ylabel("Average Complexity", fontsize=11, fontweight="bold")
    ax.set_title("Command Complexity Trend Over Time", fontsize=13, fontweight="bold")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
    plt.xticks(rotation=45, ha="right")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=10)
    fig.tight_layout()
    fig.savefig(out_path, dpi=100)
    print(f"Saved complexity trend to {out_path}")


def plot_volume_trend(buckets, counts, out_path):
    """Plot command volume over time."""
    fig, ax = plt.subplots(figsize=(14, 6))

    ax.bar(buckets, counts, width=0.03, color="steelblue", alpha=0.7, edgecolor="navy", linewidth=1)
    ax.plot(buckets, counts, color="darkblue", linewidth=2, alpha=0.5, label="Volume Trend")

    # Peak annotation
    max_idx = counts.index(max(counts))
    peak_time = buckets[max_idx]
    peak_count = counts[max_idx]
    ax.annotate(f"Peak: {peak_count} commands\n{peak_time.strftime('%Jan %d %H:%M')}", 
                xy=(peak_time, peak_count), xytext=(peak_time, peak_count + 80),
                arrowprops=dict(arrowstyle="->", color="red", lw=1.5),
                fontsize=10, fontweight="bold", color="red", ha="center")

    ax.set_xlabel("Time", fontsize=11, fontweight="bold")
    ax.set_ylabel("Commands per Hour", fontsize=11, fontweight="bold")
    ax.set_title("Command Volume Over Time\n(Shows operational intensity)", fontsize=13, fontweight="bold")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
    plt.xticks(rotation=45, ha="right")
    ax.grid(True, alpha=0.3, axis="y")
    ax.legend(loc="upper right", fontsize=10)
    fig.tight_layout()
    fig.savefig(out_path, dpi=100)
    print(f"Saved volume trend to {out_path}")


def plot_distribution(complexities, out_path):
    """Plot histogram of complexity scores."""
    fig, ax = plt.subplots(figsize=(12, 6))

    bins = np.arange(0, 8, 0.25)
    counts, edges, patches = ax.hist(complexities, bins=bins, color="steelblue", edgecolor="navy", alpha=0.7)

    # Color code by range
    colors_map = {
        "Very Low (0-1)": "#90ee90",
        "Low (1-2)": "#ffff99",
        "Medium (2-3)": "#ffb366",
        "High (3-5)": "#ff9999",
        "Very High (5+)": "#ff4444",
    }
    for i, patch in enumerate(patches):
        if edges[i] < 1:
            patch.set_facecolor("#90ee90")
        elif edges[i] < 2:
            patch.set_facecolor("#ffff99")
        elif edges[i] < 3:
            patch.set_facecolor("#ffb366")
        elif edges[i] < 5:
            patch.set_facecolor("#ff9999")
        else:
            patch.set_facecolor("#ff4444")

    ax.set_xlabel("Complexity Score", fontsize=11, fontweight="bold")
    ax.set_ylabel("Count", fontsize=11, fontweight="bold")
    ax.set_title("Distribution of Command Complexity Scores\n(3,841 total commands)", fontsize=13, fontweight="bold")
    ax.grid(True, alpha=0.3, axis="y")

    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor="#90ee90", edgecolor="black", label="Very Low (0–1.0): 2,653 (69.1%)"),
        Patch(facecolor="#ffff99", edgecolor="black", label="Low (1.0–2.0): 465 (12.1%)"),
        Patch(facecolor="#ffb366", edgecolor="black", label="Medium (2.0–3.0): 337 (8.8%)"),
        Patch(facecolor="#ff9999", edgecolor="black", label="High (3.0–5.0): 326 (8.5%)"),
        Patch(facecolor="#ff4444", edgecolor="black", label="Very High (5.0+): 60 (1.6%)"),
    ]
    ax.legend(handles=legend_elements, loc="upper right", fontsize=10)
    fig.tight_layout()
    fig.savefig(out_path, dpi=100)
    print(f"Saved distribution to {out_path}")


def plot_phase_boxplot(buckets, avgs, out_path):
    """Plot boxplot of complexity by attack phase."""
    phases = get_phases()
    phase_data = {}

    for phase_name, start, end in phases:
        phase_data[phase_name] = []
        for i, bucket in enumerate(buckets):
            if start <= bucket <= end:
                phase_data[phase_name].append(avgs[i])

    fig, ax = plt.subplots(figsize=(12, 6))

    # Prepare data for boxplot
    phase_names = list(phase_data.keys())
    data_to_plot = [phase_data[p] for p in phase_names]

    bp = ax.boxplot(data_to_plot, labels=phase_names, patch_artist=True, notch=False)

    # Color boxes
    colors = ["#ffffcc", "#ffcccc", "#ffffcc", "#ff9999", "#cc99ff"]
    for patch, color in zip(bp["boxes"], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    ax.set_ylabel("Average Hourly Complexity", fontsize=11, fontweight="bold")
    ax.set_title("Command Complexity by Attack Phase\n(Shows progression from recon to targeted exploitation)", fontsize=13, fontweight="bold")
    ax.grid(True, alpha=0.3, axis="y")
    plt.xticks(rotation=15, ha="right")
    fig.tight_layout()
    fig.savefig(out_path, dpi=100)
    print(f"Saved phase analysis to {out_path}")


def main():
    out_dir = Path("reports")
    ts_path = out_dir / "commands_timeseries_hourly.csv"
    events_path = out_dir / "command_events.jsonl"

    print("Reading data...")
    buckets, counts, avgs = read_timeseries(ts_path)
    complexities = read_events(events_path)

    print("Generating visualizations...")
    plot_complexity_trend(buckets, avgs, out_dir / "commands_complexity_trend.png")
    plot_volume_trend(buckets, counts, out_dir / "commands_volume_trend.png")
    plot_distribution(complexities, out_dir / "commands_complexity_distribution.png")
    plot_phase_boxplot(buckets, avgs, out_dir / "commands_phase_analysis.png")

    print("\nAll plots generated successfully!")


if __name__ == "__main__":
    main()
