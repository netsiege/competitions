#!/bin/bash

export DEBIAN_FRONTEND=noninteractive

# description
echo "==============================="
echo "         INSPIRE               "
echo "==============================="
echo "A solar weather and energy forecasting server for Sunspire. Inspire monitors weather patterns and predicts optimal energy generation across the solar grid."

# ===============================
# PACKAGE INSTALLATION
# ===============================
echo "[*] Installing packages..."

apt-get update
apt-get install -y openssh-server mysql-server apache2 php php-mysql php-json jq python3 python3-pip python3-venv

echo "[+] Packages installed"

# ===============================
# USER CREATION
# ===============================
echo "[*] Creating users..."

# Create inspire user
useradd -m -s /bin/bash inspire
echo "inspire:aN8ivVL3" | chpasswd

# Create ops user
useradd -m -s /bin/bash ops
echo "ops:9ksP311p" | chpasswd

# Set root password
echo "root:Mc8HYoDw" | chpasswd

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
# MYSQL (Initial Access - Anonymous Login)
# ===============================
echo "[*] Installing MySQL..."

# Start MySQL
systemctl enable mysql
systemctl start mysql

# Configure MySQL - allow anonymous login and create database
mysql << 'EOF'
-- Create database for energy heatmap
CREATE DATABASE IF NOT EXISTS sunspire_energy;

-- Create inspire user
CREATE USER IF NOT EXISTS 'inspire'@'localhost' IDENTIFIED BY 'aN8ivVL3';
GRANT ALL PRIVILEGES ON sunspire_energy.* TO 'inspire'@'localhost';

-- Enable anonymous login (vulnerability!)
CREATE USER IF NOT EXISTS ''@'%' IDENTIFIED BY '';
GRANT SELECT ON sunspire_energy.* TO ''@'%';

-- Create credentials table (discoverable via anonymous access)
USE sunspire_energy;

CREATE TABLE IF NOT EXISTS system_config (
    id INT AUTO_INCREMENT PRIMARY KEY,
    setting_name VARCHAR(64),
    setting_value VARCHAR(256),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert credential leak
INSERT INTO system_config (setting_name, setting_value) VALUES 
    ('app_name', 'Energy Heatmap'),
    ('version', '2.1.4'),
    ('db_user', 'inspire'),
    ('db_password', 'aN8ivVL3'),
    ('maintenance_mode', 'false');

-- Create some decoy energy data
CREATE TABLE IF NOT EXISTS energy_readings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    region VARCHAR(32),
    timestamp DATETIME,
    solar_output_mw DECIMAL(10,2),
    wind_output_mw DECIMAL(10,2),
    demand_mw DECIMAL(10,2)
);

INSERT INTO energy_readings (region, timestamp, solar_output_mw, wind_output_mw, demand_mw) VALUES
    ('north', NOW() - INTERVAL 1 HOUR, 245.50, 89.20, 412.00),
    ('south', NOW() - INTERVAL 1 HOUR, 312.80, 45.60, 389.50),
    ('east', NOW() - INTERVAL 1 HOUR, 198.30, 112.40, 356.20),
    ('west', NOW() - INTERVAL 1 HOUR, 278.90, 67.80, 445.70);

FLUSH PRIVILEGES;
EOF

# Configure MySQL to listen on all interfaces
sed -i 's/^bind-address\s*=.*/bind-address = 0.0.0.0/' /etc/mysql/mysql.conf.d/mysqld.cnf
# If bind-address is not present, add it
grep -q '^bind-address' /etc/mysql/mysql.conf.d/mysqld.cnf || echo 'bind-address = 0.0.0.0' >> /etc/mysql/mysql.conf.d/mysqld.cnf
systemctl restart mysql

echo "[+] MySQL configured (anonymous access enabled)"

# ===============================
# APACHE + PHP (Energy Heatmap)
# ===============================
echo "[*] Installing Apache and PHP..."

# Copy Energy Heatmap application
cp -Rf /opt/sunspire/apps/energy-heatmap /var/www/html/
rm -rf /var/www/html/data
mv /var/www/html/energy-heatmap/* /var/www/html/
rm -rf /var/www/html/energy-heatmap
rm -f /var/www/html/index.html
rm -f /var/www/html/README.md

# Set permissions
chown -R www-data:www-data /var/www/html
chmod -R 755 /var/www/html

# Enable Apache
systemctl enable apache2
systemctl restart apache2

echo "[+] Energy Heatmap installed"

# ===============================
# WINDMILLED API (Privesc - Pickle Deserialization)
# ===============================
echo "[*] Installing Windmilled API..."

# Copy Windmilled to /root (runs as root - vulnerable!)
cp -Rf /opt/sunspire/apps/windmilled /root/
rm -f /root/windmilled/README.md

# Install dependencies using venv
cd /root/windmilled
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate

# Install systemd service
cp windmilled.service /etc/systemd/system/

# Update service to use venv
sed -i 's|ExecStart=.*python3|ExecStart=/root/windmilled/venv/bin/python3|' /etc/systemd/system/windmilled.service

systemctl daemon-reload
systemctl enable windmilled
systemctl start windmilled

cd -

echo "[+] Windmilled API installed (runs as root on 127.0.0.1:5000)"

# ===============================
# LATERAL MOVEMENT ARTIFACTS
# ===============================
echo "[*] Setting up lateral movement artifacts..."

# Add crucible root hash to root's .bashrc (discoverable after privesc)
cat >> /root/.bashrc << 'EOF'

# TODO: Remove this - temporary note for crucible server rebuild
# crucible root hash: ec75b28fe9581b2921669e223875138a
# Generated for emergency access, need to update to: Fj9kL2mN
EOF

echo "[+] Lateral movement artifacts created"

# ===============================
# SCORING FILES
# ===============================
echo "[*] Creating scoring control files..."

echo "" > /home/inspire/ctrl.txt
chown inspire:inspire /home/inspire/ctrl.txt
chmod 644 /home/inspire/ctrl.txt

echo "" > /root/ctrl.txt
chmod 644 /root/ctrl.txt

echo "[+] Control files created"

# ===============================
# FINAL SETUP
# ===============================
echo "[*] Final configuration..."

# Ensure services are running
systemctl restart sshd
systemctl restart mysql
systemctl restart apache2
systemctl restart windmilled

echo ""
echo "==============================="
echo " INSPIRE DEPLOYMENT COMPLETE  "
echo "==============================="
echo ""
echo "Services:"
echo "  - SSH (OpenSSH Server on :22)"
echo "  - HTTP (Apache + Energy Heatmap on :80)"
echo "  - MySQL (MySQL Server on :3306 - anonymous access!)"
echo "  - API (Windmilled on 127.0.0.1:5000 - internal only)"
echo ""
echo "Users:"
echo "  - inspire:aN8ivVL3"
echo "  - ops:9ksP311p"
echo "  - root:Mc8HYoDw"
echo ""
echo "Attack Vectors:"
echo "  - Initial Access: MySQL anonymous login → system_config table → inspire password"
echo "  - Initial Access: SSH as inspire with discovered password"
echo "  - Privesc: Energy Heatmap api.php → jq command injection (runs as www-data)"
echo "  - Privesc: Windmilled /api/config/import → pickle deserialization (runs as root)"
echo ""
echo "Scoring:"
echo "  - Services: Apache, MySQL, SSH"
echo "  - Files: /home/inspire/ctrl.txt, /root/ctrl.txt"
echo ""
echo "Lateral Movement:"
echo "  - inspire → forge: SSH key in /root/windmilled/dev_notes.txt"
echo "  - inspire → crucible: Root password hint in /root/.bashrc"
echo ""
