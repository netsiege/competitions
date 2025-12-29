# ===============================
#          EMBER
# ===============================
# Forgotten windows server that should have been retired many years ago.
#
# PREREQUISITES:
# - Place PHP zip file in this directory: php.zip
#   Download from: https://windows.php.net/download/ (VS16 x64 Non Thread Safe)
#

Write-Host "==============================="
Write-Host "          EMBER                "
Write-Host "==============================="
Write-Host "Forgotten windows server that should have been retired many years ago."

# ===============================
# USER CREATION
# ===============================
Write-Host "[*] Creating users..."

# Create ember user
$EmberPassword = ConvertTo-SecureString "J4f9juEr" -AsPlainText -Force
New-LocalUser -Name "ember" -Password $EmberPassword -FullName "Ember User" -Description "Legacy admin account" -PasswordNeverExpires -ErrorAction SilentlyContinue
$user = Get-LocalUser -Name "ember" # when creating users with the same name as the hostname, need to use the user object
Add-LocalGroupMember -Group "Remote Desktop Users" -Member $user -ErrorAction SilentlyContinue
Add-LocalGroupMember -Group "Remote Management Users" -Member $user -ErrorAction SilentlyContinue

# Create ops user
$OpsPassword = ConvertTo-SecureString "9ksP311p" -AsPlainText -Force
New-LocalUser -Name "ops" -Password $OpsPassword -FullName "Operations" -Description "Operations account" -PasswordNeverExpires -ErrorAction SilentlyContinue
Add-LocalGroupMember -Group "Remote Desktop Users" -Member "ops" -ErrorAction SilentlyContinue

# Set Administrator password
$AdminPassword = ConvertTo-SecureString "RM1dT8zj" -AsPlainText -Force
Set-LocalUser -Name "Administrator" -Password $AdminPassword

Write-Host "[+] Users created"

# ===============================
# DISABLE FIREWALL
# ===============================
Write-Host "[*] Disabling firewall..."

Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False

Write-Host "[+] Firewall disabled"

# ===============================
# ENABLE RDP
# ===============================
Write-Host "[*] Enabling RDP..."

Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 0
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"

Write-Host "[+] RDP enabled"

# ===============================
# SET ENVIRONMENT VARIABLE (Password Leak)
# ===============================
Write-Host "[*] Setting environment variables..."

# This will be visible in phpinfo()
[System.Environment]::SetEnvironmentVariable("SECRET", "J4f9juEr", "Machine")

Write-Host "[+] Environment variables set"

# ===============================
# INSTALL IIS + PHP
# ===============================
Write-Host "[*] Installing IIS..."

# Install IIS with CGI
Install-WindowsFeature -Name Web-Server, Web-CGI -IncludeManagementTools

Write-Host "[+] IIS installed"

Write-Host "[*] Installing PHP..."

# Create PHP directory
$PhpPath = "C:\PHP"
New-Item -ItemType Directory -Path $PhpPath -Force | Out-Null

# Check for local php.zip first
$PhpZipPath = "C:\sunspire\boxes\ember\deploy\php.zip"
if (-not (Test-Path $PhpZipPath)) {
    # Download PHP from official source if not present
    Write-Host "[*] Downloading PHP 8.1 from official source..."
    $PhpUrl = "https://windows.php.net/downloads/releases/php-8.1.34-nts-Win32-vs16-x64.zip"
    $TempPhpZip = "$env:TEMP\php-latest.zip"
    
    try {
        # Use TLS 1.2 for secure download
        [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12
        Invoke-WebRequest -Uri $PhpUrl -OutFile $TempPhpZip -UseBasicParsing -TimeoutSec 300
        $PhpZipPath = $TempPhpZip
        Write-Host "[+] PHP downloaded successfully"
    } catch {
        Write-Host "[!] Failed to download PHP: $($_.Exception.Message)"
        Write-Host "[!] Attempting alternative download method..."
        try {
            (New-Object System.Net.WebClient).DownloadFile($PhpUrl, $TempPhpZip)
            $PhpZipPath = $TempPhpZip
            Write-Host "[+] PHP downloaded successfully (WebClient)"
        } catch {
            Write-Host "[!] Alternative download also failed: $($_.Exception.Message)"
            $PhpZipPath = $null
        }
    }
}

if ($PhpZipPath -and (Test-Path $PhpZipPath)) {
    try {
        Expand-Archive -Path $PhpZipPath -DestinationPath $PhpPath -Force
        
        # Create php.ini from production template
        if (Test-Path "$PhpPath\php.ini-production") {
            Copy-Item "$PhpPath\php.ini-production" "$PhpPath\php.ini"
        }
        
        # Configure IIS FastCGI for PHP
        if (Test-Path "$PhpPath\php-cgi.exe") {
            # Add PHP handler
            & "$env:windir\system32\inetsrv\appcmd.exe" set config /section:system.webServer/fastCGI "/+[fullPath='$PhpPath\php-cgi.exe']"
            & "$env:windir\system32\inetsrv\appcmd.exe" set config /section:system.webServer/handlers "/+[name='PHP_via_FastCGI',path='*.php',verb='*',modules='FastCgiModule',scriptProcessor='$PhpPath\php-cgi.exe',resourceType='Either']"
            
            # Set index.php as default document
            & "$env:windir\system32\inetsrv\appcmd.exe" set config /section:defaultDocument "/+files.[value='index.php']"
            
            Write-Host "[+] PHP configured with IIS"
        } else {
            Write-Host "[!] php-cgi.exe not found in extracted PHP"
        }
    } catch {
        Write-Host "[!] Error extracting or configuring PHP: $_"
    }
} else {
    Write-Host "[!] PHP zip file not available - PHP will not be configured"
}

# ===============================
# DEPLOY WEBSITE
# ===============================
Write-Host "[*] Deploying website..."

$WebRoot = "C:\inetpub\wwwroot"

# Copy website files
Copy-Item -Path "C:\sunspire\apps\ember-site\index.php" -Destination "$WebRoot\index.php" -Force
Copy-Item -Path "C:\sunspire\apps\ember-site\info.php" -Destination "$WebRoot\info.php" -Force

# Remove default IIS files
Remove-Item -Path "$WebRoot\iisstart.htm" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$WebRoot\iisstart.png" -Force -ErrorAction SilentlyContinue

Write-Host "[+] Website deployed"

# ===============================
# SMB SHARE (Anonymous Writable)
# ===============================
Write-Host "[*] Creating SMB share..."

# Create Scripts directory
$ScriptsPath = "C:\Scripts"
New-Item -ItemType Directory -Path $ScriptsPath -Force | Out-Null

# Copy maintenance script
Copy-Item -Path "C:\sunspire\boxes\ember\deploy\maintenance.ps1" -Destination "$ScriptsPath\maintenance.ps1" -Force

# Create additional dummy scripts to make share look more legitimate
$BackupScript = @'
# Backup Script
# Runs weekly to backup critical files
# Last modified: 2023-08-14

$BackupDest = "D:\Backups"
$Sources = @("C:\inetpub\wwwroot", "C:\Scripts")

foreach ($src in $Sources) {
    if (Test-Path $src) {
        Copy-Item -Path $src -Destination $BackupDest -Recurse -Force
    }
}
Write-Host "Backup completed: $(Get-Date)"
'@
$BackupScript | Out-File -FilePath "$ScriptsPath\backup.ps1" -Encoding UTF8

$CleanupScript = @'
# Cleanup Script  
# Removes old log files
# Schedule: Monthly

$LogPaths = @("C:\Logs", "C:\Windows\Temp", "C:\inetpub\logs")
$DaysOld = 30

foreach ($path in $LogPaths) {
    if (Test-Path $path) {
        Get-ChildItem -Path $path -Recurse -File |
            Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-$DaysOld) } |
            Remove-Item -Force -ErrorAction SilentlyContinue
    }
}
'@
$CleanupScript | Out-File -FilePath "$ScriptsPath\cleanup.ps1" -Encoding UTF8

$HealthCheckScript = @'
# Health Check Script
# Monitors system resources
# Note: Not currently scheduled

$cpu = Get-WmiObject Win32_Processor | Select-Object -ExpandProperty LoadPercentage
$mem = Get-WmiObject Win32_OperatingSystem
$memUsed = [math]::Round(($mem.TotalVisibleMemorySize - $mem.FreePhysicalMemory) / $mem.TotalVisibleMemorySize * 100, 2)

Write-Host "CPU: $cpu%"
Write-Host "Memory: $memUsed%"
'@
$HealthCheckScript | Out-File -FilePath "$ScriptsPath\healthcheck.ps1" -Encoding UTF8

# Create a README
$ReadmeContent = @'
EMBER MAINTENANCE SCRIPTS
=========================

maintenance.ps1 - System maintenance (runs every 5 minutes)
backup.ps1      - Weekly backup script
cleanup.ps1     - Monthly log cleanup
healthcheck.ps1 - Manual health check

Contact IT if you need to modify these scripts.
'@
$ReadmeContent | Out-File -FilePath "$ScriptsPath\README.txt" -Encoding UTF8

# Set NTFS permissions - Everyone Full Control
$Acl = Get-Acl $ScriptsPath
$AccessRule = New-Object System.Security.AccessControl.FileSystemAccessRule("Everyone", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
$Acl.SetAccessRule($AccessRule)
Set-Acl -Path $ScriptsPath -AclObject $Acl

# Create SMB share with anonymous access
New-SmbShare -Name "Scripts" -Path $ScriptsPath -FullAccess "Everyone" -Description "Maintenance scripts" -ErrorAction SilentlyContinue

# Enable anonymous SMB access
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" -Name "RestrictNullSessAccess" -Value 0 -Type DWord

# Allow anonymous access to the share
Grant-SmbShareAccess -Name "Scripts" -AccountName "Anonymous Logon" -AccessRight Full -Force
Grant-SmbShareAccess -Name "Scripts" -AccountName "Everyone" -AccessRight Full -Force

# Add to null session shares
$NullShares = (Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" -Name "NullSessionShares" -ErrorAction SilentlyContinue).NullSessionShares
if ($NullShares) {
    $NullShares = $NullShares + "Scripts"
} else {
    $NullShares = @("Scripts")
}
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" -Name "NullSessionShares" -Value $NullShares -Type MultiString

Write-Host "[+] SMB share created (anonymous access enabled)"

# ===============================
# SCHEDULED TASK (Privesc Vector)
# ===============================
Write-Host "[*] Creating scheduled task..."

# Create scheduled task that runs maintenance.ps1 as SYSTEM every 5 minutes
$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-ExecutionPolicy Bypass -File C:\Scripts\maintenance.ps1"
$Trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 5) -RepetitionDuration (New-TimeSpan -Days 9999)
$Principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount -RunLevel Highest
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

Unregister-ScheduledTask -TaskName "SystemMaintenance" -Confirm:$false -ErrorAction SilentlyContinue
Register-ScheduledTask -TaskName "SystemMaintenance" -Action $Action -Trigger $Trigger -Principal $Principal -Settings $Settings -Description "Automated system maintenance"

Write-Host "[+] Scheduled task created (runs as SYSTEM every 5 minutes)"

# ===============================
# SCORING FILES
# ===============================
Write-Host "[*] Creating scoring control files..."

# Create ctrl.txt for ember user
$EmberCtrl = "C:\Users\ember\ctrl.txt"
# Need to create user profile first by logging in, or create directory manually
New-Item -ItemType Directory -Path "C:\Users\ember" -Force -ErrorAction SilentlyContinue | Out-Null
New-Item -ItemType File -Path $EmberCtrl -Force | Out-Null

# Create ctrl.txt for Administrator
$AdminCtrl = "C:\Users\Administrator\ctrl.txt"
New-Item -ItemType Directory -Path "C:\Users\Administrator" -Force -ErrorAction SilentlyContinue | Out-Null
New-Item -ItemType File -Path $AdminCtrl -Force | Out-Null

Write-Host "[+] Control files created"

# ===============================
# RESTART SERVICES
# ===============================
Write-Host "[*] Restarting services..."

Restart-Service -Name "LanmanServer" -Force
iisreset /restart

Write-Host "[+] Services restarted"

# ===============================
# COMPLETE
# ===============================
Write-Host ""
Write-Host "==============================="
Write-Host "  EMBER DEPLOYMENT COMPLETE    "
Write-Host "==============================="
Write-Host ""
Write-Host "Services:"
Write-Host "  - HTTP (IIS + PHP on :80)"
Write-Host "  - SMB (Anonymous Scripts share)"
Write-Host "  - RDP (:3389)"
Write-Host ""
Write-Host "Users:"
Write-Host "  - ember:J4f9juEr"
Write-Host "  - ops:9ksP311p"
Write-Host "  - Administrator:RM1dT8zj"
Write-Host ""
Write-Host "Attack Vectors:"
Write-Host "  - Initial Access: /info.php leaks SECRET environment variable"
Write-Host "  - Initial Access: Anonymous SMB share \\<ip>\Scripts is writable"
Write-Host "  - Privesc: Replace C:\Scripts\maintenance.ps1 -> runs as SYSTEM every 5 min"
Write-Host ""
Write-Host "Scoring:"
Write-Host "  - Services: Website, SMB"
Write-Host "  - Files: C:\Users\ember\ctrl.txt, C:\Users\Administrator\ctrl.txt"
Write-Host ""
