#Requires -RunAsAdministrator
# ===============================
# ORBITAL DEPLOYMENT SCRIPT
# ===============================
# Windows Server 2022
# Orbital is a Windows file processing and scheduling server used by Sunspire's computing operations team.

Write-Host "===============================" -ForegroundColor Yellow
Write-Host "          ORBITAL             " -ForegroundColor Yellow
Write-Host "===============================" -ForegroundColor Yellow
Write-Host "Orbital is a Windows file processing and scheduling server used by Sunspire's operations team."

# ===============================
# USER CREATION
# ===============================
Write-Host "[*] Creating users..." -ForegroundColor Cyan

# allow weak passwords by modifying local security policy
secedit /export /cfg C:\secpol.cfg
(Get-Content C:\secpol.cfg) -replace 'PasswordComplexity = 1', 'PasswordComplexity = 0' `
                            -replace 'MinimumPasswordLength = \d+', 'MinimumPasswordLength = 0' | Set-Content C:\secpol.cfg
secedit /configure /db $env:windir\security\local.sdb /cfg C:\secpol.cfg /areas SECURITYPOLICY
gpupdate /force
Remove-Item C:\secpol.cfg -Force

# Create orbital user
$orbitalPassword = ConvertTo-SecureString "securepassword" -AsPlainText -Force
New-LocalUser -Name "orbital" -Password $orbitalPassword -Description "Orbital User" -PasswordNeverExpires
$user = Get-LocalUser -Name "orbital" # when creating users with the same name as the hostname, need to use the user object
Add-LocalGroupMember -Group "Users" -Member $user
Add-LocalGroupMember -Group "Remote Desktop Users" -Member "orbital"

# Create ops user
$opsPassword = ConvertTo-SecureString "9ksP311p" -AsPlainText -Force
New-LocalUser -Name "ops" -Password $opsPassword -Description "Operations User" -PasswordNeverExpires
Add-LocalGroupMember -Group "Users" -Member "ops"
Add-LocalGroupMember -Group "Remote Desktop Users" -Member "ops"

# Set Administrator password
$adminPassword = ConvertTo-SecureString "5EVB7Zmp" -AsPlainText -Force
Set-LocalUser -Name "Administrator" -Password $adminPassword

Write-Host "[+] Users created" -ForegroundColor Green

# ===============================
# SMB ANONYMOUS SHARE (with MD5 hashes)
# ===============================
Write-Host "[*] Configuring SMB share..." -ForegroundColor Cyan

# Create share directory
$sharePath = "C:\Shares\public"

# Create SMB share with anonymous access
New-SmbShare -Name "public" -Path $sharePath -FullAccess "Everyone" -Description "Public Share" | Out-Null

# Configure SMB to allow guest access and disable security signatures
Set-SmbClientConfiguration -EnableInsecureGuestLogons $true -Force
Set-SmbClientConfiguration -RequireSecuritySignature $false -Force

# Make share directory is set so that Everyone has full control
$Acl = Get-Acl $sharePath
$Ar = New-Object System.Security.AccessControl.FileSystemAccessRule("Everyone", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
$Acl.SetAccessRule($Ar)
Set-Acl $sharePath $Acl

# Enable guest account and set to never expire
Set-LocalUser -Name "Guest" -AccountNeverExpires $true
Enable-LocalUser -Name "Guest"

# Enable guest access for SMB
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" -Name "AllowInsecureGuestAuth" -Value 1 -Type DWord

# Export policy
secedit /export /cfg C:\sec_smb.cfg
# Modify policy to allow anonymous access and enumeration
(Get-Content C:\sec_smb.cfg) -replace 'EveryoneIncludesAnonymous = 0', 'EveryoneIncludesAnonymous = 1' `
                            -replace 'RestrictAnonymous = 1', 'RestrictAnonymous = 0' | Set-Content C:\sec_smb.cfg
# Re-import and update
secedit /configure /db $env:windir\security\local.sdb /cfg C:\sec_smb.cfg /areas SECURITYPOLICY
gpupdate /force
Remove-Item C:\sec_smb.cfg


New-Item -ItemType Directory -Path $sharePath -Force | Out-Null

# Create MD5 hashes file (one hash is for orbital user password)
$hashContent = @"
# System Password Hashes - DO NOT SHARE
# Generated for disaster recovery purposes
# For questions please contact Fern (systems steward @ Sunspire)

b0439fae31f8cbba6294af86234d5a28
6d7fce9fee471194aa8b5b6e47267f03
e99a18c428cb38d5f260853678922e03
d8578edf8458ce06fbc5bb76a58c5ca4
"@
Set-Content -Path "$sharePath\hashes.txt" -Value $hashContent -Force

# Create some dummy files
Set-Content -Path "$sharePath\readme.txt" -Value "Orbital File Server - Public Share" -Force
Set-Content -Path "$sharePath\maintenance.log" -Value "Last maintenance: 2025-01-15`nNext scheduled: 2025-02-15" -Force


Write-Host "[+] SMB share configured" -ForegroundColor Green

# ===============================
# SUNSPIRE BACKUP AGENT (Unquoted Service Path)
# ===============================
Write-Host "[*] Installing Sunspire Backup Agent..." -ForegroundColor Cyan

# Create directory with space in name (for unquoted path vulnerability)
$backupDir = "C:\Program Files\Sunspire Backup"
New-Item -ItemType Directory -Path $backupDir -Force | Out-Null

# Copy the backup agent executable
# Note: backup.exe should be pre-compiled from orbital-backup Go project
Copy-Item -Path "..\..\..\apps\orbital-backup\backup.exe" -Destination "$backupDir\backup.exe" -Force -ErrorAction SilentlyContinue

# If backup.exe doesn't exist, create a dummy placeholder
if (-not (Test-Path "$backupDir\backup.exe")) {
    Write-Host "[!] backup.exe not found, creating placeholder..." -ForegroundColor Yellow
    # Create a minimal batch file as placeholder
    Set-Content -Path "$backupDir\backup.bat" -Value "@echo Backup service running" -Force
}

# Register service with UNQUOTED PATH (vulnerability!)
# The path "C:\Program Files\Sunspire Backup\backup.exe" without quotes
# allows hijacking via C:\Program.exe
$serviceName = "SunspireBackup"
$serviceDisplayName = "Sunspire Backup Agent"
$servicePath = "C:\Program Files\Sunspire Backup\backup.exe"

# Use sc.exe to create service with unquoted path
& sc.exe create $serviceName binPath= $servicePath start= auto DisplayName= $serviceDisplayName | Out-Null
& sc.exe description $serviceName "Backs up SMB share contents periodically" | Out-Null

# Make C:\Program Files\Sunspire Backup writable by Users (to allow placing Sunspire.exe)
$acl = Get-Acl "C:\Program Files\Sunspire Backup"
$accessRule = New-Object System.Security.AccessControl.FileSystemAccessRule("Users", "Write", "Allow")
$acl.SetAccessRule($accessRule)
Set-Acl -Path "C:\Program Files\Sunspire Backup" -AclObject $acl -ErrorAction SilentlyContinue
Write-Host "[+] Sunspire Backup Agent installed (unquoted service path)" -ForegroundColor Green

# ===============================
# SCHEDULED TASK (SolarTelemetry - World-Writable Script)
# ===============================
Write-Host "[*] Creating scheduled task..." -ForegroundColor Cyan

# Create Sunspire directory for scripts
$scriptsDir = "C:\Sunspire"
New-Item -ItemType Directory -Path $scriptsDir -Force | Out-Null

# Create the telemetry script
$telemetryScript = @"
# SolarTelemetry - System telemetry collection script
# Runs as SYSTEM to collect performance metrics

`$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
`$logPath = "C:\Sunspire\telemetry.log"

# Collect system info
`$cpu = (Get-WmiObject Win32_Processor).LoadPercentage
`$mem = (Get-WmiObject Win32_OperatingSystem)
`$memUsed = [math]::Round((`$mem.TotalVisibleMemorySize - `$mem.FreePhysicalMemory) / 1MB, 2)

# Log metrics
Add-Content -Path `$logPath -Value "[`$timestamp] CPU: `$cpu% | Memory: `$memUsed GB"
"@
Set-Content -Path "$scriptsDir\telemetry.ps1" -Value $telemetryScript -Force

# Make the script WORLD-WRITABLE (vulnerability!)
$acl = Get-Acl "$scriptsDir\telemetry.ps1"
$accessRule = New-Object System.Security.AccessControl.FileSystemAccessRule("Everyone", "FullControl", "Allow")
$acl.SetAccessRule($accessRule)
Set-Acl -Path "$scriptsDir\telemetry.ps1" -AclObject $acl

# Create scheduled task running as SYSTEM
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-ExecutionPolicy Bypass -File C:\Sunspire\telemetry.ps1"
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 3)
$principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount -RunLevel Highest
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries

Register-ScheduledTask -TaskName "SolarTelemetry" -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Description "Collects system telemetry metrics" | Out-Null

Write-Host "[+] Scheduled task created (world-writable script)" -ForegroundColor Green

# ===============================
# RDP FILE FOR LATERAL MOVEMENT (to helios)
# ===============================
Write-Host "[*] Creating RDP file for lateral movement..." -ForegroundColor Cyan

# Create Documents folder for orbital user
$orbitalDocs = "C:\Users\orbital\Documents"
New-Item -ItemType Directory -Path $orbitalDocs -Force | Out-Null

# Create .rdp file pointing to helios
$rdpContent = @"
password 51:b:6800310065007700460057005a004700
screen mode id:i:1
use multimon:i:0
desktopwidth:i:1920
desktopheight:i:1080
session bpp:i:32
winposstr:s:0,1,0,0,800,600
compression:i:1
keyboardhook:i:2
audiocapturemode:i:0
videoplaybackmode:i:1
connection type:i:7
networkautodetect:i:1
bandwidthautodetect:i:1
displayconnectionbar:i:1
enableworkspacereconnect:i:0
disable wallpaper:i:0
allow font smoothing:i:0
allow desktop composition:i:0
disable full window drag:i:1
disable menu anims:i:1
disable themes:i:0
disable cursor setting:i:0
bitmapcachepersistenable:i:1
full address:s:<HELIOS_IP_ADDRESS>
username:s:pyre
domain:s:
prompt for credentials:i:0
"@
Set-Content -Path "$orbitalDocs\helios-admin.rdp" -Value $rdpContent -Force

# Set ownership to orbital
$acl = Get-Acl $orbitalDocs
$accessRule = New-Object System.Security.AccessControl.FileSystemAccessRule("orbital", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
$acl.SetAccessRule($accessRule)
Set-Acl -Path $orbitalDocs -AclObject $acl

Write-Host "[+] RDP file created for lateral movement" -ForegroundColor Green

# ===============================
# ENABLE RDP
# ===============================
Write-Host "[*] Enabling Remote Desktop..." -ForegroundColor Cyan

# Enable Remote Desktop
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 0

# Disable Network Level Authentication (NLA) for easier access
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name "UserAuthentication" -Value 0

# Enable Remote Desktop firewall rule
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"

# Ensure Remote Desktop Services is running
Set-Service -Name "TermService" -StartupType Automatic
Start-Service -Name "TermService" -ErrorAction SilentlyContinue

Write-Host "[+] Remote Desktop enabled" -ForegroundColor Green

# ===============================
# DISABLE FIREWALL
# ===============================
Write-Host "[*] Disabling firewall..." -ForegroundColor Cyan

# Disable Windows Firewall for all profiles
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False

Write-Host "[+] Firewall disabled" -ForegroundColor Green

# ===============================
# SCORING FILES
# ===============================
Write-Host "[*] Creating scoring control files..." -ForegroundColor Cyan

# Create C:\Administrator directory and ctrl.txt
$adminCtrlPath = "C:\Administrator"
New-Item -ItemType Directory -Path $adminCtrlPath -Force | Out-Null
Set-Content -Path "$adminCtrlPath\ctrl.txt" -Value "" -Force

# Create ctrl.txt for orbital user
$orbitalCtrlPath = "C:\Users\orbital"
New-Item -ItemType Directory -Path $orbitalCtrlPath -Force | Out-Null
Set-Content -Path "$orbitalCtrlPath\ctrl.txt" -Value "" -Force

Write-Host "[+] Control files created" -ForegroundColor Green

# ===============================
# WINDOWS SERVER SETTINGS (Disable for CTF)
# ===============================
Write-Host "[*] Configuring Windows settings for CTF..." -ForegroundColor Cyan

# Disable Windows Defender real-time monitoring (for CTF purposes)
Set-MpPreference -DisableRealtimeMonitoring $true -ErrorAction SilentlyContinue

# Disable Server Manager auto-start
Get-ScheduledTask -TaskName "ServerManager" -ErrorAction SilentlyContinue | Disable-ScheduledTask -ErrorAction SilentlyContinue

Write-Host "[+] Windows settings configured" -ForegroundColor Green

# ===============================
# MSSQL INSTALLATION (PLACEHOLDER)
# ===============================
Write-Host "[*] MSSQL installation..." -ForegroundColor Yellow
Write-Host "[!] MSSQL installation is handled separately - see Install-MSSQL.ps1" -ForegroundColor Yellow

# ===============================
# FINAL SUMMARY
# ===============================
Write-Host ""
Write-Host "===============================" -ForegroundColor Yellow
Write-Host " ORBITAL DEPLOYMENT COMPLETE  " -ForegroundColor Yellow
Write-Host "===============================" -ForegroundColor Yellow
Write-Host ""
Write-Host "Services:" -ForegroundColor Cyan
Write-Host "  - SMB (Anonymous share on :445)"
Write-Host "  - RDP (Remote Desktop on :3389)"
Write-Host "  - MSSQL (Pending - run Install-MSSQL.ps1)"
Write-Host ""
Write-Host "Users:" -ForegroundColor Cyan
Write-Host "  - orbital:securepassword"
Write-Host "  - ops:9ksP311p"
Write-Host "  - Administrator:5EVB7Zmp"
Write-Host ""
Write-Host "Attack Vectors:" -ForegroundColor Cyan
Write-Host "  - Initial Access: Anonymous SMB share with MD5 hashes"
Write-Host "  - Initial Access: MSSQL sa with blank password + xp_cmdshell"
Write-Host "  - Privesc: Scheduled task SolarTelemetry runs world-writable script as SYSTEM"
Write-Host "  - Privesc: Unquoted service path for Sunspire Backup Agent"
Write-Host "  - Lateral Movement: .rdp file to helios in C:\Users\orbital\Documents\"
Write-Host ""
Write-Host "Scoring:" -ForegroundColor Cyan
Write-Host "  - Services: SMB, MSSQL"
Write-Host "  - Files: C:\Administrator\ctrl.txt, C:\Users\orbital\ctrl.txt"
Write-Host ""
