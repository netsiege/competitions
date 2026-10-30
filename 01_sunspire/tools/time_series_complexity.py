#!/usr/bin/env python3
"""Build time-series of command counts and complexity scores from shell_history logs.

Outputs (written to `--out-dir`, default `reports/`):
- `commands_timeseries_hourly.csv` : columns `bucket_start,count,avg_complexity`
- `command_events.jsonl` : per-command JSON lines with fields: timestamp, attacker_ip, command, length, complexity

Usage: python tools/time_series_complexity.py --logs-dir logs/ --out-dir reports/ --bucket hourly
"""
from __future__ import annotations
import csv
import json
import math
import argparse
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import re


def detect_fields(headers: list[str]) -> tuple[str, str]:
    ts_field = None
    cmd_field = None
    for h in headers:
        lh = h.lower()
        if ts_field is None and ("time" in lh or "date" in lh or lh in ("ts", "timestamp")):
            ts_field = h
        if cmd_field is None and ("command" in lh or "cmd" in lh or "history" in lh):
            cmd_field = h
    if ts_field is None:
        # fallback to first column
        ts_field = headers[0]
    if cmd_field is None:
        # fallback to last column
        cmd_field = headers[-1]
    return ts_field, cmd_field


KEYWORD_WEIGHTS = {
    # minimal keyword boost (taught tools shouldn't auto-score high)
    r"\bsqlmap\b": 0.3,
    r"\bhydra\b": 0.3,
    r"\bnmap\b": 0.2,
    r"\bmsfconsole\b": 0.3,
    r"\bevil-winrm\b": 0.3,
    r"\bevil_winrm\b": 0.3,
}


def complexity_score(command: str) -> float:
    """
    Revised complexity scoring emphasizing structural complexity and arguments.
    
    Scoring:
    - Structural operators (pipes, redirects, logical): 0-3.0 points
    - Argument/flag count: 0-2.5 points (0.2 per flag)
    - Command length: 0-1.0 points
    - Keyword boost: 0-1.0 points
    """
    if not command:
        return 0.0
    cmd = command.strip()
    score = 0.0
    
    # 1. Structural complexity (highest weight)
    structural_count = 0
    if "|" in cmd:
        structural_count += 1
    if ">" in cmd or ">>" in cmd:
        structural_count += 1
    if "<" in cmd:
        structural_count += 1
    if "&&" in cmd or ";" in cmd:
        structural_count += 1
    if "||" in cmd:
        structural_count += 1
    # Each structural operator adds up to 0.6, max 3.0
    score += min(structural_count * 0.6, 3.0)
    
    # 2. Argument/flag count (heavy weight)
    # Count tokens starting with '-' or '--'
    tokens = cmd.split()
    flag_count = sum(1 for t in tokens if t.startswith("-") and len(t) > 1)
    # 0.2 per flag, capped at 2.5
    score += min(flag_count * 0.2, 2.5)
    
    # 3. Command length (light weight)
    score += min(len(cmd) / 150.0, 1.0)
    
    # 4. Keyword boost (minimal)
    keyword_boost = 0.0
    for pattern, w in KEYWORD_WEIGHTS.items():
        if re.search(pattern, cmd, flags=re.IGNORECASE):
            keyword_boost += w
    score += min(keyword_boost, 1.0)
    
    # 5. Token count (for complex chaining)
    if len(tokens) > 8:
        score += 0.5
    
    # Normalize to 0-10 range
    score = min(score, 10.0)
    return round(score, 3)


def parse_timestamp(val: str) -> datetime | None:
    if not val:
        return None
    val = val.strip()
    # common formats
    fmts = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%S.%f",
        "%m/%d/%Y %H:%M:%S",
        "%d/%m/%Y %H:%M:%S",
    ]
    for f in fmts:
        try:
            return datetime.strptime(val, f)
        except Exception:
            continue
    # epoch seconds
    try:
        ts = float(val)
        return datetime.utcfromtimestamp(ts)
    except Exception:
        pass
    return None


def bucket_dt(dt: datetime, bucket: str) -> datetime:
    if bucket == "hourly":
        return datetime(dt.year, dt.month, dt.day, dt.hour)
    if bucket == "daily":
        return datetime(dt.year, dt.month, dt.day)
    # default hourly
    return datetime(dt.year, dt.month, dt.day, dt.hour)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--logs-dir", default="logs/", help="Path to logs folder")
    p.add_argument("--out-dir", default="reports/", help="Output folder for CSV/JSON")
    p.add_argument("--bucket", choices=("hourly", "daily"), default="hourly")
    p.add_argument("--end-date", default=None, help="Filter events up to this ISO datetime (e.g., 2026-02-10T23:59:59)")
    args = p.parse_args()
    
    end_dt = None
    if args.end_date:
        end_dt = parse_timestamp(args.end_date)

    logs_dir = Path(args.logs_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    events_out = out_dir / "command_events.jsonl"
    timeseries_csv = out_dir / f"commands_timeseries_{args.bucket}.csv"

    buckets: dict[datetime, list[float]] = defaultdict(list)
    counts: dict[datetime, int] = defaultdict(int)

    total = 0
    with events_out.open("w", encoding="utf-8") as evf:
        # find shell_history.csv files under logs_dir
        for csv_path in logs_dir.rglob("shell_history.csv"):
            try:
                with csv_path.open("r", encoding="utf-8", errors="replace") as fh:
                    reader = csv.reader(fh)
                    headers = next(reader)
                    ts_field, cmd_field = detect_fields(headers)
                    # re-open with DictReader for consistent mapping
                with csv_path.open("r", encoding="utf-8", errors="replace") as fh:
                    dreader = csv.DictReader(fh)
                    for row in dreader:
                        total += 1
                        raw_ts = row.get(ts_field, "")
                        cmd = (row.get(cmd_field) or "").strip()
                        if not cmd:
                            # try last column
                            vals = list(row.values())
                            cmd = vals[-1] if vals else ""
                        dt = parse_timestamp(raw_ts)
                        if dt is None:
                            # try to parse from first column value if different
                            vals = list(row.values())
                            dt = parse_timestamp(vals[0])
                        if dt is None:
                            continue
                        # Filter by end_date if specified
                        if end_dt and dt > end_dt:
                            continue
                        score = complexity_score(cmd)
                        b = bucket_dt(dt, args.bucket)
                        buckets[b].append(score)
                        counts[b] += 1
                        rec = {
                            "timestamp": dt.isoformat(),
                            "command": cmd,
                            "length": len(cmd),
                            "complexity": score,
                            "source_file": str(csv_path),
                        }
                        evf.write(json.dumps(rec, ensure_ascii=False) + "\n")
            except StopIteration:
                continue
            except Exception:
                continue

    # write timeseries CSV
    rows = []
    for b in sorted(counts.keys()):
        avg = round(sum(buckets[b]) / len(buckets[b]), 3) if buckets[b] else 0.0
        rows.append((b.isoformat(), counts[b], avg))

    with timeseries_csv.open("w", encoding="utf-8") as tf:
        tf.write("bucket_start,count,avg_complexity\n")
        for r in rows:
            tf.write(f"{r[0]},{r[1]},{r[2]}\n")

    print(f"Wrote {events_out} and {timeseries_csv} (total events processed: {total})")


if __name__ == "__main__":
    main()
