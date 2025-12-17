#!/bin/bash
#
# Root cron script - Automated build system
# Runs every 5 minutes to process manufacturing scripts
#

cd /home/forge/manufacturing-scripts

# Check for changes and commit
if [ -n "$(git status --porcelain)" ]; then
    git add .
    git commit -m "Automated build - $(date '+%Y-%m-%d %H:%M:%S')"
fi
