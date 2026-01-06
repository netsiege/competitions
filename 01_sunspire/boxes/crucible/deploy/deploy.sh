#!/bin/bash 

export DEBIAN_FRONTEND=noninteractive

# description
echo "==============================="
echo "          CRUCIBLE             "
echo "==============================="
echo "idk"

# ===============================
# PACKAGE INSTALLATION
# ===============================
echo "[*] Installing packages..."

apt-get update
apt-get install -y openssh-server python3 python3-pip python3-venv build-essential

echo "[+] Packages installed"

# ===============================
# USER CREATION
# ===============================
echo "[*] Creating users..."

# Create forge user
useradd -m -s /bin/bash crucible
echo "crucible:mqD5uv0j" | chpasswd

# Create ops user
useradd -m -s /bin/bash ops
echo "ops:9ksP311p" | chpasswd

# Set root password
echo "root:hawaiirocks" | chpasswd

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

# ===============================
# energy-projections service
# ===============================
echo "[*] Configuring energy-projections service..."

mkdir -p /var/www
cp -Rf /opt/sunspire/apps/energy-projections /var/www/energy-projections
chown -R crucible:crucible /var/www/energy-projections

cd /var/www/energy-projections
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate

cp /var/www/energy-projections/energy-projections.service /etc/systemd/system/energy-projections.service
systemctl daemon-reload
systemctl enable energy-projections
systemctl start energy-projections

cd - 
echo "[+] energy-projections service configured"


# ===============================
# chatbot service
# ===============================
echo "[*] Configuring chatbot service..."

# Copy chatbot source to /tmp and build
CHATBOT_SRC="/opt/sunspire/apps/chatbot"
if [ -d "$CHATBOT_SRC" ]; then
	echo "[+] Found chatbot source at $CHATBOT_SRC"
	mkdir -p /opt/chatbot
	cp -Rf "$CHATBOT_SRC"/* /opt/chatbot/
	chown -R root:root /opt/chatbot
	cd /opt/chatbot || true

	# Build the chatbot (Makefile expects to produce 'chatbot')
	if [ -f Makefile ]; then
		make || true
	else
		# Fallback: try to compile main.c directly
		if [ -f main.c ]; then
			gcc -Wall -Wno-format-security -O2 -o chatbot main.c || true
		fi
	fi

	# Install binary and service
	mkdir -p /opt/chatbot
	if [ -f chatbot ]; then
		chmod 755 chatbot
		cp chatbot /opt/chatbot/chatbot
	fi

	if [ -f chatbot.service ]; then
		cp chatbot.service /etc/systemd/system/chatbot.service
	fi

	systemctl daemon-reload
	systemctl enable chatbot || true
	systemctl start chatbot || true

	cd - >/dev/null || true
	echo "[+] chatbot service configured"
else
	echo "[!] chatbot source not found at $CHATBOT_SRC"
fi

# ===============================
# SCORING FILES
# ===============================
echo "[*] Creating scoring control files..."

echo "" > /home/crucible/ctrl.txt
chown crucible:crucible /home/crucible/ctrl.txt
chmod 644 /home/crucible/ctrl.txt

echo "" > /root/ctrl.txt
chmod 644 /root/ctrl.txt

echo "[+] Control files created"
