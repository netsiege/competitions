# Sunspire Ansible Deployment

Ansible playbooks for deploying Sunspire infrastructure.

## Prerequisites

1. **Python packages:**
   ```bash
   pip install ansible pypsrp
   ```

2. **Ansible collections:**
   ```bash
   ansible-galaxy collection install -r requirements.yml
   ```

3. **Create the archive** (from project root):
   ```bash
   tar -czvf sunspire.tar.gz apps/ boxes/ credentials/
   ```

## Usage

### Deploy to all VMs
```bash
cd ansible
ansible-playbook -i inventory.ini deploy.yml
```

### Deploy to specific groups
```bash
# Linux only
ansible-playbook -i inventory.ini deploy.yml --limit linux

# Windows only
ansible-playbook -i inventory.ini deploy.yml --limit windows
```

### Deploy to specific hosts
```bash
ansible-playbook -i inventory.ini deploy.yml --limit solaris,forge
```

### Fetch deployment logs
```bash
ansible-playbook -i inventory.ini fetch-logs.yml
```

Logs are saved to `../deploy-logs/<timestamp>/`

### Resize partitions (Linux only)
```bash
ansible-playbook -i inventory.ini resize-partitions.yml
```

## Inventory

The `inventory.ini` file contains:
- Host IPs matching terraform configuration
- Per-host credentials from deploy scripts
- Connection settings (SSH for Linux, PSRP for Windows)

## Files

| File | Description |
|------|-------------|
| `ansible.cfg` | Ansible configuration |
| `inventory.ini` | Host inventory with credentials |
| `requirements.yml` | Ansible Galaxy requirements |
| `deploy.yml` | Main deployment playbook |
| `fetch-logs.yml` | Log fetching playbook |
| `resize-partitions.yml` | Partition resize playbook |

## How It Works

### Linux Deployment
1. Copies `sunspire.tar.gz` via SSH
2. Extracts to `/opt/sunspire`
3. Runs `deploy.sh` in background with nohup
4. Logs to `/var/log/deploy-<hostname>.log`
5. Cleans up `/opt/sunspire` after completion

### Windows Deployment
1. Copies `sunspire.tar.gz` via PSRP
2. Extracts to `C:\sunspire`
3. Creates a scheduled task to run `deploy.ps1`
4. Logs to `C:\Windows\Temp\deploy-<hostname>.log`
5. Cleans up `C:\sunspire` after completion

## Troubleshooting

### PSRP Connection Issues
Ensure WinRM is enabled on Windows hosts:
```powershell
Enable-PSRemoting -Force
Set-Item WSMan:\localhost\Service\Auth\Basic -Value $true
Set-Item WSMan:\localhost\Service\AllowUnencrypted -Value $true
```

### SSH Connection Issues
The playbook uses `-o StrictHostKeyChecking=no` to bypass host key verification.

### Check connectivity
```bash
# Linux
ansible linux -i inventory.ini -m ping

# Windows
ansible windows -i inventory.ini -m win_ping
```
