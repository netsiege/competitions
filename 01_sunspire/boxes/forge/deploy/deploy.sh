#!/bin/bash

export DEBIAN_FRONTEND=noninteractive

# description
echo "==============================="
echo "          FORGE                "
echo "==============================="
echo "A forge to develop new software for Sunspire. Forge is the manufacturing facility responsible for producing solar panel components and sustainable materials."

# ===============================
# USER CREATION
# ===============================
echo "[*] Creating users..."

# Create forge user
useradd -m -s /bin/bash forge
echo "forge:h1ewFWZG" | chpasswd

# Create ops user
useradd -m -s /bin/bash ops
echo "ops:9ksP311p" | chpasswd

# Set root password
echo "root:7ZjXxjQB" | chpasswd

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

# Add authorized key for forge user (lateral movement from inspire)
mkdir -p /home/forge/.ssh
chmod 700 /home/forge/.ssh
cat > /home/forge/.ssh/authorized_keys << 'EOF'
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIA1/zzaiFvdi8X9nwzWyXoKY+/c5U6WRLKxerWHLjH9/
EOF
chmod 600 /home/forge/.ssh/authorized_keys
chown -R forge:forge /home/forge/.ssh

systemctl enable ssh
systemctl start ssh

echo "[+] SSH configured (with authorized_keys for lateral movement)"

# ===============================
# NGINX (Git HTTP Server)
# ===============================
echo "[*] Installing Nginx..."

apt-get install -y nginx git

# Copy nginx config
cp /opt/sunspire/boxes/forge/deploy/nginx-git.conf /etc/nginx/sites-available/git
ln -sf /etc/nginx/sites-available/git /etc/nginx/sites-enabled/git
rm -f /etc/nginx/sites-enabled/default

# Test and reload nginx
nginx -t
systemctl enable nginx
systemctl restart nginx

echo "[+] Nginx configured"

# ===============================
# GIT HTTP REPOSITORY (Initial Access)
# ===============================
echo "[*] Creating Git HTTP repository..."

# Run the init-repo script
chmod +x /opt/sunspire/boxes/forge/deploy/init-repo.sh
/opt/sunspire/boxes/forge/deploy/init-repo.sh
git config --global --add safe.directory /var/lib/git/forge-logs.git

echo "[+] Git HTTP repository created"

# ===============================
# FORGE API (SSRF Target)
# ===============================
echo "[*] Installing Forge API..."

apt-get install -y python3 python3-pip python3-venv

# Copy API to /root/forge-api
cp -Rf /opt/sunspire/apps/forge-api /root/
rm /root/forge-api/README.md

# Install dependencies using venv
cd /root/forge-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate

# Install systemd service
cp forge-api.service /etc/systemd/system/

# Update service to use venv
sed -i 's|ExecStart=.*python3|ExecStart=/root/forge-api/venv/bin/python3|' /etc/systemd/system/forge-api.service

systemctl daemon-reload
systemctl enable forge-api
systemctl start forge-api

cd -

echo "[+] Forge API installed"

# ===============================
# PRIVESC: Git Pre-Commit Hooks
# ===============================
echo "[*] Setting up manufacturing scripts repository..."

# Create working git repo for forge user
PRIV_REPO="/home/forge/manufacturing-scripts"
mkdir -p "$PRIV_REPO"
cd "$PRIV_REPO"

git init
git config user.email "forge@sunspire.local"
git config user.name "Forge Build System"

# Add some initial scripts
cat > build.sh << 'EOF'
#!/bin/bash
# Manufacturing build script
echo "Building manufacturing components..."
echo "Build complete: $(date)"
EOF

cat > validate.sh << 'EOF'
#!/bin/bash
# Validate manufacturing output
echo "Validating output..."
exit 0
EOF

cat > readme.txt << 'EOF'
Manufacturing Scripts Repository
Every 5 minutes a commit is triggered by the root cron job.
EOF 

chmod +x build.sh validate.sh

git add .
git commit -m "Initial build scripts"

# Create pre-commit hook (world-writable - vulnerability!)
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
# Pre-commit validation hook
echo "Running pre-commit checks..."
/home/forge/manufacturing-scripts/validate.sh
EOF

chmod 777 .git/hooks/pre-commit

# Set ownership
chown -R forge:forge "$PRIV_REPO"

# Make hooks directory world-writable (vulnerability!)
chmod 777 "$PRIV_REPO/.git/hooks"
git config --global --add safe.directory /home/forge/manufacturing-scripts

cd -

echo "[+] Manufacturing scripts repository created (hooks writable)"

# ===============================
# ROOT CRON JOB (Triggers Privesc)
# ===============================
echo "[*] Setting up root cron job..."

# Copy cron script
cp /opt/sunspire/boxes/forge/deploy/root-cron.sh /usr/local/bin/forge-build.sh
chmod +x /usr/local/bin/forge-build.sh

# Add cron job for root - runs every 5 minutes
(crontab -l 2>/dev/null; echo "*/5 * * * * /usr/local/bin/forge-build.sh") | crontab -

echo "[+] Root cron job configured"

# ===============================
# SCORING FILES
# ===============================
echo "[*] Creating scoring control files..."

echo "" > /home/forge/ctrl.txt
chown forge:forge /home/forge/ctrl.txt
chmod 644 /home/forge/ctrl.txt

echo "" > /root/ctrl.txt
chmod 644 /root/ctrl.txt

echo "[+] Control files created"

# ===============================
# FINAL SETUP
# ===============================
echo "[*] Final configuration..."

# Ensure services are running
systemctl restart sshd
systemctl restart nginx
systemctl restart forge-api

echo ""
echo "==============================="
echo "  FORGE DEPLOYMENT COMPLETE   "
echo "==============================="
echo ""
echo "Services:"
echo "  - SSH (OpenSSH Server on :22)"
echo "  - HTTP (Nginx Git Server on :80)"
echo "  - API (Forge API on :4000)"
echo ""
echo "Users:"
echo "  - forge:h1ewFWZG (same as pyre - password reuse)"
echo "  - ops:9ksP311p"
echo "  - root:7ZjXxjQB"
echo ""
echo "Attack Vectors:"
echo "  - Initial Access: SSRF from Starfall → /api/info → leaks ROOT_PASSWORD"
echo "  - Initial Access: Git clone http://<ip>/git/forge-logs.git → git log -p → FORGE_USER_PASSWORD"
echo "  - Privesc: World-writable .git/hooks/pre-commit → root cron triggers"
echo ""
echo "Scoring:"
echo "  - Services: API, SSH"
echo "  - Files: /home/forge/ctrl.txt, /root/ctrl.txt"
echo ""
echo "Lateral Movement:"
echo "  - forge → pyre: Password reuse (h1ewFWZG)"
echo "  - inspire → forge: SSH key (found in windmilled dev_notes.txt)"
echo ""
