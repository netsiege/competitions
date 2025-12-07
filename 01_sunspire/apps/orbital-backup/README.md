# SunSpire Backup Agent

A minimal Windows service that backs up SMB share contents to a zip file.

## Build

```powershell
# On Windows
go build -o backup.exe .

# Cross-compile from Linux/macOS
GOOS=windows GOARCH=amd64 go build -o backup.exe .
```

## Usage

```powershell
# Install as Windows service
.\backup.exe install

# Start the service
.\backup.exe start

# Stop the service
.\backup.exe stop

# Uninstall the service
.\backup.exe uninstall
```

## Configuration

| Setting | Value |
|---------|-------|
| Source Directory | `C:\Shares\public` |
| Backup Path | `C:\Program Files\SunSpire Backup\backup.zip` |
| Interval | 300 minutes |

## Service Details

- **Service Name**: SunSpireBackup
- **Display Name**: SunSpire Backup Agent
- **Description**: Backs up SMB share contents periodically

## Vulnerability Note

When installed via the deploy script, this service is registered with an **unquoted service path**, making it vulnerable to privilege escalation:

```
C:\Program Files\SunSpire Backup\backup.exe
```

An attacker can place a malicious `C:\Program.exe` to hijack execution.
