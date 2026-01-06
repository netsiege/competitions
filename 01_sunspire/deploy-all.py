#!/usr/bin/env python3
"""
Deploy sunspire.tar.gz to all VMs defined in terraform/vars.tf and run their deploy scripts.
Usage: 
    python deploy-all.py          # Deploy to all VMs
    python deploy-all.py --logs   # Download deploy logs from all VMs

Requirements:
- Linux VMs: paramiko (pip install paramiko)
- Windows VMs: PsExec must be in PATH (from Sysinternals)
"""

import os
import re
import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime

import paramiko
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient

# Configuration
SCRIPT_DIR = Path(__file__).parent.resolve()
ARCHIVE_NAME = "sunspire.tar.gz"
VARS_TF_PATH = SCRIPT_DIR / "terraform" / "vars.tf"
LOGS_DIR = SCRIPT_DIR / "deploy-logs"

# HTTP server hosting the archive (update this to your server IP:port)
WEB_SERVER = "http://10.100.254.2:8080"
ARCHIVE_URL = f"{WEB_SERVER}/{ARCHIVE_NAME}"

# Credentials - primary password to try first
DEFAULT_PASSWORD = "netsiege123!"
WINDOWS_USER = "Administrator"

# Per-VM passwords extracted from deploy scripts (root/Administrator)
VM_PASSWORDS = {
    # Linux VMs
    "solaris": "Ag9G61RF",
    "starfall": "qi6AJZin",
    "pyre": "791Yz1Py",
    "forge": "7ZjXxjQB",
    "inspire": "Mc8HYoDw",
    "crucible": "hawaiirocks",
    # Windows VMs
    "helios": "BTw5hYqi",
    "orbital": "5EVB7Zmp",
    "ember": "RM1dT8zj",
}
def parse_vars_tf(filepath: Path) -> dict:
    """Parse terraform vars.tf and extract the vms variable as a dict."""
    content = filepath.read_text()
    
    # Find the vms default block
    vms_match = re.search(
        r'variable\s+"vms".*?default\s*=\s*\{(.*?)\n\s*\}(?=\s*\n\})',
        content,
        re.DOTALL
    )
    
    if not vms_match:
        raise ValueError("Could not find 'vms' variable in vars.tf")
    
    vms_block = vms_match.group(1)
    
    # Parse each VM block
    vm_pattern = re.compile(
        r'(\w+)\s*=\s*\{([^}]+)\}',
        re.DOTALL
    )
    
    vms = {}
    for match in vm_pattern.finditer(vms_block):
        vm_name = match.group(1)
        vm_content = match.group(2)
        
        # Parse individual fields
        vm_config = {}
        
        # Extract os_type
        os_match = re.search(r'os_type\s*=\s*"(\w+)"', vm_content)
        if os_match:
            vm_config["os_type"] = os_match.group(1)
        
        # Extract ip_address (strip CIDR notation)
        ip_match = re.search(r'ip_address\s*=\s*"([\d.]+)(?:/\d+)?"', vm_content)
        if ip_match:
            vm_config["ip_address"] = ip_match.group(1)
        
        # Extract cores
        cores_match = re.search(r'cores\s*=\s*(\d+)', vm_content)
        if cores_match:
            vm_config["cores"] = int(cores_match.group(1))
        
        # Extract memory
        memory_match = re.search(r'memory\s*=\s*(\d+)', vm_content)
        if memory_match:
            vm_config["memory"] = int(memory_match.group(1))
        
        # Extract disk_size
        disk_match = re.search(r'disk_size\s*=\s*"([^"]+)"', vm_content)
        if disk_match:
            vm_config["disk_size"] = disk_match.group(1)
        
        # Extract vmid
        vmid_match = re.search(r'vmid\s*=\s*(\d+)', vm_content)
        if vmid_match:
            vm_config["vmid"] = int(vmid_match.group(1))
        
        # Add deployment info based on OS type
        if vm_config.get("os_type") == "linux":
            vm_config["user"] = "root"
            vm_config["deploy_script"] = f"boxes/{vm_name}/deploy/deploy.sh"
        elif vm_config.get("os_type") == "windows":
            vm_config["user"] = "Administrator"
            vm_config["deploy_script"] = f"boxes/{vm_name}/deploy/deploy.ps1"
        
        # Get password from dictionary
        vm_config["password"] = VM_PASSWORDS.get(vm_name, DEFAULT_PASSWORD)
        
        vms[vm_name] = vm_config
    
    return vms


def run_command(cmd: list, description: str, shell: bool = False) -> bool:
    """Run a command and return success status."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300, shell=shell)
        if result.returncode != 0:
            print(f"    Error: {result.stderr.strip() or result.stdout.strip()}")
            return False
        return True
    except subprocess.TimeoutExpired:
        print(f"    Error: Command timed out")
        return False
    except Exception as e:
        print(f"    Error: {e}")
        return False


def ssh_exec(ssh: SSHClient, command: str) -> tuple[bool, str]:
    """Execute a command over SSH and return success status and output."""
    stdin, stdout, stderr = ssh.exec_command(command)
    exit_code = stdout.channel.recv_exit_status()
    output = stdout.read().decode().strip()
    error = stderr.read().decode().strip()
    if exit_code != 0:
        return False, error or output
    return True, output


def deploy_linux(vm_name: str, vm_config: dict) -> bool:
    """Deploy to a Linux VM using paramiko for password auth."""
    ip = vm_config["ip_address"]
    user = vm_config["user"]
    vm_password = vm_config.get("password", DEFAULT_PASSWORD)
    remote_dir = "/opt/sunspire"
    deploy_script = vm_config["deploy_script"]
    
    # Passwords to try: default first, then VM-specific fallback
    passwords_to_try = [DEFAULT_PASSWORD]
    if vm_password != DEFAULT_PASSWORD:
        passwords_to_try.append(vm_password)
    
    try:
        # Connect via SSH with password - try multiple passwords
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        
        print(f"  [1/6] Connecting to {ip}...")
        connected = False
        for pwd in passwords_to_try:
            try:
                ssh.connect(ip, username=user, password=pwd, timeout=30)
                print(f"    Connected with password: {pwd[:3]}***")
                connected = True
                break
            except paramiko.AuthenticationException:
                continue
        
        if not connected:
            print(f"    Error: All passwords failed")
            return False
        
        # Delete old log file if exists
        ssh_exec(ssh, f"rm -f /var/log/deploy-{vm_name}.log")
        
        print(f"  [2/6] Creating remote directory...")
        success, output = ssh_exec(ssh, f"mkdir -p {remote_dir}")
        if not success:
            print(f"    Error: {output}")
            return False
        
        print(f"  [3/6] Downloading {ARCHIVE_NAME} from web server...")
        success, output = ssh_exec(ssh, f"cd {remote_dir} && curl -sO {ARCHIVE_URL} || wget -q {ARCHIVE_URL}")
        if not success:
            print(f"    Error: {output}")
            return False
        
        print(f"  [4/6] Extracting archive...")
        success, output = ssh_exec(ssh, f"cd {remote_dir} && tar -xzf {ARCHIVE_NAME} && rm {ARCHIVE_NAME}")
        if not success:
            print(f"    Error: {output}")
            return False
        
        print(f"  [5/6] Running deploy script in background...")
        # Get the directory containing the deploy script and cd there before running
        deploy_script_dir = f"{remote_dir}/{'/'.join(deploy_script.split('/')[:-1])}"
        deploy_script_name = deploy_script.split('/')[-1]
        # Run deploy script in background with nohup, cleanup after itself
        ssh_exec(ssh, f"cd {remote_dir} && chmod +x {deploy_script} && cd {deploy_script_dir} && nohup bash -c 'bash {deploy_script_name} && rm -rf {remote_dir}' > /var/log/deploy-{vm_name}.log 2>&1 &")
        print(f"    Deploy script started (logs at /var/log/deploy-{vm_name}.log)")
        print(f"  [6/6] Cleanup scheduled after deploy completes" )
        
        ssh.close()
        return True
        
    except Exception as e:
        print(f"    Error: {e}")
        return False


def deploy_windows(vm_name: str, vm_config: dict) -> bool:
    """Deploy to a Windows VM using PsExec."""
    ip = vm_config["ip_address"]
    vm_password = vm_config.get("password", DEFAULT_PASSWORD)
    remote_dir = r"C:\\sunspire"
    deploy_script = vm_config["deploy_script"].replace("/", "\\")
    
    # Passwords to try: default first, then VM-specific fallback
    passwords_to_try = [DEFAULT_PASSWORD]
    if vm_password != DEFAULT_PASSWORD:
        passwords_to_try.append(vm_password)
    
    # Try multiple passwords
    print(f"  [1/5] Connecting and creating remote directory...")
    connected_password = None
    for pwd in passwords_to_try:
        psexec_test = ["psexec.exe", f"\\\\{ip}", "-u", WINDOWS_USER, "-p", pwd, "-accepteula","-i", "cmd", "/c", f"if not exist {remote_dir} mkdir {remote_dir}"]
        if run_command(psexec_test, "Testing connection"):
            print(f"    Connected with password: {pwd[:3]}***")
            connected_password = pwd
            break
    
    if not connected_password:
        print(f"    Error: All passwords failed")
        return False
    
    psexec_base = ["psexec.exe", f"\\\\{ip}", "-u", WINDOWS_USER, "-p", connected_password, "-accepteula", "-i"]
    
    # Delete old log file if exists
    cmd = psexec_base + ["cmd", "/c", f"del /f /q C:\\Windows\\Temp\\deploy-{vm_name}.log 2>nul"]
    run_command(cmd, "Deleting old log")
    
    print(f"  [2/5] Downloading {ARCHIVE_NAME} from web server...")
    cmd = psexec_base + ["powershell", "-Command", f"Invoke-WebRequest -Uri '{ARCHIVE_URL}' -OutFile '{remote_dir}\\{ARCHIVE_NAME}'"]
    if not run_command(cmd, "Downloading archive"):
        return False
    
    print(f"  [3/5] Extracting archive...")
    cmd = psexec_base + ["cmd", "/c", f"cd /d {remote_dir} && tar -xzf {ARCHIVE_NAME}"]
    if not run_command(cmd, "Extracting"):
        return False
    
    print(f"  [4/5] Running deploy script in background...")
    # Get the directory containing the deploy script and cd there before running
    deploy_script_path = f"{remote_dir}\\{deploy_script}"
    deploy_script_dir = '\\'.join(deploy_script_path.split('\\')[:-1])
    deploy_script_name = deploy_script.split('\\')[-1]
    
    # Create a wrapper script that runs the deploy and cleans up
    wrapper_script = f"C:\\Windows\\Temp\\deploy-wrapper-{vm_name}.ps1"
    wrapper_content = f"""
Set-ExecutionPolicy Bypass -Scope Process -Force
Set-Location '{deploy_script_dir}'
& '.\\{deploy_script_name}' *> C:\\Windows\\Temp\\deploy-{vm_name}.log
Remove-Item -Recurse -Force '{remote_dir}' -ErrorAction SilentlyContinue
Remove-Item -Force '{wrapper_script}' -ErrorAction SilentlyContinue
"""
    # Write the wrapper script
    cmd = psexec_base + ["powershell", "-Command", f"Set-Content -Path '{wrapper_script}' -Value @'\n{wrapper_content}\n'@"]
    run_command(cmd, "Creating wrapper script")
    
    # Create a scheduled task to run immediately and delete itself
    task_name = f"SunspireDeploy_{vm_name}"
    cmd = psexec_base + ["powershell", "-Command", f"""
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument '-ExecutionPolicy Bypass -File {wrapper_script}'
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddSeconds(5)
$trigger.EndBoundary = (Get-Date).AddHours(1).ToString('s')
$settings = New-ScheduledTaskSettingsSet -DeleteExpiredTaskAfter 00:00:01
Register-ScheduledTask -TaskName '{task_name}' -Action $action -Trigger $trigger -Settings $settings -User 'SYSTEM' -RunLevel Highest -Force
"""]
    run_command(cmd, "Creating scheduled task")
    print(f"    Deploy script scheduled (logs at C:\\Windows\\Temp\\deploy-{vm_name}.log)")
    print(f"  [5/5] Cleanup scheduled after deploy completes")
    
    return True


def fetch_logs_linux(vm_name: str, vm_config: dict, logs_dir: Path) -> bool:
    """Fetch deploy log from a Linux VM."""
    ip = vm_config["ip_address"]
    user = vm_config["user"]
    vm_password = vm_config.get("password", DEFAULT_PASSWORD)
    remote_log = f"/var/log/deploy-{vm_name}.log"
    
    # Passwords to try
    passwords_to_try = [DEFAULT_PASSWORD]
    if vm_password != DEFAULT_PASSWORD:
        passwords_to_try.append(vm_password)
    
    try:
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        
        connected = False
        for pwd in passwords_to_try:
            try:
                ssh.connect(ip, username=user, password=pwd, timeout=30)
                connected = True
                break
            except paramiko.AuthenticationException:
                continue
        
        if not connected:
            print(f"    Error: Authentication failed")
            return False
        
        # Check if log exists
        success, output = ssh_exec(ssh, f"test -f {remote_log} && echo 'exists'")
        if "exists" not in output:
            print(f"    Log file not found: {remote_log}")
            ssh.close()
            return False
        
        # Download log
        local_log = logs_dir / f"{vm_name}.log"
        with SCPClient(ssh.get_transport()) as scp:
            scp.get(remote_log, str(local_log))
        
        print(f"    Downloaded to {local_log}")
        ssh.close()
        return True
        
    except Exception as e:
        print(f"    Error: {e}")
        return False


def fetch_logs_windows(vm_name: str, vm_config: dict, logs_dir: Path) -> bool:
    """Fetch deploy log from a Windows VM."""
    ip = vm_config["ip_address"]
    vm_password = vm_config.get("password", DEFAULT_PASSWORD)
    remote_log = f"C:\\Windows\\Temp\\deploy-{vm_name}.log"
    local_log = logs_dir / f"{vm_name}.log"
    
    # Passwords to try
    passwords_to_try = [DEFAULT_PASSWORD]
    if vm_password != DEFAULT_PASSWORD:
        passwords_to_try.append(vm_password)
    
    # Try to connect and copy file
    for pwd in passwords_to_try:
        # Map network share
        unc_path = f"\\\\{ip}\\C$"
        subprocess.run(f'net use "{unc_path}" /delete /y', shell=True, capture_output=True)
        connect_result = subprocess.run(
            f'net use "{unc_path}" "{pwd}" /user:{WINDOWS_USER} /persistent:no',
            shell=True, capture_output=True, text=True
        )
        
        if connect_result.returncode == 0:
            # Copy log file
            remote_unc = f"\\\\{ip}\\C$\\Windows\\Temp\\deploy-{vm_name}.log"
            copy_result = subprocess.run(
                f'copy /Y "{remote_unc}" "{local_log}"',
                shell=True, capture_output=True, text=True
            )
            
            # Disconnect
            subprocess.run(f'net use "{unc_path}" /delete /y', shell=True, capture_output=True)
            
            if copy_result.returncode == 0:
                print(f"    Downloaded to {local_log}")
                return True
            else:
                print(f"    Log file not found or copy failed")
                return False
    
    print(f"    Error: Authentication failed")
    return False


def fetch_all_logs(vms: dict):
    """Fetch deploy logs from all VMs."""
    # Create logs directory with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    logs_dir = LOGS_DIR / timestamp
    logs_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Downloading logs to: {logs_dir}")
    print()
    
    results = {}
    for vm_name, vm_config in vms.items():
        ip = vm_config["ip_address"]
        os_type = vm_config["os_type"]
        
        print(f"Fetching log from {vm_name} ({ip})...")
        
        try:
            if os_type == "linux":
                success = fetch_logs_linux(vm_name, vm_config, logs_dir)
            elif os_type == "windows":
                success = fetch_logs_windows(vm_name, vm_config, logs_dir)
            else:
                success = False
            
            results[vm_name] = success
        except Exception as e:
            print(f"    Error: {e}")
            results[vm_name] = False
    
    print()
    print("=" * 50)
    print("  Log Fetch Summary")
    print("=" * 50)
    for vm_name, success in results.items():
        status = "OK" if success else "FAILED"
        color = "\033[92m" if success else "\033[91m"
        reset = "\033[0m"
        print(f"  {color}{vm_name}: {status}{reset}")
    
    succeeded = sum(1 for s in results.values() if s)
    print()
    print(f"  {succeeded}/{len(results)} logs downloaded")
    print(f"  Logs saved to: {logs_dir}")
    print("=" * 50)


def main():
    # Check for --logs flag
    fetch_logs_mode = "--logs" in sys.argv
    
    if fetch_logs_mode:
        print("=" * 50)
        print("  Sunspire Log Fetcher")
        print("=" * 50)
        print()
    else:
        print("=" * 50)
        print("  Sunspire Deployment Script")
        print("=" * 50)
        print()
        print(f"Archive URL: {ARCHIVE_URL}")
        print()
    
    # Verify prerequisites
    if not VARS_TF_PATH.exists():
        print(f"ERROR: vars.tf not found at {VARS_TF_PATH}")
        sys.exit(1)
    
    # Parse vars.tf
    print("Parsing terraform/vars.tf...")
    try:
        vms = parse_vars_tf(VARS_TF_PATH)
    except Exception as e:
        print(f"ERROR: Failed to parse vars.tf: {e}")
        sys.exit(1)
    
    print(f"Found {len(vms)} VMs: {', '.join(vms.keys())}")
    print()
    
    # Print parsed config as JSON
    print("Parsed VM Configuration:")
    print("-" * 50)
    print(json.dumps(vms, indent=2))
    print("-" * 50)
    print()
    
    # If --logs mode, fetch logs and exit
    if fetch_logs_mode:
        fetch_all_logs(vms)
        sys.exit(0)
    
    # Deploy to each VM
    results = {}
    for vm_name, vm_config in vms.items():
        ip = vm_config["ip_address"]
        os_type = vm_config["os_type"]
        
        print("-" * 50)
        print(f"Deploying to: {vm_name} ({ip}) [{os_type}]")
        print("-" * 50)
        
        try:
            if os_type == "linux":
                success = deploy_linux(vm_name, vm_config)
                
            elif os_type == "windows":
                success = deploy_windows(vm_name, vm_config)
            else:
                print(f"  Unknown OS type: {os_type}")
                success = False
            
            results[vm_name] = success
            if success:
                print(f"  SUCCESS: {vm_name} deployed!")
            else:
                print(f"  FAILED: {vm_name}")
        except Exception as e:
            print(f"  FAILED: {vm_name} - {e}")
            results[vm_name] = False
        
        print()
    
    # Summary
    print("=" * 50)
    print("  Deployment Summary")
    print("=" * 50)
    for vm_name, success in results.items():
        status = "SUCCESS" if success else "FAILED"
        color_code = "\033[92m" if success else "\033[91m"
        reset = "\033[0m"
        print(f"  {color_code}{vm_name}: {status}{reset}")
    
    succeeded = sum(1 for s in results.values() if s)
    print()
    print(f"  {succeeded}/{len(results)} deployments successful")
    print("=" * 50)
    
    sys.exit(0 if all(results.values()) else 1)


if __name__ == "__main__":
    main()