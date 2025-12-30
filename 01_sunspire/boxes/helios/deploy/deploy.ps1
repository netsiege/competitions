#Requires -RunAsAdministrator
# ===============================
# HELIOS DEPLOYMENT SCRIPT
# ===============================
# Windows Server 2022
# Helios is a Windows server that is primarily used for administration tasks across the network. Just as how Helios takes his chariot across the sky, this server allows sunspire network stewards to walk across the network.

Write-Host "===============================" -ForegroundColor Yellow
Write-Host "          HELIOS              " -ForegroundColor Yellow
Write-Host "===============================" -ForegroundColor Yellow
Write-Host "Helios is a Windows server that is primarily used for administration tasks across the network. Just as how Helios takes his chariot across the sky, this server allows sunspire network stewards to walk across the network."

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

# Create helios user (weak password)
$heliosPassword = ConvertTo-SecureString "password" -AsPlainText -Force
New-LocalUser -Name "helios" -Password $heliosPassword -Description "Helios User" -PasswordNeverExpires -ErrorAction SilentlyContinue
Add-LocalGroupMember -Group "Users" -Member "helios" -ErrorAction SilentlyContinue
$user = Get-LocalUser -Name "helios" # when creating users with the same name as the hostname, need to use the user object
Add-LocalGroupMember -Group "Remote Desktop Users" -Member $user -ErrorAction SilentlyContinue
Add-LocalGroupMember -Group "Remote Management Users" -Member $user -ErrorAction SilentlyContinue

# Create pyre user (same password as pyre user on pyre server - password reuse)
$pyrePassword = ConvertTo-SecureString "h1ewFWZG" -AsPlainText -Force
New-LocalUser -Name "pyre" -Password $pyrePassword -Description "Pyre User" -PasswordNeverExpires -ErrorAction SilentlyContinue
Add-LocalGroupMember -Group "Users" -Member "pyre" -ErrorAction SilentlyContinue
Add-LocalGroupMember -Group "Remote Desktop Users" -Member "pyre" -ErrorAction SilentlyContinue

# Create ops user
$opsPassword = ConvertTo-SecureString "9ksP311p" -AsPlainText -Force
New-LocalUser -Name "ops" -Password $opsPassword -Description "Operations User" -PasswordNeverExpires -ErrorAction SilentlyContinue
Add-LocalGroupMember -Group "Users" -Member "ops" -ErrorAction SilentlyContinue
Add-LocalGroupMember -Group "Remote Desktop Users" -Member "ops" -ErrorAction SilentlyContinue

# Set Administrator password
$adminPassword = ConvertTo-SecureString "BTw5hYqi" -AsPlainText -Force
Set-LocalUser -Name "Administrator" -Password $adminPassword

Write-Host "[+] Users created" -ForegroundColor Green

# ===============================
# USER PROFILE CREATION (REVIEW)
# ===============================
# NOTE: User profiles are not created until a user logs in for the first time.
# This means C:\Users\helios won't exist until helios logs in.
# The following section attempts to force profile creation by running a process as the user.
# Uncomment if needed:

# Write-Host "[*] Creating user profiles..." -ForegroundColor Cyan
# 
# # Force helios profile creation by running a dummy process
# $heliosCred = New-Object System.Management.Automation.PSCredential("helios", $heliosPassword)
# Start-Process -FilePath "cmd.exe" -ArgumentList "/c echo profile created" -Credential $heliosCred -Wait -NoNewWindow
# 
# # Force pyre profile creation
# $pyreCred = New-Object System.Management.Automation.PSCredential("pyre", $pyrePassword)
# Start-Process -FilePath "cmd.exe" -ArgumentList "/c echo profile created" -Credential $pyreCred -Wait -NoNewWindow
# 
# Write-Host "[+] User profiles created" -ForegroundColor Green

# ===============================
# DISABLE FIREWALL
# ===============================
Write-Host "[*] Disabling firewall..." -ForegroundColor Cyan

# Disable Windows Firewall for all profiles
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False

Write-Host "[+] Firewall disabled" -ForegroundColor Green

# ===============================
# INSTALL IIS, ADD FILES, ENABLE DIRECTORY BROWSING
# ===============================
Write-Host "[*] Installing and configuring IIS..." -ForegroundColor Cyan
# Install IIS
Install-WindowsFeature -Name Web-Server -IncludeManagementTools
# Add files to IIS root
$iisRoot = "C:\inetpub\wwwroot"
Set-Content -Path "$iisRoot\index.html" -Value "<html><body><h1>Welcome to Helios Server</h1><p>This is the default IIS page.</p></body></html>" -Force
Set-Content -Path "$iisRoot\readme.txt" -Value "This is the Helios server IIS web root. Directory browsing is enabled." -Force
Set-Content -Path "$iisRoot\notes.txt" -Value "Note: The helios user has a weak password" -Force
Set-Content -Path "$iisRoot\credentials.txt" -Value "DARKSIDE, Classof07, password, Kassidy, nirvana, babyblue, myspace1" -Force
# enable directory browsing
Write-Host "[*] Enabling directory browsing in IIS..." -ForegroundColor Cyan
Set-WebConfigurationProperty -filter /system.webServer/directoryBrowse -name enabled -value True

# disable default document to force directory listing
Set-WebConfigurationProperty -filter /system.webServer/defaultDocument -name enabled -value False -PSPath "IIS:\Sites\Default Web Site"
Remove-WebConfigurationProperty -filter /system.webServer/defaultDocument/files -name . -atElement @{value="index.html"}

# verify 
$status = Get-WebConfigurationProperty -filter /system.webServer/directoryBrowse -name enabled
Write-Host "Directory Browsing is now set to: $($status.Value)" -ForegroundColor Green

Write-Host "[*] Restarting IIS..." -ForegroundColor Cyan
Reset-IISServerManager
Write-Host "[+] IIS installed and configured" -ForegroundColor Green

# ===============================
# POWERSHELL HISTORY (Privesc Hint)
# ===============================
Write-Host "[*] Planting PowerShell history..." -ForegroundColor Cyan

# Create helios user's PowerShell history directory
# NOTE: This requires the user profile to exist. If profile doesn't exist, create manually.
$heliosHistoryPath = "C:\Users\helios\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine"
New-Item -ItemType Directory -Path $heliosHistoryPath -Force | Out-Null

# Plant fake history containing Administrator password in net user command
$fakeHistory = @"
Get-Process
Get-Service
cd C:\Users\helios\Documents
dir
Get-LocalUser
net user Administrator BTw5hYqi
whoami
exit
"@

$historyFile = Join-Path $heliosHistoryPath "ConsoleHost_history.txt"
Set-Content -Path $historyFile -Value $fakeHistory -Force

Write-Host "[+] PowerShell history planted" -ForegroundColor Green

# ===============================
# ENVIRONMENT VARIABLE (Privesc Hint)
# ===============================
Write-Host "[*] Setting environment variables..." -ForegroundColor Cyan

# Set system-wide environment variable containing Administrator password
# This is a "misconfiguration" - admin password stored in environment variable
[Environment]::SetEnvironmentVariable("ADMIN_BACKUP_KEY", "BTw5hYqi", "Machine")

Write-Host "[+] Environment variables set" -ForegroundColor Green

# ===============================
# SSH KEYS FOR LATERAL MOVEMENT (to starfall)
# ===============================
Write-Host "[*] Configuring SSH keys for lateral movement..." -ForegroundColor Cyan

# Create .ssh directory for helios user
$heliosSshPath = "C:\Users\helios\"
New-Item -ItemType Directory -Path $heliosSshPath -Force | Out-Null

# Copy SSH keys from credentials directory
# These keys can be used to SSH into starfall
Copy-Item -Path "C:\sunspire\credentials\sunspire_key\id_rsa" -Destination "$heliosSshPath\id_rsa" -Force

# Create a readme hint
$sshReadme = @"
# SSH Key for accessing other systems
# Use: ssh -i id_rsa user@<TARGET_HOST>
"@
Set-Content -Path "$heliosSshPath\readme.txt" -Value $sshReadme -Force

Write-Host "[+] SSH keys configured for lateral movement" -ForegroundColor Green

# ===============================
# SCORING FILES
# ===============================
Write-Host "[*] Creating scoring control files..." -ForegroundColor Cyan

# Create C:\Administrator directory and ctrl.txt
$adminCtrlPath = "C:\Users\Administrator"
New-Item -ItemType Directory -Path $adminCtrlPath -Force | Out-Null
Set-Content -Path "$adminCtrlPath\ctrl.txt" -Value "" -Force

# Create ctrl.txt for helios user
$heliosCtrlPath = "C:\Users\helios"
New-Item -ItemType Directory -Path $heliosCtrlPath -Force | Out-Null
Set-Content -Path "$heliosCtrlPath\ctrl.txt" -Value "" -Force

Write-Host "[+] Control files created" -ForegroundColor Green

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
# WINDOWS SERVER HARDENING (Disable for CTF)
# ===============================
Write-Host "[*] Configuring Windows settings for CTF..." -ForegroundColor Cyan

# Disable Windows Defender real-time monitoring (for CTF purposes)
Set-MpPreference -DisableRealtimeMonitoring $true -ErrorAction SilentlyContinue

# Disable Server Manager auto-start
Get-ScheduledTask -TaskName "ServerManager" -ErrorAction SilentlyContinue | Disable-ScheduledTask -ErrorAction SilentlyContinue

Write-Host "[+] Windows settings configured" -ForegroundColor Green

# ===============================
# CLEANUP
# ===============================
Write-Host "[*] Cleaning up..." -ForegroundColor Cyan

# Remove installer
Remove-Item -Path $vncInstaller -Force -ErrorAction SilentlyContinue

Write-Host "[+] Cleanup complete" -ForegroundColor Green

# ===============================
# FINAL SUMMARY
# ===============================
Write-Host ""
Write-Host "===============================" -ForegroundColor Yellow
Write-Host " HELIOS DEPLOYMENT COMPLETE   " -ForegroundColor Yellow
Write-Host "===============================" -ForegroundColor Yellow
Write-Host ""
Write-Host "Services:" -ForegroundColor Cyan
Write-Host "  - VNC (TightVNC on :5900, no authentication)"
Write-Host "  - RDP (Remote Desktop on :3389)"
Write-Host ""
Write-Host "Users:" -ForegroundColor Cyan
Write-Host "  - helios:password (weak/guessable)"
Write-Host "  - pyre:h1ewFWZG (same as pyre server)"
Write-Host "  - ops:9ksP311p"
Write-Host "  - Administrator:BTw5hYqi"
Write-Host ""
Write-Host "Attack Vectors:" -ForegroundColor Cyan
Write-Host "  - Initial Access: Directory browsing"
Write-Host "  - Initial Access: Weak password for helios user"
Write-Host "  - Initial Access: Password reuse (pyre user)"
Write-Host "  - Initial Access: .rdp file from orbital"
Write-Host "  - Privesc: PowerShell history contains 'net user Administrator' command"
Write-Host "  - Privesc: Environment variable ADMIN_BACKUP_KEY contains admin password"
Write-Host "  - Lateral Movement: SSH keys in C:\Users\helios\.ssh\ for starfall"
Write-Host ""
Write-Host "Scoring:" -ForegroundColor Cyan
Write-Host "  - Services: VNC, RDP"
Write-Host "  - Files: C:\Administrator\ctrl.txt, C:\Users\helios\ctrl.txt"
Write-Host ""
