#Requires -RunAsAdministrator
<#
.SYNOPSIS
    MS SQL Server silent installation script for Orbital CTF box.

.DESCRIPTION
    This script installs MS SQL Server Developer Edition unattended.
    Configures sa account with blank password and enables xp_cmdshell.
    Pre-populates database with solar panel telemetry data.

.NOTES
    Based on: https://github.com/majkinetor/Install-SqlServer
    Modified for CTF deployment with intentional vulnerabilities.
#>

param(
    # Instance name
    [string] $InstanceName = 'MSSQLSERVER',
    
    # Skip data population
    [switch] $SkipData
)

$ErrorActionPreference = 'STOP'
$scriptName = "Install-MSSQL"
$start = Get-Date

Write-Host "===============================" -ForegroundColor Yellow
Write-Host "   MSSQL SERVER INSTALLATION  " -ForegroundColor Yellow
Write-Host "===============================" -ForegroundColor Yellow

# ===============================
# CHECK IF SQL SERVER IS ALREADY INSTALLED
# ===============================
if (Get-Service -Name 'MSSQLSERVER' -ErrorAction SilentlyContinue) {
    Write-Host "[+] SQL Server already installed, skipping installation step" -ForegroundColor Green
} else {
    # ===============================
    # DOWNLOAD ISO
    # ===============================
    $isoUrl = "https://download.microsoft.com/download/7/c/1/7c14e92e-bdcb-4f89-b7cf-93543e7112d1/SQLServer2019-x64-ENU-Dev.iso"
    $saveDir = Join-Path $Env:TEMP $scriptName
    New-Item $saveDir -ItemType Directory -ErrorAction SilentlyContinue | Out-Null
    $IsoPath = Join-Path $saveDir "SQLServer2019-x64-ENU-Dev.iso"
    $minIsoSize = 1500MB  # SQL Server ISO should be ~1.5GB+

    if (Test-Path $IsoPath) {
        $fileSize = (Get-Item $IsoPath).Length
        if ($fileSize -lt $minIsoSize) {
            Write-Host "[!] ISO file appears corrupted (size: $([math]::Round($fileSize/1MB))MB), re-downloading..." -ForegroundColor Yellow
            Dismount-DiskImage -ImagePath $IsoPath -ErrorAction SilentlyContinue
            Remove-Item $IsoPath -Force -ErrorAction SilentlyContinue
        } else {
            Write-Host "[*] ISO already present: $IsoPath" -ForegroundColor Cyan
        }
    }

    if (-not (Test-Path $IsoPath)) {
        Write-Host "[*] Downloading ISO to: $IsoPath" -ForegroundColor Cyan
        Invoke-WebRequest $isoUrl -OutFile $IsoPath -UseBasicParsing
    }

    # ===============================
    # MOUNT ISO
    # ===============================
    Write-Host "[*] Mounting ISO..." -ForegroundColor Cyan

    $mountedImage = Mount-DiskImage $IsoPath -StorageType ISO -PassThru
    $volume = $mountedImage | Get-Volume
    $iso_drive = if ($volume) {
        $volume.DriveLetter + ':'
    } else {
        # Fallback for Windows Sandbox
        Get-PSDrive | Where-Object { $_.Description -like 'sql*' } | Select-Object -ExpandProperty Root
    }

    if (!$iso_drive) { 
        throw "Can't find mounted ISO drive" 
    }

    Write-Host "[+] ISO mounted at: $iso_drive" -ForegroundColor Green

    # ===============================
    # INSTALL SQL SERVER
    # ===============================
    Write-Host "[*] Installing SQL Server..." -ForegroundColor Cyan

    $setupPath = "${iso_drive}setup.exe"
    $arguments = @(
        '/Q'
        '/INDICATEPROGRESS'
        '/IACCEPTSQLSERVERLICENSETERMS'
        '/ACTION=install'
        '/UPDATEENABLED=false'
        '/FEATURES=SQLEngine'
        "/INSTANCENAME=$InstanceName"
        '/SQLSYSADMINACCOUNTS="BUILTIN\Administrators"'
        '/SQLSVCACCOUNT="NT Service\MSSQLSERVER"'
        '/AGTSVCACCOUNT="NT Service\SQLSERVERAGENT"'
        '/SQLSVCSTARTUPTYPE=automatic'
        '/AGTSVCSTARTUPTYPE=automatic'
        '/TCPENABLED=1'
        '/NPENABLED=1'
    )

    Write-Host "[*] Running SQL Server setup..." -ForegroundColor Cyan
    $argString = $arguments -join ' '
    Write-Host "[*] Arguments: $argString" -ForegroundColor Gray
    
    $process = Start-Process -FilePath $setupPath -ArgumentList $arguments -Wait -PassThru -NoNewWindow
    $exitCode = $process.ExitCode

    if ($exitCode -and $exitCode -ne 3010 -and $exitCode -ne 0) {
        throw "SQL Server installation failed, exit code: $exitCode"
    }

    Write-Host "[+] SQL Server installed" -ForegroundColor Green
}

# Wait for services to start and be ready
Write-Host "[*] Waiting for SQL Server services..." -ForegroundColor Cyan
Start-Sleep -Seconds 10

# Ensure SQL Server is running
Get-Service -Name 'MSSQLSERVER' -ErrorAction SilentlyContinue | Start-Service -ErrorAction SilentlyContinue
Get-Service -Name 'SQLSERVERAGENT' -ErrorAction SilentlyContinue | Start-Service -ErrorAction SilentlyContinue

# ===============================
# CONFIGURE SQL SERVER
# ===============================
Write-Host "[*] Configuring SQL Server..." -ForegroundColor Cyan

# Import SQL Server module or use sqlcmd
$sqlcmd = "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\SQLCMD.EXE"
if (-not (Test-Path $sqlcmd)) {
    $sqlcmd = Get-ChildItem "C:\Program Files\Microsoft SQL Server" -Recurse -Filter "sqlcmd.exe" -ErrorAction SilentlyContinue | Select-Object -First 1 -ExpandProperty FullName
}

if (-not $sqlcmd) {
    Write-Host "[!] sqlcmd not found, using osql or alternative..." -ForegroundColor Yellow
    $sqlcmd = "sqlcmd"
}

# SQL commands to configure the server
$sqlConfig = @"
-- Enable Mixed Mode authentication and create sa login with blank password
USE [master]
GO

-- Enable Mixed Mode authentication
EXEC xp_instance_regwrite N'HKEY_LOCAL_MACHINE', N'Software\Microsoft\MSSQLServer\MSSQLServer', N'LoginMode', REG_DWORD, 2
GO

-- Configure sa account (VULNERABILITY!)
-- First set a temporary password, enable, then set to blank
ALTER LOGIN [sa] WITH PASSWORD=N'temp_pass_123'
GO

ALTER LOGIN [sa] ENABLE
GO

-- Now set blank password (SQL Server allows this after enabling with temp password)
ALTER LOGIN [sa] WITH PASSWORD=N''
GO

-- Ensure sa has sysadmin role using sp_addsrvrolemember
EXEC sp_addsrvrolemember @loginame = N'sa', @rolename = N'sysadmin'
GO

-- Enable xp_cmdshell (VULNERABILITY!)
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
EXEC sp_configure 'xp_cmdshell', 1;
RECONFIGURE;

-- Allow remote connections
EXEC sp_configure 'remote access', 1;
RECONFIGURE;
GO
"@

$configFile = "$Env:TEMP\sql_config.sql"
Set-Content -Path $configFile -Value $sqlConfig

Write-Host "[*] Enabling Mixed Mode auth, xp_cmdshell, and configuring sa account..." -ForegroundColor Cyan
& $sqlcmd -S "localhost" -E -i $configFile

# Restart SQL Server for Mixed Mode auth to take effect
Write-Host "[*] Restarting SQL Server to apply authentication mode change..." -ForegroundColor Cyan
Restart-Service -Name 'MSSQLSERVER' -Force
Start-Sleep -Seconds 10

# Ensure sa account is enabled after restart
$enableSa = @"
USE [master]
GO
ALTER LOGIN [sa] ENABLE
GO
ALTER LOGIN [sa] WITH PASSWORD=N'', CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
GO
"@

$enableSaFile = "$Env:TEMP\enable_sa.sql"
Set-Content -Path $enableSaFile -Value $enableSa

Write-Host "[*] Ensuring sa account is enabled..." -ForegroundColor Cyan
& $sqlcmd -S "localhost" -E -i $enableSaFile

Write-Host "[+] SQL Server configured" -ForegroundColor Green

# ===============================
# POPULATE WITH SOLAR PANEL DATA
# ===============================
if (-not $SkipData) {
    Write-Host "[*] Populating database with solar panel data..." -ForegroundColor Cyan
    
    $sqlData = @"
-- Create SunSpire database
CREATE DATABASE SunSpire;
GO

USE SunSpire;
GO

-- Solar Panel Inventory Table
CREATE TABLE SolarPanels (
    PanelID INT PRIMARY KEY IDENTITY(1,1),
    SerialNumber VARCHAR(50),
    Model VARCHAR(100),
    Manufacturer VARCHAR(100),
    InstallDate DATE,
    Location VARCHAR(200),
    Capacity_kW DECIMAL(10,2),
    Status VARCHAR(20)
);

-- Solar Panel Telemetry Table
CREATE TABLE PanelTelemetry (
    TelemetryID INT PRIMARY KEY IDENTITY(1,1),
    PanelID INT,
    Timestamp DATETIME,
    Voltage DECIMAL(10,2),
    Current DECIMAL(10,2),
    Power_W DECIMAL(10,2),
    Temperature_C DECIMAL(5,2),
    Irradiance DECIMAL(10,2),
    Efficiency DECIMAL(5,2)
);

-- Maintenance Records Table
CREATE TABLE MaintenanceLog (
    LogID INT PRIMARY KEY IDENTITY(1,1),
    PanelID INT,
    MaintenanceDate DATE,
    TechnicianName VARCHAR(100),
    Description TEXT,
    Cost DECIMAL(10,2)
);

-- Insert sample solar panels
INSERT INTO SolarPanels (SerialNumber, Model, Manufacturer, InstallDate, Location, Capacity_kW, Status) VALUES
('SP-2024-001', 'SunMax 400W', 'SolarTech Industries', '2024-01-15', 'Roof Section A - North', 0.40, 'Active'),
('SP-2024-002', 'SunMax 400W', 'SolarTech Industries', '2024-01-15', 'Roof Section A - North', 0.40, 'Active'),
('SP-2024-003', 'SunMax 400W', 'SolarTech Industries', '2024-01-15', 'Roof Section A - South', 0.40, 'Active'),
('SP-2024-004', 'HeliosPrime 500W', 'Helios Energy Corp', '2024-02-20', 'Roof Section B - East', 0.50, 'Active'),
('SP-2024-005', 'HeliosPrime 500W', 'Helios Energy Corp', '2024-02-20', 'Roof Section B - East', 0.50, 'Maintenance'),
('SP-2024-006', 'OrbitalSun 450W', 'Orbital Renewables', '2024-03-10', 'Ground Array 1', 0.45, 'Active'),
('SP-2024-007', 'OrbitalSun 450W', 'Orbital Renewables', '2024-03-10', 'Ground Array 1', 0.45, 'Active'),
('SP-2024-008', 'StarLight 380W', 'Starfall Solar Co', '2024-04-05', 'Carport Structure', 0.38, 'Active'),
('SP-2024-009', 'PyreFlame 420W', 'Pyre Energy Systems', '2024-05-12', 'Warehouse Roof', 0.42, 'Offline'),
('SP-2024-010', 'ForgePower 550W', 'Forge Industrial Solar', '2024-06-01', 'Factory Building A', 0.55, 'Active');

-- Insert sample telemetry data
DECLARE @i INT = 1;
DECLARE @panelId INT;
DECLARE @timestamp DATETIME;
DECLARE @voltage DECIMAL(10,2);
DECLARE @current DECIMAL(10,2);
DECLARE @temp DECIMAL(5,2);

WHILE @i <= 100
BEGIN
    SET @panelId = ((@i - 1) % 10) + 1;
    SET @timestamp = DATEADD(HOUR, -@i, GETDATE());
    SET @voltage = 35.0 + (RAND() * 10);
    SET @current = 8.0 + (RAND() * 4);
    SET @temp = 25.0 + (RAND() * 30);
    
    INSERT INTO PanelTelemetry (PanelID, Timestamp, Voltage, Current, Power_W, Temperature_C, Irradiance, Efficiency)
    VALUES (
        @panelId,
        @timestamp,
        @voltage,
        @current,
        @voltage * @current,
        @temp,
        800 + (RAND() * 400),
        18.0 + (RAND() * 4)
    );
    
    SET @i = @i + 1;
END

-- Insert maintenance records
INSERT INTO MaintenanceLog (PanelID, MaintenanceDate, TechnicianName, Description, Cost) VALUES
(5, '2024-11-15', 'John Martinez', 'Replaced inverter connection, cleaned panel surface', 150.00),
(9, '2024-11-20', 'Sarah Chen', 'Panel offline - investigating micro-crack damage', 0.00),
(2, '2024-10-05', 'Mike Johnson', 'Routine cleaning and inspection', 75.00),
(7, '2024-09-18', 'John Martinez', 'Tightened mounting brackets, checked wiring', 50.00),
(1, '2024-08-22', 'Lisa Wong', 'Annual performance evaluation - passed', 100.00);

-- Create view for daily production summary
CREATE VIEW DailyProduction AS
SELECT 
    CAST(Timestamp AS DATE) as ProductionDate,
    SUM(Power_W) / 1000 as TotalEnergy_kWh,
    AVG(Efficiency) as AvgEfficiency,
    COUNT(DISTINCT PanelID) as ActivePanels
FROM PanelTelemetry
GROUP BY CAST(Timestamp AS DATE);
GO

PRINT 'SunSpire database populated with solar panel data';
"@

    $dataFile = "$Env:TEMP\sql_data.sql"
    Set-Content -Path $dataFile -Value $sqlData
    
    & $sqlcmd -S "localhost" -E -i $dataFile
    
    Write-Host "[+] Solar panel data populated" -ForegroundColor Green
}

# ===============================
# CLEANUP
# ===============================
Write-Host "[*] Cleaning up..." -ForegroundColor Cyan

# Dismount ISO
if ($mountedImage) {
    Dismount-DiskImage -ImagePath $mountedImage.ImagePath -ErrorAction SilentlyContinue
} else {
    Dismount-DiskImage $IsoPath -ErrorAction SilentlyContinue
}

# Remove temp SQL files
Remove-Item "$Env:TEMP\sql_config.sql" -Force -ErrorAction SilentlyContinue
Remove-Item "$Env:TEMP\sql_data.sql" -Force -ErrorAction SilentlyContinue

Write-Host "[+] Cleanup complete" -ForegroundColor Green

# ===============================
# FIREWALL (if not already disabled)
# ===============================
Write-Host "[*] Configuring SQL Server firewall rules..." -ForegroundColor Cyan

New-NetFirewallRule -DisplayName "Allow SQL Server" `
                    -Direction Inbound `
                    -Protocol TCP `
                    -LocalPort 1433 `
                    -Action Allow `
                    -Profile Any -ErrorAction SilentlyContinue | Out-Null

Write-Host "[+] Firewall rules configured" -ForegroundColor Green

# ===============================
# FINAL SUMMARY
# ===============================
$elapsed = ((Get-Date) - $start).TotalMinutes

Write-Host ""
Write-Host "===============================" -ForegroundColor Yellow
Write-Host " MSSQL INSTALLATION COMPLETE  " -ForegroundColor Yellow
Write-Host "===============================" -ForegroundColor Yellow
Write-Host ""
Write-Host "Installation time: $([math]::Round($elapsed, 1)) minutes" -ForegroundColor Cyan
Write-Host ""
Write-Host "Configuration:" -ForegroundColor Cyan
Write-Host "  - Instance: $InstanceName"
Write-Host "  - Port: 1433"
Write-Host "  - sa password: (blank)"
Write-Host "  - xp_cmdshell: ENABLED"
Write-Host "  - Database: SunSpire (solar panel data)"
Write-Host ""
Write-Host "Vulnerabilities:" -ForegroundColor Red
Write-Host "  - sa account has BLANK password"
Write-Host "  - xp_cmdshell is ENABLED (allows OS command execution)"
Write-Host ""
Write-Host "Test connection:" -ForegroundColor Cyan
Write-Host "  sqlcmd -S localhost -U sa -P ''"
Write-Host "  EXEC xp_cmdshell 'whoami'"
Write-Host ""
