#!/usr/bin/env python3
"""
Aggregate Shell History Logs from Sunspire Competition

This script consolidates shell_history.csv files from 12 IPs (3 teams × 4 players each)
into multiple structured datasets for analysis and visualization.

Teams:
- Canopy: 10.100.7.11-14 (Players C1-C4)
- Harmony: 10.100.7.21-24 (Players H1-H4)
- Steel: 10.100.7.31-34 (Players T1-T4)
"""

import os
import re
import csv
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter
import pandas as pd
from typing import Dict, List, Tuple, Optional


# ============================================================================
# CONFIGURATION
# ============================================================================

# IP to Team/Player Mapping
IP_MAPPING = {
    "10.100.7.11": ("Canopy", "C1"),
    "10.100.7.12": ("Canopy", "C2"),
    "10.100.7.13": ("Canopy", "C3"),
    "10.100.7.14": ("Canopy", "C4"),
    "10.100.7.21": ("Harmony", "H1"),
    "10.100.7.22": ("Harmony", "H2"),
    "10.100.7.23": ("Harmony", "H3"),
    "10.100.7.24": ("Harmony", "H4"),
    "10.100.7.31": ("Steel", "T1"),
    "10.100.7.32": ("Steel", "T2"),
    "10.100.7.33": ("Steel", "T3"),
    "10.100.7.34": ("Steel", "T4"),
}

# Teaching Milestones (from competition schedule)
TEACHING_MILESTONES = [
    ("2026-01-05", "Introduction to Netsiege"),
    ("2026-01-06", "Operating System Fundamentals"),
    ("2026-01-12", "Network Enumeration and Basic Attacks"),
    ("2026-01-13", "File Shares"),
    ("2026-01-20", "Basic Privilege Escalation"),
    ("2026-01-26", "Web 1"),
    ("2026-02-02", "Defense"),
    ("2026-02-03", "Review and Compete"),
    ("2026-02-10", "Web 2"),
]

INPUT_DIR = Path("/Users/akshay/Documents/GitHub/competitions/01_sunspire/logs")
OUTPUT_DIR = Path("/Users/akshay/Documents/GitHub/competitions/01_sunspire/aggregated_data")


# ============================================================================
# COMMAND PARSING
# ============================================================================

def parse_command(cmd_str: str) -> Tuple[str, str]:
    """
    Parse command string into base command and command with flags.
    
    Examples:
        "nmap -sV -p 1-65535 10.100.7.40" -> ("nmap", "nmap -sV -p 1-65535")
        "gobuster dir -u 10.100.7.40 -w /path/to/wordlist" -> ("gobuster", "gobuster dir")
        "tldr smb" -> ("tldr", "tldr")
        "sudo bash" -> ("bash", "sudo bash")
        "ssh -l root 10.100.7.40" -> ("ssh", "ssh -l root")
    
    Args:
        cmd_str: Raw command string
        
    Returns:
        Tuple of (base_command, command_with_flags)
    """
    cmd_str = cmd_str.strip()
    if not cmd_str:
        return ("", "")
    
    # Split on whitespace and pipes/redirects
    tokens = re.split(r'\s+', cmd_str)
    
    # Remove empty tokens
    tokens = [t for t in tokens if t]
    
    if not tokens:
        return ("", "")
    
    # Skip sudo, bash, sh, etc. prefix
    idx = 0
    while idx < len(tokens) and tokens[idx] in ['sudo', 'bash', 'sh', 'zsh']:
        idx += 1
    
    if idx >= len(tokens):
        return (tokens[0], cmd_str)
    
    # Base command is the first non-prefix token
    base_cmd = tokens[idx]
    
    # Determine how many tokens to include for "command with flags"
    # Rule: include base command + flags (starting with - or --), up to first non-flag arg
    cmd_with_flags_tokens = [base_cmd]
    
    i = idx + 1
    while i < len(tokens):
        token = tokens[i]
        
        # Stop if we hit a pipe, redirect, or semicolon
        if token in ['|', '||', '&&', ';', '>', '>>', '<', '2>', '&']:
            break
        
        # Include flags
        if token.startswith('-'):
            # For flags like -w /path, include the next token only if it's not a path/IP
            cmd_with_flags_tokens.append(token)
            # Check if next token looks like a value for this flag (not another flag, not a path)
            if i + 1 < len(tokens) and not tokens[i + 1].startswith('-'):
                # Heuristic: if it's a short value or looks like a parameter, include it
                next_tok = tokens[i + 1]
                if len(next_tok) < 50 and not ('/' in next_tok or '.' in next_tok):
                    cmd_with_flags_tokens.append(next_tok)
                    i += 1
                elif token in ['-l', '-u', '-w', '-P', '-p']:
                    # These flags commonly have arguments; include them
                    cmd_with_flags_tokens.append(next_tok)
                    i += 1
            break  # Only include flags immediately after base command
        
        # Stop at first positional argument (IP, hostname, path, etc.)
        if re.match(r'^\d+\.\d+\.\d+\.\d+', token) or '/' in token or token[0].isdigit():
            break
        
        # For compound commands like "gobuster dir", include the next token if it's not a flag
        if not token.startswith('-') and i == idx + 1:
            cmd_with_flags_tokens.append(token)
        else:
            break
        
        i += 1
    
    command_with_flags = ' '.join(cmd_with_flags_tokens)
    
    return (base_cmd, command_with_flags)


# ============================================================================
# DATA LOADING AND PROCESSING
# ============================================================================

def load_all_shell_histories() -> List[Dict]:
    """
    Load all shell_history.csv files and enrich with team/player info.
    
    Returns:
        List of dictionaries with columns:
        - timestamp, working_directory, command (from CSV)
        - ip, team, player_id, command_base, command_with_flags, timestamp_dt (added)
    """
    all_records = []
    
    for ip, (team, player_id) in IP_MAPPING.items():
        csv_path = INPUT_DIR / ip / "shell_history.csv"
        
        if not csv_path.exists():
            print(f"Warning: {csv_path} not found")
            continue
        
        print(f"Loading {csv_path}...")
        
        try:
            with open(csv_path, 'r', encoding='utf-8', errors='ignore') as f:
                # CSV format: timestamp,working_directory,command
                reader = csv.reader(f)
                for row in reader:
                    if len(row) < 3:
                        continue
                    
                    try:
                        timestamp_str = row[0].strip()
                        working_dir = row[1].strip()
                        command_str = row[2].strip()
                        
                        # Parse timestamp
                        try:
                            timestamp_dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                        except ValueError:
                            continue  # Skip rows with unparseable timestamps
                        
                        # Parse command
                        cmd_base, cmd_with_flags = parse_command(command_str)
                        
                        record = {
                            'timestamp': timestamp_str,
                            'working_directory': working_dir,
                            'command': command_str,
                            'ip': ip,
                            'team': team,
                            'player_id': player_id,
                            'command_base': cmd_base,
                            'command_with_flags': cmd_with_flags,
                            'timestamp_dt': timestamp_dt,
                        }
                        
                        all_records.append(record)
                    
                    except Exception as e:
                        print(f"Error parsing row in {ip}: {e}")
                        continue
        
        except Exception as e:
            print(f"Error reading {csv_path}: {e}")
            continue
    
    print(f"Loaded {len(all_records)} total records\n")
    return all_records


# ============================================================================
# OUTPUT GENERATION
# ============================================================================

def generate_master_command_log(records: List[Dict]) -> pd.DataFrame:
    """Generate master command log with all enriched records."""
    df = pd.DataFrame(records)
    df = df.sort_values('timestamp_dt').reset_index(drop=True)
    
    # Select and reorder columns
    output_cols = [
        'timestamp', 'team', 'player_id', 'ip', 'working_directory',
        'command_base', 'command_with_flags', 'command'
    ]
    
    return df[output_cols]


def generate_command_frequency_table(records: List[Dict]) -> pd.DataFrame:
    """Generate frequency table of commands with first/last seen and teams/players."""
    freq_data = defaultdict(lambda: {
        'count': 0,
        'first_seen': None,
        'last_seen': None,
        'teams': set(),
        'players': set(),
        'ips': set(),
    })
    
    for record in records:
        cmd = record['command_with_flags']
        freq_data[cmd]['count'] += 1
        freq_data[cmd]['teams'].add(record['team'])
        freq_data[cmd]['players'].add(record['player_id'])
        freq_data[cmd]['ips'].add(record['ip'])
        
        ts = record['timestamp_dt']
        if freq_data[cmd]['first_seen'] is None or ts < freq_data[cmd]['first_seen']:
            freq_data[cmd]['first_seen'] = ts
        if freq_data[cmd]['last_seen'] is None or ts > freq_data[cmd]['last_seen']:
            freq_data[cmd]['last_seen'] = ts
    
    rows = []
    for cmd, data in freq_data.items():
        rows.append({
            'command': cmd,
            'count': data['count'],
            'first_seen': data['first_seen'].strftime("%Y-%m-%d %H:%M:%S"),
            'last_seen': data['last_seen'].strftime("%Y-%m-%d %H:%M:%S"),
            'teams_involved': ', '.join(sorted(data['teams'])),
            'players_involved': ', '.join(sorted(data['players'])),
            'ips_involved': ', '.join(sorted(data['ips'])),
        })
    
    df = pd.DataFrame(rows).sort_values('count', ascending=False).reset_index(drop=True)
    return df


def generate_daily_aggregation(records: List[Dict]) -> pd.DataFrame:
    """Generate daily activity aggregation by team/player."""
    daily_data = defaultdict(lambda: {
        'total_commands': 0,
        'unique_commands': set(),
        'commands': [],
    })
    
    for record in records:
        date = record['timestamp_dt'].strftime("%Y-%m-%d")
        team = record['team']
        player = record['player_id']
        ip = record['ip']
        key = (date, team, player, ip)
        
        daily_data[key]['total_commands'] += 1
        daily_data[key]['unique_commands'].add(record['command_with_flags'])
        daily_data[key]['commands'].append(record['command_with_flags'])
    
    rows = []
    for (date, team, player, ip), data in daily_data.items():
        rows.append({
            'date': date,
            'team': team,
            'player_id': player,
            'ip': ip,
            'total_commands': data['total_commands'],
            'unique_commands': len(data['unique_commands']),
            'unique_command_list': '; '.join(sorted(data['unique_commands'])),
        })
    
    df = pd.DataFrame(rows).sort_values(['date', 'team', 'player_id']).reset_index(drop=True)
    return df


def generate_research_flag_tracker(records: List[Dict]) -> pd.DataFrame:
    """Track usage of tldr, man, help flags (both standalone and as arguments)."""
    research_records = []
    
    for record in records:
        cmd_base = record['command_base']
        cmd_full = record['command']
        
        # Check for standalone research commands
        if cmd_base in ['tldr', 'man', 'help']:
            research_records.append({
                'timestamp': record['timestamp'],
                'team': record['team'],
                'player_id': record['player_id'],
                'ip': record['ip'],
                'flag_type': cmd_base,
                'command': record['command_with_flags'],
                'full_command': cmd_full,
            })
        
        # Check for --help or -h flags
        if '--help' in cmd_full or ' -h' in cmd_full or cmd_full.endswith(' -h'):
            research_records.append({
                'timestamp': record['timestamp'],
                'team': record['team'],
                'player_id': record['player_id'],
                'ip': record['ip'],
                'flag_type': '--help flag',
                'command': record['command_with_flags'],
                'full_command': cmd_full,
            })
    
    df = pd.DataFrame(research_records).sort_values('timestamp').reset_index(drop=True)
    return df


def generate_weekly_aggregation(records: List[Dict]) -> pd.DataFrame:
    """Generate weekly team-level aggregation with top commands."""
    weekly_data = defaultdict(lambda: {
        'total_commands': 0,
        'unique_commands': set(),
        'command_freq': Counter(),
    })
    
    for record in records:
        # Get week starting Sunday
        ts = record['timestamp_dt']
        week_start = ts - pd.Timedelta(days=ts.weekday())
        week_str = week_start.strftime("%Y-W%V (%Y-%m-%d)")
        
        team = record['team']
        key = (week_str, team)
        
        weekly_data[key]['total_commands'] += 1
        weekly_data[key]['unique_commands'].add(record['command_with_flags'])
        weekly_data[key]['command_freq'][record['command_with_flags']] += 1
    
    rows = []
    for (week_str, team), data in weekly_data.items():
        # Get top 5 commands
        top_5 = data['command_freq'].most_common(5)
        top_5_str = '; '.join([f"{cmd} ({count})" for cmd, count in top_5])
        
        rows.append({
            'week': week_str,
            'team': team,
            'total_commands': data['total_commands'],
            'unique_commands': len(data['unique_commands']),
            'top_5_commands': top_5_str,
        })
    
    df = pd.DataFrame(rows).sort_values(['week', 'team']).reset_index(drop=True)
    return df


def generate_teaching_milestones() -> pd.DataFrame:
    """Generate teaching milestones reference table."""
    rows = []
    for date_str, topic in TEACHING_MILESTONES:
        rows.append({
            'date': date_str,
            'topic': topic,
            'milestone_type': 'teaching_start',
        })
    
    return pd.DataFrame(rows)


# ============================================================================
# MAIN
# ============================================================================

def main():
    """Main execution."""
    print("=" * 80)
    print("SHELL HISTORY AGGREGATION - SUNSPIRE COMPETITION")
    print("=" * 80)
    print()
    
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}\n")
    
    # Load data
    print("STEP 1: Loading and parsing shell history files...")
    print("-" * 80)
    records = load_all_shell_histories()
    
    if not records:
        print("ERROR: No records loaded. Exiting.")
        return
    
    print(f"✓ Loaded and parsed {len(records)} command records\n")
    
    # Generate outputs
    print("STEP 2: Generating output datasets...")
    print("-" * 80)
    
    outputs = {
        'master_command_log.csv': generate_master_command_log(records),
        'command_frequency.csv': generate_command_frequency_table(records),
        'daily_aggregation.csv': generate_daily_aggregation(records),
        'research_flag_tracker.csv': generate_research_flag_tracker(records),
        'weekly_aggregation.csv': generate_weekly_aggregation(records),
        'teaching_milestones.csv': generate_teaching_milestones(),
    }
    
    # Write outputs
    print("STEP 3: Writing output files...")
    print("-" * 80)
    
    for filename, df in outputs.items():
        output_path = OUTPUT_DIR / filename
        df.to_csv(output_path, index=False)
        print(f"✓ {filename:40s} ({len(df):6d} rows)")
    
    print()
    print("=" * 80)
    print("AGGREGATION COMPLETE")
    print("=" * 80)
    print(f"\nAll outputs saved to: {OUTPUT_DIR}")
    print(f"\nGenerated {len(outputs)} datasets:")
    for filename in sorted(outputs.keys()):
        print(f"  - {filename}")


if __name__ == "__main__":
    main()
