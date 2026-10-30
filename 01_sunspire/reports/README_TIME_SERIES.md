**Time-Series & Complexity Analysis**

- **Extractor**: `tools/time_series_complexity.py` — scans `logs/` for `shell_history.csv`, computes a complexity score per command, and writes:
  - `reports/command_events.jsonl` (per-event JSON lines)
  - `reports/commands_timeseries_hourly.csv` (hourly buckets; columns: `bucket_start,count,avg_complexity`)

- **Plotter**: `tools/plot_commands.py` — reads the CSV and creates `reports/commands_timeseries_plot.png` showing command volume and average complexity over time.

Run (from repo root):
```bash
python3 tools/time_series_complexity.py --logs-dir logs/ --out-dir reports/ --bucket hourly
python3 tools/plot_commands.py --timeseries reports/commands_timeseries_hourly.csv --out reports/commands_timeseries_plot.png
```

Notes:
- The complexity heuristic is a lightweight score (0-10) combining command length, use of pipes/redirects, and presence of common exploit/tool keywords (sqlmap, nmap, hydra, wget, curl, etc.).
- If your environment uses a virtualenv, activate it first. These scripts only use Python stdlib + matplotlib for plotting.
