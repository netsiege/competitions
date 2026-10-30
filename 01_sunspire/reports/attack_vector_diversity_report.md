# Attack Vector Diversity Report

**Analysis**: Which attack vectors were exploited by different teams against each target (non-simultaneous).

## Summary by Target

| Box | Teams | Vectors | Multi-Vector Exploits |
|---|---|---|---|
| **ember** | Team 1, Team 2, Team 3 | 2 | 2 |
| **orbital** | Team 1, Team 2, Team 3 | 3 | 6 |
| **pyre** | Team 1, Team 3 | 1 | 0 |

## Detailed Breakdown

### ORBITAL

**Teams Involved**: Team 1, Team 2, Team 3

| Attack Vector | Teams | Count | Sample Command |
|---|---|---|---|
| MSSQL | Team 1 | 1 | `sqlcmd -S tcp:10.100.7.42,1433...` |
| SMB Anonymous | Team 1, Team 2, Team 3 | 16 | `nxc smb 10.100.7.42 -u orbital -p securepassword...` |
| WinRM Access | Team 1, Team 3 | 8 | `evil-winrm -i 10.100.7.42 -u root...` |

### EMBER

**Teams Involved**: Team 1, Team 2, Team 3

| Attack Vector | Teams | Count | Sample Command |
|---|---|---|---|
| RDP Access | Team 1, Team 2 | 51 | `xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!...` |
| SMB Writable Scripts | Team 1, Team 2, Team 3 | 21 | `smbclient //10.100.7.46/Scripts --user guest...` |

### PYRE

**Teams Involved**: Team 1, Team 3

| Attack Vector | Teams | Count | Sample Command |
|---|---|---|---|
| SQL Injection | Team 1, Team 3 | 76 | `sqlmap -u http://10.100.7.45/panels.php?id=1" -D "pyrewatch" -T "alerts" --threads $(nproc)"...` |

## Cross-Vector Analysis

**Targets with most diverse attack strategies (2+ teams using different vectors):**

### orbital
- **Teams**: Team 1, Team 2, Team 3
- **Unique Vectors Attempted**: 3
- **Vector Coverage**:
  - MSSQL: exploited by Team 1 (1 times)
  - SMB Anonymous: exploited by Team 1, Team 2, Team 3 (16 times)
  - WinRM Access: exploited by Team 1, Team 3 (8 times)

### ember
- **Teams**: Team 1, Team 2, Team 3
- **Unique Vectors Attempted**: 2
- **Vector Coverage**:
  - RDP Access: exploited by Team 1, Team 2 (51 times)
  - SMB Writable Scripts: exploited by Team 1, Team 2, Team 3 (21 times)

### pyre
- **Teams**: Team 1, Team 3
- **Unique Vectors Attempted**: 1
- **Vector Coverage**:
  - SQL Injection: exploited by Team 1, Team 3 (76 times)

