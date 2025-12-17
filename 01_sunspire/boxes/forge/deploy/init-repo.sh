#!/bin/bash
#
# Initialize Git Repository with Password Leak in History
# This script creates a fake manufacturing logs repository where
# the forge user password was accidentally committed then removed.
#

set -e

REPO_NAME="forge-logs"
GIT_DIR="/var/lib/git"
BARE_REPO="${GIT_DIR}/${REPO_NAME}.git"
TEMP_DIR=$(mktemp -d)

echo "[*] Creating git repository with password leak history..."

# ===============================
# SETUP TEMP WORKING REPO
# ===============================

cd "$TEMP_DIR"
git init
git config user.email "mason@sunspire.local"
git config user.name "mason"

# ===============================
# COMMIT 1: Initial manufacturing logs
# ===============================

mkdir -p logs

cat > logs/production.log << 'EOF'
[2024-12-01 06:15:23] Production line 1 started - Batch FORGE-2024-1180
[2024-12-01 06:18:45] Silicon wafer loading complete - 500 units
[2024-12-01 07:22:11] Cell assembly phase 1 complete
[2024-12-01 08:45:33] Quality check passed - 498/500 units
[2024-12-01 09:12:00] Batch FORGE-2024-1180 complete
[2024-12-01 10:00:15] Production line 1 started - Batch FORGE-2024-1181
[2024-12-01 10:03:22] Silicon wafer loading complete - 500 units
[2024-12-01 11:15:44] Cell assembly phase 1 complete
[2024-12-01 12:30:00] Lunch break - line paused
[2024-12-01 13:00:00] Production resumed
[2024-12-01 14:22:18] Quality check passed - 500/500 units
[2024-12-01 15:00:00] Batch FORGE-2024-1181 complete
EOF

cat > logs/maintenance.log << 'EOF'
[2024-12-02 05:00:00] Scheduled maintenance window opened
[2024-12-02 05:15:00] CNC Bay 1 - Spindle lubrication complete
[2024-12-02 05:30:00] Assembly Line 2 - Belt tension adjusted
[2024-12-02 06:00:00] Lamination Chamber 1 - Heating element inspection OK
[2024-12-02 06:30:00] Soldering Bay 3 - Tip replacement complete
[2024-12-02 07:00:00] All stations passed pre-shift inspection
[2024-12-02 07:15:00] Maintenance window closed
EOF

cat > logs/quality.log << 'EOF'
[2024-12-01] QC Report - Batch FORGE-2024-1180
  Total Units: 500
  Passed: 498
  Failed: 2
  Defect Types: Micro-crack (1), Busbar misalignment (1)
  Yield: 99.6%

[2024-12-01] QC Report - Batch FORGE-2024-1181  
  Total Units: 500
  Passed: 500
  Failed: 0
  Yield: 100%

[2024-12-02] QC Report - Batch FORGE-2024-1182
  Total Units: 750
  Passed: 748
  Failed: 2
  Defect Types: EVA bubble (1), Frame scratch (1)
  Yield: 99.7%
EOF

git add .
git commit -m "Initial commit - manufacturing logs"

# ===============================
# COMMIT 2: Add config with password (THE LEAK)
# ===============================

mkdir -p config

cat > config/system.conf << 'EOF'
# Forge Manufacturing System Configuration
# Last updated: 2024-12-05 by mason

[database]
host = localhost
port = 3306
name = forge_manufacturing

[api]
port = 4000
debug = false

[authentication]
# TODO: Move these to environment variables
FORGE_USER=forge
FORGE_USER_PASSWORD=h1ewFWZG

[logging]
level = INFO
path = /var/log/forge

[backup]
enabled = true
schedule = 0 2 * * *
destination = /var/backups/forge
EOF

git add .
git commit -m "Add system configuration backup"

# ===============================
# COMMIT 3: Remove sensitive config
# ===============================

rm -rf config/

git add .
git commit -m "Remove sensitive config - should not be in repo"

# ===============================
# COMMIT 4: Update logs
# ===============================

cat >> logs/production.log << 'EOF'
[2024-12-10 06:00:00] Production line 1 started - Batch FORGE-2024-1220
[2024-12-10 06:05:12] Silicon wafer loading complete - 600 units
[2024-12-10 07:30:45] Cell assembly phase 1 complete
[2024-12-10 08:45:00] Cell assembly phase 2 complete
[2024-12-10 10:00:33] Quality check passed - 597/600 units
[2024-12-10 10:30:00] Batch FORGE-2024-1220 complete
[2024-12-15 06:00:00] Production line 1 started - Batch FORGE-2024-1245
[2024-12-15 06:08:22] Silicon wafer loading complete - 500 units
[2024-12-15 07:45:11] Cell assembly phase 1 complete
[2024-12-15 09:00:00] Quality check in progress
EOF

cat >> logs/maintenance.log << 'EOF'
[2024-12-09 05:00:00] Weekly maintenance window
[2024-12-09 05:20:00] Assembly Line 4 - Conveyor motor replaced
[2024-12-09 06:00:00] QC Station 1 - Calibration complete
[2024-12-09 06:30:00] All systems operational
[2024-12-16 05:00:00] Scheduled maintenance window
[2024-12-16 05:15:00] Cutting Station A - Blade replacement
[2024-12-16 06:00:00] Pre-shift inspection complete
EOF

git add .
git commit -m "Update logs - December batch"

# ===============================
# COMMIT 5: Add .gitignore
# ===============================

cat > .gitignore << 'EOF'
# Configuration files - DO NOT COMMIT
config/
*.conf
*.env

# Temporary files
*.tmp
*.bak

# IDE
.vscode/
.idea/
EOF

git add .
git commit -m "Add .gitignore for config files"

# ===============================
# CREATE BARE REPO FOR HTTP SERVING
# ===============================

echo "[*] Creating bare repository at ${BARE_REPO}..."

mkdir -p "$GIT_DIR"
git clone --bare "$TEMP_DIR" "$BARE_REPO"

# Required for dumb HTTP protocol
cd "$BARE_REPO"
git update-server-info

# Enable post-update hook for future updates
if [ -f hooks/post-update.sample ]; then
    mv hooks/post-update.sample hooks/post-update
    chmod +x hooks/post-update
fi

# Set ownership for web server
chown -R www-data:www-data "$BARE_REPO"

# Cleanup
rm -rf "$TEMP_DIR"

echo "[+] Git repository created successfully"
echo ""
echo "Repository: ${BARE_REPO}"
echo "Clone URL:  http://<server_ip>/git/${REPO_NAME}.git"
echo ""
echo "To find the leaked password:"
echo "  git clone http://<server_ip>/git/${REPO_NAME}.git"
echo "  cd ${REPO_NAME}"
echo "  git log -p"
echo "  # Look for 'Remove sensitive config' commit"
