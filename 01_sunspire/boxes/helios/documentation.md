# Helios

> Helios is a Windows server that is primarily used for administration tasks across the network. Just as how Helios takes his chariot across the sky, this server allows Sunspire network stewards to walk across the network.

---

## Overview

| Property | Value |
|----------|-------|
| Difficulty | Easy |
| OS | Windows Server 2022 |
| Services | VNC, RDP |
| Initial Access | Anonymous VNC, Weak Password, Password Reuse, .rdp from orbital |
| Privilege Escalation | PowerShell History, Environment Variable |
| Lateral Movement | SSH Keys → starfall |

---

## Users

| Username | Password | Notes |
|----------|----------|-------|
| helios | password | Weak/guessable password |
| pyre | h1ewFWZG | Same password as pyre user on pyre server |
| ops | 9ksP311p | |
| Administrator | BTw5hYqi | |

---

## Services

### Remote Desktop (RDP)
- Listening on port `:3389`
- Network Level Authentication (NLA) disabled
- Runs as Windows service `TermService`
- Accessible by users in "Remote Desktop Users" group (helios)

---

## Attack Vectors

### Initial Access

#### Option 1: Weak/Guessable Password
The `helios` user has an extremely weak password.

1. Attempt common passwords:
   ```
   helios:password
   ```
2. Use for RDP or other authenticated access

#### Option 2: Password Reuse (pyre)
The `pyre` user on this machine has the same password as the `pyre` user on the pyre server.

1. If you've compromised pyre server, try the same credentials:
   ```
   pyre:h1ewFWZG
   ```

#### Option 3: .rdp File from Orbital
An `.rdp` file found on the orbital machine can be used to connect to Helios.

---

### Privilege Escalation

#### Option 1: PowerShell History
The PowerShell command history contains the Administrator password.

1. Check PowerShell history:
   ```powershell
   Get-Content $env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
   ```
   Or navigate to:
   ```
   C:\Users\helios\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
   ```

2. Find the `net user` command containing the password:
   ```
   net user Administrator BTw5hYqi
   ```

3. Use the password to escalate:
   ```powershell
   runas /user:Administrator cmd.exe
   ```

#### Option 2: Environment Variable
The Administrator password is stored in a system environment variable.

1. List environment variables:
   ```powershell
   Get-ChildItem Env:
   ```
   Or:
   ```cmd
   set
   ```

2. Find the `ADMIN_BACKUP_KEY` variable:
   ```
   ADMIN_BACKUP_KEY=BTw5hYqi
   ```

3. Use the password to escalate to Administrator

---

### Lateral Movement

#### SSH Keys → starfall
SSH keys are available in the helios user's home directory.

1. Check for SSH keys:
   ```powershell
   dir C:\Users\helios\
   type C:\Users\helios\readme.txt
   ```

2. Use the private key to SSH to starfall:
   ```powershell
   ssh -i C:\Users\helios\id_rsa user@starfall
   ```

---

## Scoring

### Services
- [ ] VNC (TightVNC on :5900)
- [ ] RDP (Remote Desktop on :3389)

### Control Files
- [ ] `C:\Administrator\ctrl.txt`
- [ ] `C:\Users\helios\ctrl.txt`

---

## File Locations

| Purpose | Path |
|---------|------|
| PowerShell History | C:\Users\helios\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt |
| SSH Private Key | C:\Users\helios\id_rsa |
| SSH Readme | C:\Users\helios\readme.txt |
| Admin Control File | C:\Administrator\ctrl.txt |
| Helios Control File | C:\Users\helios\ctrl.txt |

---

## Firewall Rules

| Rule | Port | Protocol | Direction |
|------|------|----------|-----------|
| Remote Desktop | 3389 | TCP | Inbound |

---

## Notes

- Windows Defender real-time monitoring is disabled
- Server Manager auto-start is disabled
- User profiles may need to be created by logging in as the user first (see commented section in deploy.ps1)
