#!/bin/sh

export DEBIAN_FRONTEND=noninteractive

# description
echo "==============================="
echo " SOLARIS "
echo "==============================="
echo "Solaris is an old file sharing server. It represents reliability, stability, warmth, and a touch of nostalgia of what used to be."

# ===============================
# USER CREATION
# ===============================
echo "[*] Creating users..."

# Create solaris user
useradd -m -s /bin/bash solaris
echo "solaris:solar-paneL321" | chpasswd

# Create ops user
useradd -m -s /bin/bash ops
echo "ops:9ksP311p" | chpasswd

# Set root password
echo "root:Ag9G61RF" | chpasswd

echo "[+] Users created"

# ===============================
# SSH SERVER
# ===============================
echo "[*] Configuring SSH..."

apt-get update
apt-get install -y openssh-server

# Enable password authentication
sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config

systemctl enable ssh
systemctl start ssh

echo "[+] SSH configured"

# ===============================
# SAMBA SMB (Anonymous Share)
# ===============================
echo "[*] Configuring Samba..."

apt-get install -y samba

# Create share directory
mkdir -p /srv/samba/public
chmod 777 /srv/samba/public

# Create backup.zip containing solaris user password
mkdir -p /tmp/backup_staging
echo "# Created by sysadmin

User credentials backup:
  solaris:solar-paneL321

# Do not share this file!
" > /tmp/backup_staging/credentials.txt

cd /tmp/backup_staging # cd out
apt-get install -y zip
zip /srv/samba/public/backup.zip credentials.txt
rm -rf /tmp/backup_staging

chmod 644 /srv/samba/public/backup.zip

# Configure Samba for anonymous access
cat > /etc/samba/smb.conf << 'EOF'
[global]
   workgroup = WORKGROUP
   server string = Solaris File Server
   security = user
   map to guest = Bad User
   guest account = nobody

[public]
   path = /srv/samba/public
   browseable = yes
   read only = yes
   guest ok = yes
   public = yes
EOF

systemctl enable smbd
systemctl restart smbd

echo "[+] Samba configured with anonymous share"

# cd back to deploy directory
cd -

# ===============================
# APACHE + PHP WEBSITE (Arbitrary File Upload)
# ===============================
echo "[*] Configuring Apache with PHP..."

apt-get install -y apache2 php libapache2-mod-php

# Create web root
mkdir -p /var/www/html
cp -Rf /opt/sunspire/apps/solaris-uploader/* /var/www/html/
chmod -R 755 /var/www/html

# Create uploads directory
mkdir -p /var/www/html/uploads
chmod 777 /var/www/html/uploads

# Set ownership
chown -R www-data:www-data /var/www/html

systemctl enable apache2
systemctl restart apache2

echo "[+] Apache with PHP configured (arbitrary file upload vulnerable)"

# ===============================
# SUID base64 BINARY (Privilege Escalation)
# ===============================
echo "[*] Configuring SUID base64 binary..."

# Set SUID bit on base64
chmod u+s /usr/bin/base64

echo "[+] SUID bit set on /usr/bin/base64"

# ===============================
# CRONJOB: solaris-report.sh
# ===============================
echo "[*] Configuring reporting cronjob..."

# Create the reporting script
cat > /usr/local/bin/solaris-report.sh << 'EOF'
#!/bin/bash
# Solaris Auth Log Reporter
# Encodes the last 10 auth.log lines for secure storage

tail -n 10 /var/log/auth.log | base64 >> /var/log/auth-store.log
EOF

chmod 755 /usr/local/bin/solaris-report.sh

# Create the log file
touch /var/log/auth-store.log
chmod 644 /var/log/auth-store.log

# Add cronjob to run every 5 minutes
echo "*/5 * * * * root /usr/local/bin/solaris-report.sh" > /etc/cron.d/solaris-report

echo "[+] Cronjob configured"

# ===============================
# SSH KEYS FOR LATERAL MOVEMENT (to orbital)
# ===============================
echo "[*] Configuring SSH keys for lateral movement..."

# Create .ssh directory for solaris user
mkdir -p /home/solaris/.ssh
chmod 700 /home/solaris/.ssh

# Add SSH key pair for lateral movement to starfall
cp /opt/sunspire/credentials/sunspire_key/id_rsa /home/solaris/.ssh/id_rsa
cp /opt/sunspire/credentials/sunspire_key/id_rsa.pub /home/solaris/.ssh/id_rsa.pub

# Add a note about the key
cat > /home/solaris/.ssh/readme.txt << 'EOF'
# SSH Key for accessing other systems
EOF

chown -R solaris:solaris /home/solaris/.ssh
chmod 600 /home/solaris/.ssh/id_rsa
chmod 644 /home/solaris/.ssh/id_rsa.pub
chmod 644 /home/solaris/.ssh/readme.txt

echo "[+] SSH keys configured for lateral movement"


# ===============================
# SCORING FILES
# ===============================
echo "[*] Creating scoring control files..."

echo "" > /home/solaris/ctrl.txt
chown solaris:solaris /home/solaris/ctrl.txt
chmod 644 /home/solaris/ctrl.txt

echo "" > /var/www/html/ctrl.txt
chown www-data:www-data /var/www/html/ctrl.txt
chmod 644 /var/www/html/ctrl.txt

echo "" > /root/ctrl.txt
chmod 644 /root/ctrl.txt

echo "[+] Control files created"

# ===============================
# FINAL SETUP
# ===============================
echo "[*] Final configuration..."

# Ensure services are running
systemctl restart ssh
systemctl restart smbd
systemctl restart apache2

echo ""
echo "==============================="
echo " SOLARIS DEPLOYMENT COMPLETE "
echo "==============================="
echo ""
echo "Services:"
echo "  - SSH (OpenSSH Server)"
echo "  - SMB (Samba anonymous share)"
echo "  - HTTP (Apache + PHP)"
echo ""
echo "Users:"
echo "  - solaris:solar-paneL321"
echo "  - ops:9ksP311p"
echo "  - root:Ag9G61RF"
echo ""
echo "Attack Vectors:"
echo "  - Initial Access: SMB anonymous share contains backup.zip with creds"
echo "  - Initial Access: Arbitrary file upload on PHP website"
echo "  - Privesc: SUID base64 binary (/usr/bin/base64)"
echo "  - Lateral Movement: SSH keys in /home/solaris/.ssh/ for orbital"
echo ""
echo "Scoring:"
echo "  - Services: Website, SSH, SMB"
echo "  - Files: /root/ctrl.txt, /home/solaris/ctrl.txt, /var/www/html/ctrl.txt"
echo ""
