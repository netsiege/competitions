#!/bin/sh

export DEBIAN_FRONTEND=noninteractive

# description
echo "==============================="
echo " STARFALL "
echo "==============================="
echo "Starfall is a beautiful creation by our systems stewardess Fern. The same way the stars will never fall, neither will Sunspire's most critical services. Starfall is a gateway to much more..."

# ===============================
# PACKAGE INSTALLATION
# ===============================
echo "[*] Installing packages..."

apt-get update
apt-get install -y openssh-server python3 python3-pip python3-venv

echo "[+] Packages installed"

# ===============================
# USER CREATION
# ===============================
echo "[*] Creating users..."

# Create starfall user
useradd -m -s /bin/bash starfall
echo "starfall:starfall" | chpasswd

# Create ops user
useradd -m -s /bin/bash ops
echo "ops:9ksP311p" | chpasswd

# Set root password
echo "root:qi6AJZin" | chpasswd

# Add starfall to sudoers group
usermod -aG sudo starfall

echo "[+] Users created"

# ===============================
# SSH SERVER
# ===============================
echo "[*] Configuring SSH..."

# Enable password authentication
sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config

systemctl enable ssh
systemctl start ssh

echo "[+] SSH configured"

# ===============================
# FLASK API SERVICE
# ===============================
echo "[*] Configuring Flask API..."

# Create application directory
mkdir -p /opt/starfall
cp -Rf /opt/sunspire/apps/starfaller/* /opt/starfall/
chmod -R 755 /opt/starfall

# Create virtual environment and install dependencies
cd /opt/starfall
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate

# Set ownership
chown -R starfall:starfall /opt/starfall

# Install systemd service
cp /opt/starfall/starfall-api.service /etc/systemd/system/starfall-api.service

# Update service to use venv
sed -i 's|ExecStart=/usr/bin/python3|ExecStart=/opt/starfall/venv/bin/python3|' /etc/systemd/system/starfall-api.service

systemctl daemon-reload
systemctl enable starfall-api
systemctl start starfall-api

echo "[+] Flask API configured on :5000 (external) and :5001 (internal)"

# ===============================
# SCORING FILES
# ===============================
echo "[*] Creating scoring control files..."

echo "" > /home/starfall/ctrl.txt
chown starfall:starfall /home/starfall/ctrl.txt
chmod 644 /home/starfall/ctrl.txt

echo "" > /opt/starfall/ctrl.txt
chmod 644 /opt/starfall/ctrl.txt

echo "[+] Control files created"

# ===============================
# FINAL SETUP
# ===============================
echo "[*] Final configuration..."

# Ensure services are running
systemctl restart ssh
systemctl restart starfall-api

echo ""
echo "==============================="
echo " STARFALL DEPLOYMENT COMPLETE "
echo "==============================="
echo ""
echo "Services:"
echo "  - SSH (OpenSSH Server)"
echo "  - API (Flask on :5000 external, :5001 internal)"
echo ""
echo "Users:"
echo "  - starfall:starfall (sudoer)"
echo "  - ops:9ksP311p"
echo "  - root:qi6AJZin"
echo ""
echo "Attack Vectors:"
echo "  - Initial Access: Command injection on /api/health/history?file="
echo "  - Initial Access: Weak/guessable password (starfall:starfall)"
echo "  - Privesc: None needed - starfall is in sudoers group"
echo "  - Lateral Movement: SSRF via internal API :5001 to forge"
echo ""
echo "Scoring:"
echo "  - Services: API, SSH"
echo "  - Files: /home/starfall/ctrl.txt, /opt/starfall/ctrl.txt"
echo ""
