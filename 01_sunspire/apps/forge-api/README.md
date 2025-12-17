# Forge Manufacturing Control API

Component fabrication monitoring and control system for Sunspire's manufacturing facility.

## Deployment

```bash
# Copy to target directory
cp -Rf forge-api /root/

# Install dependencies
pip3 install -r /root/forge-api/requirements.txt

# Install and enable service
cp /root/forge-api/forge-api.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable forge-api
systemctl start forge-api
```

## Endpoints

| Endpoint | Auth | Description |
|----------|------|-------------|
| `/` | No | API index |
| `/api/status` | No | Production status |
| `/api/materials` | No | Materials inventory |
| `/api/jobs` | No | Manufacturing jobs |
| `/api/info` | Yes | System info (restricted) |

## Configuration

Environment variables in `.env`:
- `FORGE_TOKEN` - API authentication token
- `ROOT_PASSWORD` - System root password (for internal use)

## Port

Listens on port **4000** (required for Starfaller SSRF integration).
