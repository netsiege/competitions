#!/bin/bash

# Function to fetch files for a specific IP range and password
fetch_group() {
    local start_ip_end=$1
    local end_ip_end=$2
    local password=$3
    local user="kali"
    local file=".full_research_history.csv"

    for (( i=$start_ip_end; i<=$end_ip_end; i++ )); do
        local ip="10.100.7.$i"
        
        echo "Processing $ip..."
        
        # Make the necessary directory locally
        mkdir -p "./$ip"
        
        # Use sshpass to SCP the file
        # Note: StrictHostKeyChecking=no prevents hanging on new SSH connections
		ssh-keygen -R "$ip"
        sshpass -p "$password" scp -o StrictHostKeyChecking=no "$user@$ip:~/$file" "./$ip/$file"
        
        # Simple error checking
        if [ $? -eq 0 ]; then
            echo "  [+] Successfully downloaded from $ip"
        else
            echo "  [-] Failed to download from $ip"
        fi
    done
    echo "----------------------------------------"
}

echo "Starting file retrieval..."
echo "----------------------------------------"

# Group 1 (IPs: 10.100.7.11-14)
fetch_group 11 14 "6pMAUz1N"

# Group 2 (IPs: 10.100.7.21-24)
fetch_group 21 24 "dFMVxYA4"

# Group 3 (IPs: 10.100.7.31-34)
fetch_group 31 34 "PhF7ffPZ"

echo "All transfers complete."
