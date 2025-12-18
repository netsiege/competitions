# Maintenance Script
# Runs every 5 minutes via scheduled task
# Last updated: 2024-06-15

Write-Host "[$(Get-Date)] Running scheduled maintenance..."

# Clean temp files older than 7 days
$TempPath = "C:\Windows\Temp"
$CutoffDate = (Get-Date).AddDays(-7)

Get-ChildItem -Path $TempPath -Recurse -ErrorAction SilentlyContinue | 
    Where-Object { $_.LastWriteTime -lt $CutoffDate } | 
    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue

# Log rotation
$LogPath = "C:\Logs"
if (Test-Path $LogPath) {
    Get-ChildItem -Path $LogPath -Filter "*.log" -ErrorAction SilentlyContinue |
        Where-Object { $_.LastWriteTime -lt $CutoffDate } |
        Remove-Item -Force -ErrorAction SilentlyContinue
}

Write-Host "[$(Get-Date)] Maintenance complete."
