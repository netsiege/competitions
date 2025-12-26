#!/bin/bash

export DEBIAN_FRONTEND=noninteractive

# description
echo "==============================="
echo "           PYRE               "
echo "==============================="
echo "Pyre is Sunspire's thermal management and safety monitoring system. Like a controlled flame, it keeps watch over the heat that powers our infrastructure."

# ===============================
# USER CREATION
# ===============================
echo "[*] Creating users..."

# Create pyre user (same password as forge user - password reuse)
useradd -m -s /bin/bash pyre
echo "pyre:mqD5uv0j" | chpasswd

# Create ops user
useradd -m -s /bin/bash ops
echo "ops:9ksP311p" | chpasswd

# Set root password
echo "root:791Yz1Py" | chpasswd

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
# APACHE + PHP + MYSQL
# ===============================
echo "[*] Installing Apache, PHP, and MySQL..."

# Install packages
apt-get install -y apache2 php php-mysql libapache2-mod-php mysql-server

# Copy webapp to webroot
cp -Rf /opt/sunspire/apps/pyre-thermals/* /var/www/html/
rm -f /var/www/html/index.html  # Remove default Apache page
rm -rf /var/www/html/README.md

# Set permissions
chown -R www-data:www-data /var/www/html
chmod -R 755 /var/www/html

echo "[+] Apache and PHP installed"

# ===============================
# MYSQL CONFIGURATION
# ===============================
echo "[*] Configuring MySQL..."

# Start MySQL service
systemctl start mysql
systemctl enable mysql

# Configure secure_file_priv to allow file writes
# This enables the INTO OUTFILE SQL injection vector
cat >> /etc/mysql/mysql.conf.d/mysqld.cnf << 'EOF'

# Allow MySQL to write files anywhere (for export features)
secure_file_priv = ""
EOF

# Restart MySQL to apply config
systemctl restart mysql

# Import database schema
mysql < /var/www/html/schema.sql

# Remove schema.sql from webroot (don't expose it)
rm -f /var/www/html/schema.sql

echo "[+] MySQL configured"

# ===============================
# APACHE CONFIGURATION
# ===============================
echo "[*] Configuring Apache..."

# Enable Apache and start
systemctl enable apache2
systemctl restart apache2

echo "[+] Apache configured"

# ===============================
# MOTD SCRIPT (World-Writable - Privesc)
# ===============================
echo "[*] Creating MOTD script..."

# Create the MOTD script with ASCII art
cat > /etc/update-motd.d/99-sunspire << 'EOF'
#!/bin/bash
echo ""
echo "  ███████╗██╗   ██╗███╗   ██╗███████╗██████╗ ██╗██████╗ ███████╗"
echo "  ██╔════╝██║   ██║████╗  ██║██╔════╝██╔══██╗██║██╔══██╗██╔════╝"
echo "  ███████╗██║   ██║██╔██╗ ██║███████╗██████╔╝██║██████╔╝█████╗  "
echo "  ╚════██║██║   ██║██║╚██╗██║╚════██║██╔═══╝ ██║██╔══██╗██╔══╝  "
echo "  ███████║╚██████╔╝██║ ╚████║███████║██║     ██║██║  ██║███████╗"
echo "  ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝"
echo ""
echo "  Thermal Monitoring System - PyreWatch v15.5.0"
echo ""
EOF

# Make it executable AND world-writable (vulnerability!)
chmod 777 /etc/update-motd.d/99-sunspire

echo "[+] MOTD script created (world-writable)"

# ===============================
# PYTHON3 CAPABILITY (Privesc)
# ===============================
echo "[*] Setting Python3 capability..."

# Set cap_setuid on python3 binary (allows privilege escalation)
# Need to use realpath since /usr/bin/python3 is a symlink
PYTHON3_REAL=$(realpath /usr/bin/python3)
setcap cap_setuid+ep "$PYTHON3_REAL"

echo "[+] Python3 capability set on $PYTHON3_REAL"

# ===============================
# SCORING FILES
# ===============================
echo "[*] Creating scoring control files..."

echo "" > /home/pyre/ctrl.txt
chown pyre:pyre /home/pyre/ctrl.txt
chmod 644 /home/pyre/ctrl.txt

echo "" > /root/ctrl.txt
chmod 644 /root/ctrl.txt

echo "[+] Control files created"

# ===============================
# FINAL SETUP
# ===============================
echo "[*] Final configuration..."

# Ensure services are running
systemctl restart ssh
systemctl restart apache2
systemctl restart mysql

echo ""
echo "==============================="
echo "   PYRE DEPLOYMENT COMPLETE   "
echo "==============================="
echo ""
echo "Services:"
echo "  - SSH (OpenSSH Server)"
echo "  - HTTP (Apache + PHP on :80)"
echo "  - MySQL (localhost only)"
echo ""
echo "Users:"
echo "  - pyre:h1ewFWZG (same as forge - password reuse)"
echo "  - ops:9ksP311p"
echo "  - root:791Yz1Py"
echo ""
echo "Attack Vectors:"
echo "  - Initial Access: SQLi in panels.php → INTO OUTFILE webshell"
echo "  - Initial Access: Password reuse (pyre = forge)"
echo "  - Privesc: World-writable MOTD script /etc/update-motd.d/99-sunspire"
echo "  - Privesc: Python3 binary has cap_setuid capability"
echo ""
echo "Scoring:"
echo "  - Services: Website, SSH"
echo "  - Files: /home/pyre/ctrl.txt, /root/ctrl.txt"
echo ""
