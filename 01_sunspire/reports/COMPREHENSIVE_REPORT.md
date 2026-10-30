# Comprehensive Target Attack Report
## Sunspire Forensics (All Targets, Non-Simultaneous)

**Scope**: All target-directed commands from shell history. No simultaneity constraints.
**Data Source**: `reports/all_attacks_non_simultaneous.json`

## Executive Summary

- **Total target-directed commands**: 1377
- **Targets covered**: 8
- **Teams observed**: Team 1 (.1x), Team 2 (.2x), Team 3 (.3x)

## Coverage Table

| Target | Commands | Teams Seen | Vector Families |
|---|---:|---|---:|
| **crucible** | 29 | Team 1, Team 3 | 1 |
| **ember** | 288 | Team 1, Team 2, Team 3 | 3 |
| **forge** | 60 | Team 1, Team 2, Team 3 | 3 |
| **helios** | 80 | Team 1, Team 2, Team 3 | 3 |
| **inspire** | 104 | Team 1, Team 3 | 2 |
| **orbital** | 317 | Team 1, Team 2, Team 3 | 3 |
| **pyre** | 391 | Team 1, Team 2, Team 3 | 3 |
| **starfall** | 108 | Team 1, Team 2, Team 3 | 2 |

## Per-Target Analysis

### CRUCIBLE

- **Commands on target**: 29
- **Teams observed**: Team 1, Team 3
- **Vector families identified**: 1
- **Unmatched commands**: 11

**Observed TTP Families**

| TTP Family | Total Matched Commands | Teams | Sample Ref | Sample Command Snippet |
|---|---:|---|---|---|
| recon/access | 18 | Team 1, Team 3 | logs/10.100.7.11/shell_history.csv#L298 | `nmap -sV -p 5985 -T3 10.100.7.47` |

**Team-by-Team TTP Use**

| Team | TTP Families Used | Approx TTP Activity Score | Sample Evidence Ref | Sample Command Snippet |
|---|---|---:|---|---|
| Team 1 (.1x) | recon/access | 18 | logs/10.100.7.11/shell_history.csv#L298 | `nmap -sV -p 5985 -T3 10.100.7.47` |
| Team 2 (.2x) | none observed in matched vectors | 0 |  |  |
| Team 3 (.3x) | recon/access | 18 | logs/10.100.7.11/shell_history.csv#L298 | `nmap -sV -p 5985 -T3 10.100.7.47` |

### EMBER

- **Commands on target**: 288
- **Teams observed**: Team 1, Team 2, Team 3
- **Vector families identified**: 3
- **Unmatched commands**: 49

**Observed TTP Families**

| TTP Family | Total Matched Commands | Teams | Sample Ref | Sample Command Snippet |
|---|---:|---|---|---|
| RDP access | 69 | Team 1, Team 2, Team 3 | logs/10.100.7.21/shell_history.csv#L132 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:PNqRrcXU4W0eWaE1MGvy` |
| SMB/scripts path | 170 | Team 1, Team 2, Team 3 | logs/10.100.7.11/shell_history.csv#L185 | `nxc smb 10.100.7.46 -u EMBER$ -p J4f9juEr --shares` |
| scheduled task/script abuse | 11 | Team 2, Team 3 | logs/10.100.7.32/shell_history.csv#L701 | `smbclient //10.100.7.46/Scripts --user guest -c 'put maintenance.ps1'` |

**Team-by-Team TTP Use**

| Team | TTP Families Used | Approx TTP Activity Score | Sample Evidence Ref | Sample Command Snippet |
|---|---|---:|---|---|
| Team 1 (.1x) | RDP access, SMB/scripts path | 239 | logs/10.100.7.21/shell_history.csv#L132 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:PNqRrcXU4W0eWaE1MGvy` |
| Team 2 (.2x) | RDP access, SMB/scripts path, scheduled task/script abuse | 250 | logs/10.100.7.21/shell_history.csv#L132 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:PNqRrcXU4W0eWaE1MGvy` |
| Team 3 (.3x) | RDP access, SMB/scripts path, scheduled task/script abuse | 250 | logs/10.100.7.21/shell_history.csv#L132 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:PNqRrcXU4W0eWaE1MGvy` |

**Team-Differentiated Approach Notes**
- `RDP access` used by Team 1, Team 2, Team 3, while `scheduled task/script abuse` used by Team 2, Team 3.
- `SMB/scripts path` used by Team 1, Team 2, Team 3, while `scheduled task/script abuse` used by Team 2, Team 3.

### FORGE

- **Commands on target**: 60
- **Teams observed**: Team 1, Team 2, Team 3
- **Vector families identified**: 3
- **Unmatched commands**: 17

**Observed TTP Families**

| TTP Family | Total Matched Commands | Teams | Sample Ref | Sample Command Snippet |
|---|---:|---|---|---|
| Git artifact/history path | 15 | Team 1, Team 3 | logs/10.100.7.32/shell_history.csv#L268 | `git clone 10.100.7.44` |
| SSH credential/lateral movement | 25 | Team 1, Team 2, Team 3 | logs/10.100.7.21/shell_history.csv#L83 | `hydra -I forge -P rockyou.txt ssh 10.100.7.44` |
| web enum against forge | 3 | Team 2 | logs/10.100.7.24/shell_history.csv#L224 | `gobuster dir -u https://http://10.100.7.44/ -w wordlist.txt` |

**Team-by-Team TTP Use**

| Team | TTP Families Used | Approx TTP Activity Score | Sample Evidence Ref | Sample Command Snippet |
|---|---|---:|---|---|
| Team 1 (.1x) | Git artifact/history path, SSH credential/lateral movement | 40 | logs/10.100.7.21/shell_history.csv#L83 | `hydra -I forge -P rockyou.txt ssh 10.100.7.44` |
| Team 2 (.2x) | SSH credential/lateral movement, web enum against forge | 28 | logs/10.100.7.21/shell_history.csv#L83 | `hydra -I forge -P rockyou.txt ssh 10.100.7.44` |
| Team 3 (.3x) | Git artifact/history path, SSH credential/lateral movement | 40 | logs/10.100.7.21/shell_history.csv#L83 | `hydra -I forge -P rockyou.txt ssh 10.100.7.44` |

**Team-Differentiated Approach Notes**
- `Git artifact/history path` used by Team 1, Team 3, while `SSH credential/lateral movement` used by Team 1, Team 2, Team 3.
- `Git artifact/history path` used by Team 1, Team 3, while `web enum against forge` used by Team 2.
- `SSH credential/lateral movement` used by Team 1, Team 2, Team 3, while `web enum against forge` used by Team 2.

### HELIOS

- **Commands on target**: 80
- **Teams observed**: Team 1, Team 2, Team 3
- **Vector families identified**: 3
- **Unmatched commands**: 30

**Observed TTP Families**

| TTP Family | Total Matched Commands | Teams | Sample Ref | Sample Command Snippet |
|---|---:|---|---|---|
| RDP access | 12 | Team 2, Team 3 | logs/10.100.7.34/shell_history.csv#L6 | `xfreerdp3 /u:helios /v:10.100.7.41 /u:')b:t].n!5<Xj=/DGXtv&'` |
| SMB/enum | 31 | Team 1, Team 2 | logs/10.100.7.11/shell_history.csv#L83 | `nxc smb 10.100.7.41 -u guest` |
| ssh access | 7 | Team 2, Team 3 | logs/10.100.7.32/shell_history.csv#L109 | `ssh -i ~/.ssh/helios helios@10.100.7.41` |

**Team-by-Team TTP Use**

| Team | TTP Families Used | Approx TTP Activity Score | Sample Evidence Ref | Sample Command Snippet |
|---|---|---:|---|---|
| Team 1 (.1x) | SMB/enum | 31 | logs/10.100.7.11/shell_history.csv#L83 | `nxc smb 10.100.7.41 -u guest` |
| Team 2 (.2x) | RDP access, SMB/enum, ssh access | 50 | logs/10.100.7.11/shell_history.csv#L83 | `nxc smb 10.100.7.41 -u guest` |
| Team 3 (.3x) | RDP access, ssh access | 19 | logs/10.100.7.34/shell_history.csv#L6 | `xfreerdp3 /u:helios /v:10.100.7.41 /u:')b:t].n!5<Xj=/DGXtv&'` |

**Team-Differentiated Approach Notes**
- `RDP access` used by Team 2, Team 3, while `SMB/enum` used by Team 1, Team 2.
- `SMB/enum` used by Team 1, Team 2, while `ssh access` used by Team 2, Team 3.

### INSPIRE

- **Commands on target**: 104
- **Teams observed**: Team 1, Team 3
- **Vector families identified**: 2
- **Unmatched commands**: 34

**Observed TTP Families**

| TTP Family | Total Matched Commands | Teams | Sample Ref | Sample Command Snippet |
|---|---:|---|---|---|
| MySQL access | 44 | Team 1, Team 3 | logs/10.100.7.34/shell_history.csv#L86 | `mysql -h 10.100.7.48 -u root -\n` |
| web enum/recon | 26 | Team 1, Team 3 | logs/10.100.7.11/shell_history.csv#L300 | `nmap -sV -p 5985 -T3 10.100.7.48` |

**Team-by-Team TTP Use**

| Team | TTP Families Used | Approx TTP Activity Score | Sample Evidence Ref | Sample Command Snippet |
|---|---|---:|---|---|
| Team 1 (.1x) | MySQL access, web enum/recon | 70 | logs/10.100.7.11/shell_history.csv#L300 | `nmap -sV -p 5985 -T3 10.100.7.48` |
| Team 2 (.2x) | none observed in matched vectors | 0 |  |  |
| Team 3 (.3x) | MySQL access, web enum/recon | 70 | logs/10.100.7.11/shell_history.csv#L300 | `nmap -sV -p 5985 -T3 10.100.7.48` |

### ORBITAL

- **Commands on target**: 317
- **Teams observed**: Team 1, Team 2, Team 3
- **Vector families identified**: 3
- **Unmatched commands**: 155

**Observed TTP Families**

| TTP Family | Total Matched Commands | Teams | Sample Ref | Sample Command Snippet |
|---|---:|---|---|---|
| MSSQL | 11 | Team 1 | logs/10.100.7.11/shell_history.csv#L327 | `mssqlclient.py sa@10.100.7.42 -p 1433 # When prompted for password, just hit Enter` |
| SMB anonymous/enum | 124 | Team 1, Team 2, Team 3 | logs/10.100.7.11/shell_history.csv#L339 | `nxc smb 10.100.7.42 -u Administrator` |
| WinRM | 27 | Team 1, Team 2, Team 3 | logs/10.100.7.11/shell_history.csv#L73 | `evil-winrm -i 10.100.7.42 -u orbital` |

**Team-by-Team TTP Use**

| Team | TTP Families Used | Approx TTP Activity Score | Sample Evidence Ref | Sample Command Snippet |
|---|---|---:|---|---|
| Team 1 (.1x) | MSSQL, SMB anonymous/enum, WinRM | 162 | logs/10.100.7.11/shell_history.csv#L73 | `evil-winrm -i 10.100.7.42 -u orbital` |
| Team 2 (.2x) | SMB anonymous/enum, WinRM | 151 | logs/10.100.7.11/shell_history.csv#L73 | `evil-winrm -i 10.100.7.42 -u orbital` |
| Team 3 (.3x) | SMB anonymous/enum, WinRM | 151 | logs/10.100.7.11/shell_history.csv#L73 | `evil-winrm -i 10.100.7.42 -u orbital` |

**Team-Differentiated Approach Notes**
- `MSSQL` used by Team 1, while `SMB anonymous/enum` used by Team 1, Team 2, Team 3.
- `MSSQL` used by Team 1, while `WinRM` used by Team 1, Team 2, Team 3.

### PYRE

- **Commands on target**: 391
- **Teams observed**: Team 1, Team 2, Team 3
- **Vector families identified**: 3
- **Unmatched commands**: 152

**Observed TTP Families**

| TTP Family | Total Matched Commands | Teams | Sample Ref | Sample Command Snippet |
|---|---:|---|---|---|
| DB/file extraction via SQLi | 81 | Team 1, Team 3 | logs/10.100.7.32/shell_history.csv#L807 | `sqlmap -u http://10.100.7.45/panels.php?id=1" --dbs"` |
| OS shell via SQLi | 55 | Team 1, Team 3 | logs/10.100.7.32/shell_history.csv#L906 | `sqlmap -u http://10.100.7.45/panels.php?id=1" --os-cmd=whoami"` |
| SQL injection | 239 | Team 1, Team 3 | logs/10.100.7.32/shell_history.csv#L735 | `curl http://10.100.7.45/panels.php?id=3` |

**Team-by-Team TTP Use**

| Team | TTP Families Used | Approx TTP Activity Score | Sample Evidence Ref | Sample Command Snippet |
|---|---|---:|---|---|
| Team 1 (.1x) | DB/file extraction via SQLi, OS shell via SQLi, SQL injection | 375 | logs/10.100.7.32/shell_history.csv#L735 | `curl http://10.100.7.45/panels.php?id=3` |
| Team 2 (.2x) | none observed in matched vectors | 0 |  |  |
| Team 3 (.3x) | DB/file extraction via SQLi, OS shell via SQLi, SQL injection | 375 | logs/10.100.7.32/shell_history.csv#L735 | `curl http://10.100.7.45/panels.php?id=3` |

### STARFALL

- **Commands on target**: 108
- **Teams observed**: Team 1, Team 2, Team 3
- **Vector families identified**: 2
- **Unmatched commands**: 23

**Observed TTP Families**

| TTP Family | Total Matched Commands | Teams | Sample Ref | Sample Command Snippet |
|---|---:|---|---|---|
| ssh access | 73 | Team 1, Team 3 | logs/10.100.7.34/shell_history.csv#L12 | `ssh superuser@10.100.7.43` |
| web/api probing | 12 | Team 1, Team 2, Team 3 | logs/10.100.7.34/shell_history.csv#L13 | `nmap 10.100.7.41 10.100.7.42 10.100.7.43` |

**Team-by-Team TTP Use**

| Team | TTP Families Used | Approx TTP Activity Score | Sample Evidence Ref | Sample Command Snippet |
|---|---|---:|---|---|
| Team 1 (.1x) | ssh access, web/api probing | 85 | logs/10.100.7.34/shell_history.csv#L12 | `ssh superuser@10.100.7.43` |
| Team 2 (.2x) | web/api probing | 12 | logs/10.100.7.34/shell_history.csv#L13 | `nmap 10.100.7.41 10.100.7.42 10.100.7.43` |
| Team 3 (.3x) | ssh access, web/api probing | 85 | logs/10.100.7.34/shell_history.csv#L12 | `ssh superuser@10.100.7.43` |

**Team-Differentiated Approach Notes**
- `ssh access` used by Team 1, Team 3, while `web/api probing` used by Team 1, Team 2, Team 3.

## Cross-Target Findings

**Highest command-volume targets**
- pyre: 391 commands
- orbital: 317 commands
- ember: 288 commands
- starfall: 108 commands
- inspire: 104 commands

This report intentionally ignores simultaneity and focuses only on per-target attack coverage and team TTP differences.
