#!/usr/bin/env python3
"""Example plotting script for command counts and complexity over time.

Reads `reports/commands_timeseries_hourly.csv` (created by `time_series_complexity.py`) and
generates `reports/commands_timeseries_plot.png` showing counts and average complexity.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import matplotlib.pyplot as plt
import csv


def read_timeseries(path: Path):
    buckets = []
    counts = []
    avgs = []
    with path.open("r", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for r in reader:
            buckets.append(r["bucket_start"])
            counts.append(int(r["count"]))
            avgs.append(float(r["avg_complexity"]))
    return buckets, counts, avgs


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--timeseries", default="reports/commands_timeseries_hourly.csv")
    p.add_argument("--out", default="reports/commands_timeseries_plot.png")
    args = p.parse_args()

    ts_path = Path(args.timeseries)
    out_path = Path(args.out)

    buckets, counts, avgs = read_timeseries(ts_path)

    fig, ax1 = plt.subplots(figsize=(12, 5))
    ax1.plot(buckets, counts, color="tab:blue", label="command count")
    ax1.set_ylabel("Command Count", color="tab:blue")
    ax1.tick_params(axis="y", labelcolor="tab:blue")
    ax1.tick_params(axis="x", rotation=45)

    ax2 = ax1.twinx()
    ax2.plot(buckets, avgs, color="tab:red", label="avg complexity")
    ax2.set_ylabel("Avg Complexity", color="tab:red")
    ax2.tick_params(axis="y", labelcolor="tab:red")

    plt.title("Commands Over Time — Count and Average Complexity")
    fig.tight_layout()
    fig.savefig(out_path)
    print(f"Saved plot to {out_path}")


if __name__ == "__main__":
    main()
