# Sunspire Competition - Shell History Aggregation

## Overview
Aggregated shell command history from all 12 players across 3 teams (Canopy, Harmony, Steel) covering Jan 8 - May 11, 2026.

**Total Commands Captured:** 3,853  
**Date Range:** 2026-01-08 to 2026-05-11  
**Teams:** Canopy (C1-C4), Harmony (H1-H4), Steel (T1-T4)

---

## Output Datasets

### 1. **master_command_log.csv** (3,853 rows)
**Purpose:** Complete reference log of all commands with full metadata.

**Columns:**
- `timestamp` - When the command was executed
- `team` - Team name (Canopy, Harmony, or Steel)
- `player_id` - Individual player ID (C1-C4, H1-H4, T1-T4)
- `ip` - IP address of the player's machine
- `working_directory` - Directory where command was executed
- `command_base` - Base command name (first word after sudo/bash prefixes)
- `command_with_flags` - Command with associated flags (e.g., "nmap -sV", "gobuster dir")
- `command` - Full command as entered (with all arguments)

**Use for:**
- Detailed drill-down analysis
- Verifying specific commands and their context
- Correlation with exact timestamps

---

### 2. **command_frequency.csv** (659 unique commands)
**Purpose:** Frequency analysis showing command adoption and usage patterns.

**Columns:**
- `command` - Command with flags (aggregation key)
- `count` - Total occurrences
- `first_seen` - Timestamp of first usage
- `last_seen` - Timestamp of last usage
- `teams_involved` - Which teams used this command
- `players_involved` - Which players used this command
- `ips_involved` - Which IPs used this command

**Sorted by:** Count (descending)

**Use for:**
- Identify most/least used commands
- Determine when commands were first adopted by teams
- Classify commands into "enumeration/learning" vs "exploitation" categories
- See command usage spread across teams/players

**Top 10 Commands:**
1. `ls` (420 times)
2. `nxc smb` (236 times)
3. `smbclient` (202 times)
4. `xfreerdp3` (169 times)
5. `exit` (142 times)
6. `sqlmap -u 10.100.7.45/panels.php?id=1` (116 times)
7. `ssh -i` (109 times)
8. `nmap` (106 times)
9. `clear` (82 times)
10. `nmap -sV` (78 times)

---

### 3. **daily_aggregation.csv** (82 days)
**Purpose:** Daily activity summary by player, useful for trend analysis.

**Columns:**
- `date` - Date (YYYY-MM-DD)
- `team` - Team name
- `player_id` - Player ID
- `ip` - Player's IP
- `total_commands` - Count of commands issued that day
- `unique_commands` - Count of distinct commands
- `unique_command_list` - Semicolon-separated list of unique commands

**Use for:**
- **Timeline scatter plot**: Plot (date, total_commands) to show activity volume over 3 months
- Track increased frequency/comfort as competition progresses
- Identify inactive days/players
- Correlate spikes with teaching milestones

**Example Insight:** Week of Jan 12 shows spike in activity (Network Enumeration teaching day)

---

### 4. **research_flag_tracker.csv** (203 research actions)
**Purpose:** Track student research behavior (active learning indicators).

**Columns:**
- `timestamp` - When research flag was used
- `team` - Team name
- `player_id` - Player ID
- `ip` - Player's IP
- `flag_type` - Type of research (`tldr`, `man`, or `--help flag`)
- `command` - Command being researched
- `full_command` - Full command line

**Breakdown:**
- `tldr` commands: 142 occurrences
- `--help` flags: 55 occurrences
- `man` pages: 6 occurrences

**Use for:**
- **Research intensity plot**: Count research flags by date/team
- Proves students are learning (not just running memorized scripts)
- Identify which commands required research
- Track when different teams adopted research behavior

---

### 5. **weekly_aggregation.csv** (18 rows)
**Purpose:** High-level team activity trends at weekly granularity.

**Columns:**
- `week` - Week identifier (YYYY-WNN with start date)
- `team` - Team name
- `total_commands` - Total commands that week
- `unique_commands` - Distinct command variants
- `top_5_commands` - Top 5 commands with frequencies

**Use for:**
- Simplify visualization (easier than daily data)
- Compare team productivity across weeks
- Identify when command diversity increased
- Spot activity patterns

**Notable Trend:**
- Week 3 (Jan 12): Sharp increase in Steel team activity (464 total, 100 unique)
- Week 5 (Jan 26): Sustained high activity across all teams (1,253 total commands)

---

### 6. **teaching_milestones.csv** (9 milestones)
**Purpose:** Reference timeline for overlay on command analysis.

**Columns:**
- `date` - Teaching/competition milestone date
- `topic` - What was taught/event
- `milestone_type` - Always "teaching_start" (extensible for other types)

**Milestones:**
| Date | Topic |
|------|-------|
| 2026-01-05 | Introduction to Netsiege |
| 2026-01-06 | Operating System Fundamentals |
| 2026-01-12 | Network Enumeration and Basic Attacks |
| 2026-01-13 | File Shares |
| 2026-01-20 | Basic Privilege Escalation |
| 2026-01-26 | Web 1 |
| 2026-02-02 | Defense |
| 2026-02-03 | Review and Compete |
| 2026-02-10 | Web 2 |

**Use for:**
- Overlay on timeline plots to correlate teaching with command adoption
- Verify students apply taught concepts immediately
- Identify which topics led to exploration/experimentation

---

## Recommended Analyses

### 1. Timeline Scatter Plot (Long-form Pillar)
```
X-axis: Date (Jan 8 - Feb 10)
Y-axis: Total commands per day
Color: Team (Canopy, Harmony, Steel)
Size: Unique command count
Overlay: Teaching milestones as vertical lines
```
**Data source:** `daily_aggregation.csv`

### 2. Command Type Comparison
```
Bar chart comparing:
- Enumeration/learning commands (nmap, gobuster, enum4linux, etc.)
- Exploitation commands (sqlmap, xfreerdp3, smbclient, ssh, etc.)
- Grouped by team and/or time period
```
**Data source:** `command_frequency.csv` (you classify commands into categories)

### 3. Research Behavior
```
Stacked bar chart: Research flags over time
- tldr usage trend
- man page usage trend  
- --help flag usage trend
Show: Per team, per week
```
**Data source:** `research_flag_tracker.csv`

### 4. Command Adoption Timeline
```
For specific commands of interest (e.g., nmap, sqlmap, xfreerdp3):
- First_seen date by team
- Usage frequency over time
- Does it align with teaching?
```
**Data source:** `command_frequency.csv` (filter by command)

### 5. Comfort/Skill Growth
```
Heatmap: Commands per day (daily_aggregation) 
- X-axis: Date
- Y-axis: Team/Player
- Color intensity: Command volume
Shows: Increased frequency = increased comfort
```
**Data source:** `daily_aggregation.csv`

### 6. Correlation with Teaching
```
For each milestone date, analyze:
- Commands issued in next 3-7 days
- New command types appearing post-teaching
- Research intensity changes
```
**Data sources:** `teaching_milestones.csv` + `daily_aggregation.csv` + `command_frequency.csv`

---

## How to Extend

### Add Command Classifications
Create a `command_classifications.csv`:
```csv
command,classification,category
nmap,enumeration,reconnaissance
nmap -sV,enumeration,reconnaissance
sqlmap -u,exploitation,database_attack
xfreerdp3,exploitation,lateral_movement
tldr,learning,research
man,learning,research
```

Join with `command_frequency.csv` to enable type-based filtering.

### Add Custom Time Periods
- Split `daily_aggregation.csv` into phases (pre-web, pre-defense, etc.)
- Create pivot tables by team and phase

### Track Individual Growth
- Player-level heatmaps from `daily_aggregation.csv`
- Compare player productivity within teams
- Identify role specialization (e.g., who focused on web vs network attacks)

---

## Technical Notes

- **Command Parsing:** Extracts base command + immediate flags; stops at first positional argument (IP/path)
  - Example: `nmap -sV -p 1-65535 10.100.7.40` → command_with_flags = `nmap -sV`
  
- **CSV Format:** All files use standard CSV encoding with proper quoting for fields containing commas/quotes
  
- **Timezone:** All timestamps are as recorded in shell history (no timezone conversion applied)
  
- **Data Integrity:** 3,853 valid commands successfully parsed and aggregated across all 12 players

---

## File Locations
- Script: `aggregate_shell_history.py`
- All outputs: `aggregated_data/` directory
- Source data: `logs/10.100.7.{11-34}/shell_history.csv`
