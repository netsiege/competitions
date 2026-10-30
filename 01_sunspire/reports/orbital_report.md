# Orbital (10.100.7.42) Concurrent Incident Report

**Total incidents targeting Orbital**: 18

## Vulnerability Summary
- SMB: 36 incidents
- anonymous: 36 incidents
- base64: 18 incidents
- git: 18 incidents
- sql: 54 incidents

## All Incidents
### Incident 1
- Time window: 2026-01-13T19:19:00
- Target: orbital (10.100.7.42)
- Number of entries: 2
- Entries:
  - 2026-01-13T19:19:36 | logs/10.100.7.13/shell_history.csv#L49
    Command: `evil-winrm -i 10.100.7.42 -u root`
  - 2026-01-13T19:19:19 | logs/10.100.7.24/shell_history.csv#L49
    Command: `nxc smb 10.100.7.42 -u orbital -p securepassword`
- Matched vulnerability documentation:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

### Incident 2
- Time window: 2026-01-13T19:54:00
- Target: orbital (10.100.7.42)
- Number of entries: 4
- Entries:
  - 2026-01-13T19:54:11 | logs/10.100.7.11/shell_history.csv#L73
    Command: `evil-winrm -i 10.100.7.42 -u orbital`
  - 2026-01-13T19:54:55 | logs/10.100.7.11/shell_history.csv#L74
    Command: `evil-winrm -i 10.100.7.42 -u orbital`
  - 2026-01-13T19:54:38 | logs/10.100.7.32/shell_history.csv#L321
    Command: `smbclient //10.100.7.42/public --user guest`
  - 2026-01-13T19:54:53 | logs/10.100.7.32/shell_history.csv#L322
    Command: `smbclient //10.100.7.42/public --user guest`
- Matched vulnerability documentation:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

### Incident 3
- Time window: 2026-01-13T19:56:00
- Target: orbital (10.100.7.42)
- Number of entries: 2
- Entries:
  - 2026-01-13T19:56:00 | logs/10.100.7.11/shell_history.csv#L77
    Command: `evil-winrm -i 10.100.7.42 -u orbital`
  - 2026-01-13T19:56:49 | logs/10.100.7.32/shell_history.csv#L326
    Command: `nxc smb 10.100.7.42 -u guest -p '' --shares`
- Matched vulnerability documentation:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

### Incident 4
- Time window: 2026-01-13T19:58:00
- Target: orbital (10.100.7.42)
- Number of entries: 4
- Entries:
  - 2026-01-13T19:58:28 | logs/10.100.7.32/shell_history.csv#L330
    Command: `nxc smb 10.100.7.42 -u guest -p ''`
  - 2026-01-13T19:58:59 | logs/10.100.7.32/shell_history.csv#L331
    Command: `nxc smb 10.100.7.42 -u solaris -p solar-paneL321`
  - 2026-01-13T19:58:53 | logs/10.100.7.24/shell_history.csv#L67
    Command: `xfreerdp3 /u:orbital /v:10.100.7.42 /p:securepassword`
  - 2026-01-13T19:58:57 | logs/10.100.7.24/shell_history.csv#L68
    Command: `xfreerdp3 /u:orbital /v:10.100.7.42 /p:securepassword`
- Matched vulnerability documentation:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

### Incident 5
- Time window: 2026-01-13T19:59:00
- Target: orbital (10.100.7.42)
- Number of entries: 4
- Entries:
  - 2026-01-13T19:59:40 | logs/10.100.7.11/shell_history.csv#L79
    Command: `evil-winrm -i 10.100.7.42 -u root`
  - 2026-01-13T19:59:53 | logs/10.100.7.32/shell_history.csv#L332
    Command: `nxc smb 10.100.7.42 -u solaris -p solar-paneL321`
  - 2026-01-13T19:59:00 | logs/10.100.7.24/shell_history.csv#L69
    Command: `xfreerdp3 /u:orbital /v:10.100.7.42 /p:securepassword`
  - 2026-01-13T19:59:10 | logs/10.100.7.24/shell_history.csv#L70
    Command: `xfreerdp3 /u:orbital /v:10.100.7.42 /p:securepassword`
- Matched vulnerability documentation:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

### Incident 6
- Time window: 2026-01-13T20:01:00
- Target: orbital (10.100.7.42)
- Number of entries: 2
- Entries:
  - 2026-01-13T20:01:40 | logs/10.100.7.11/shell_history.csv#L81
    Command: `evil-winrm -i 10.100.7.42`
  - 2026-01-13T20:01:57 | logs/10.100.7.32/shell_history.csv#L342
    Command: `nxc smb 10.100.7.42 -u guest -X echo""`
- Matched vulnerability documentation:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

### Incident 7
- Time window: 2026-01-26T18:45:00
- Target: orbital (10.100.7.42)
- Number of entries: 3
- Entries:
  - 2026-01-26T18:45:14 | logs/10.100.7.11/shell_history.csv#L144
    Command: `evil-winrm -i 10.100.7.42 -u solaris`
  - 2026-01-26T18:45:14 | logs/10.100.7.24/shell_history.csv#L100
    Command: `xfreerdp3 /u:orbital /v:10.100.7.42`
  - 2026-01-26T18:45:27 | logs/10.100.7.24/shell_history.csv#L101
    Command: `xfreerdp3 /u:orbital /v:10.100.7.42`
- Matched vulnerability documentation:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

### Incident 8
- Time window: 2026-02-10T19:56:00
- Target: orbital (10.100.7.42)
- Number of entries: 3
- Entries:
  - 2026-02-10T19:56:27 | logs/10.100.7.34/shell_history.csv#L113
    Command: `enum4linux -a 10.100.7.42`
  - 2026-02-10T19:56:40 | logs/10.100.7.34/shell_history.csv#L114
    Command: `nmap --script smb-enum-shares,smb-enum-users -p445 10.100.7.42`
  - 2026-02-10T19:56:13 | logs/10.100.7.14/shell_history.csv#L611
    Command: `sqlcmd -S tcp:10.100.7.42,1433`
- Matched vulnerability documentation:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

### Incident 9
- Time window: 2026-02-10T20:10:00
- Target: orbital (10.100.7.42)
- Number of entries: 2
- Entries:
  - 2026-02-10T20:10:47 | logs/10.100.7.11/shell_history.csv#L356
    Command: `nxc smb 10.100.7.42 -u orbital -p 'Canopy@123'`
  - 2026-02-10T20:10:46 | logs/10.100.7.31/shell_history.csv#L96
    Command: `nxc smb 10.100.7.42 -u orbital -p 123 -X Restart-Computer`
- Matched vulnerability documentation:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

### Incident 10
- Time window: 2026-02-09T18:52:00
- Target: orbital (10.100.7.42)
- Number of entries: 4
- Entries:
  - 2026-02-09T18:52:52 | logs/10.100.7.33/shell_history.csv#L161
    Command: `ssh orbital@10.100.7.42`
  - 2026-02-09T18:52:58 | logs/10.100.7.33/shell_history.csv#L162
    Command: `ssh orbital@10.100.7.42`
  - 2026-02-09T18:52:59 | logs/10.100.7.33/shell_history.csv#L163
    Command: `ssh orbital@10.100.7.42`
  - 2026-02-09T18:52:25 | logs/10.100.7.14/shell_history.csv#L478
    Command: `smbmap -H 10.100.7.42 -u guest -p "`
- Matched vulnerability documentation:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

### Incident 11
- Time window: 2026-02-09T19:37:00
- Target: orbital (10.100.7.42)
- Number of entries: 2
- Entries:
  - 2026-02-09T19:37:16 | logs/10.100.7.33/shell_history.csv#L170
    Command: `evil-winrm -i 10.100.7.42 -u orbital -p securepassword`
  - 2026-02-09T19:37:21 | logs/10.100.7.14/shell_history.csv#L511
    Command: `xfreerdp3 /v:10.100.7.42 /u:orbital /p:securepassword`
- Matched vulnerability documentation:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

### Incident 12
- Time window: 2026-01-12T19:54:00
- Target: orbital (10.100.7.42)
- Number of entries: 2
- Entries:
  - 2026-01-12T19:54:39 | logs/10.100.7.34/shell_history.csv#L13
    Command: `nmap 10.100.7.41 10.100.7.42 10.100.7.43`
  - 2026-01-12T19:54:57 | logs/10.100.7.13/shell_history.csv#L34
    Command: `hydra -l guest -P /usr/share/wordlists/rockyou.txt ssh://10.100.7.42`
- Matched vulnerability documentation:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

### Incident 13
- Time window: 2026-01-13T19:49:00
- Target: orbital (10.100.7.42)
- Number of entries: 2
- Entries:
  - 2026-01-13T19:49:30 | logs/10.100.7.32/shell_history.csv#L314
    Command: `nxc smb 10.100.7.42 -u guest -p '' --shares`
  - 2026-01-13T19:49:45 | logs/10.100.7.24/shell_history.csv#L62
    Command: `xfreerdp3 /u:orbital /v:10.100.7.42 /p:securepassword`
- Matched vulnerability documentation:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

### Incident 14
- Time window: 2026-01-13T20:14:00
- Target: orbital (10.100.7.42)
- Number of entries: 3
- Entries:
  - 2026-01-13T20:14:46 | logs/10.100.7.32/shell_history.csv#L353
    Command: `nxc smb 10.100.7.42 -u orbital -p orbital""`
  - 2026-01-13T20:14:38 | logs/10.100.7.24/shell_history.csv#L81
    Command: `enum4linux -a 10.100.7.42`
  - 2026-01-13T20:14:39 | logs/10.100.7.24/shell_history.csv#L82
    Command: `enum4linux -a 10.100.7.42`
- Matched vulnerability documentation:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

### Incident 15
- Time window: 2026-02-10T19:54:00
- Target: orbital (10.100.7.42)
- Number of entries: 2
- Entries:
  - 2026-02-10T19:54:15 | logs/10.100.7.34/shell_history.csv#L110
    Command: `nmap -sC -sV -p 3389,445 10.100.7.42`
  - 2026-02-10T19:54:54 | logs/10.100.7.14/shell_history.csv#L609
    Command: `10.100.7.42`
- Matched vulnerability documentation:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

### Incident 16
- Time window: 2026-02-10T19:55:00
- Target: orbital (10.100.7.42)
- Number of entries: 3
- Entries:
  - 2026-02-10T19:55:34 | logs/10.100.7.34/shell_history.csv#L111
    Command: `nmap -sC -sV -p- -T4 10.100.7.42`
  - 2026-02-10T19:55:48 | logs/10.100.7.34/shell_history.csv#L112
    Command: `smbclient -L //10.100.7.42/ -N`
  - 2026-02-10T19:55:00 | logs/10.100.7.14/shell_history.csv#L610
    Command: `nmap 10.100.7.42`
- Matched vulnerability documentation:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

### Incident 17
- Time window: 2026-01-12T19:32:00
- Target: orbital (10.100.7.42)
- Number of entries: 5
- Entries:
  - 2026-01-12T19:32:56 | logs/10.100.7.13/shell_history.csv#L30
    Command: `nmap -sV -p 1-65535 -T3 10.100.7.42`
  - 2026-01-12T19:32:19 | logs/10.100.7.22/shell_history.csv#L37
    Command: `xfreerdp3 /u:Administrator /v:10.100.7.42 /p:$HEX[330a]`
  - 2026-01-12T19:32:41 | logs/10.100.7.22/shell_history.csv#L38
    Command: `xfreerdp3 /u:orbital /v:10.100.7.42 /p:abc123`
  - 2026-01-12T19:32:45 | logs/10.100.7.22/shell_history.csv#L39
    Command: `xfreerdp3 /u:orbital /v:10.100.7.42 /p:qwert`
  - 2026-01-12T19:32:48 | logs/10.100.7.22/shell_history.csv#L40
    Command: `xfreerdp3 /u:orbital /v:10.100.7.42 /p:qwerty`
- Matched vulnerability documentation:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

### Incident 18
- Time window: 2026-01-12T19:48:00
- Target: orbital (10.100.7.42)
- Number of entries: 2
- Entries:
  - 2026-01-12T19:48:47 | logs/10.100.7.13/shell_history.csv#L33
    Command: `hydra -l administrator -P /usr/share/wordlists/rockyou.txt ssh://10.100.7.42`
  - 2026-01-12T19:48:42 | logs/10.100.7.22/shell_history.csv#L42
    Command: `xfreerdp3 /u:orbital /v:10.100.7.42 /p:securepassword`
- Matched vulnerability documentation:
  - boxes/orbital/documentation.md: base64, sql, anonymous, SMB
  - boxes/orbital/deploy/Install-MSSQL.ps1: sql, git
  - boxes/orbital/deploy/deploy.ps1: sql, anonymous, SMB

