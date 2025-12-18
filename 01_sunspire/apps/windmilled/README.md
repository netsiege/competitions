# Windmilled - Wind Turbine Configuration Manager

Internal API for managing Sunspire's wind turbine network.

## Deployment

```bash
# Copy to /root/windmilled
cp -Rf windmilled /root/

# Install dependencies
pip3 install -r /root/windmilled/requirements.txt

# Install and enable service
cp /root/windmilled/windmilled.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable windmilled
systemctl start windmilled
```

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API index |
| `/api/turbines` | GET | List all turbines |
| `/api/turbines/<id>` | GET | Get turbine details |
| `/api/status` | GET | System status |
| `/api/maintenance` | GET | Maintenance schedule |
| `/api/config/export` | GET | Export configuration |
| `/api/config/import` | POST | Import configuration |

## Configuration Import/Export

Export current configuration:
```bash
curl http://127.0.0.1:5000/api/config/export
```

Import configuration:
```bash
curl -X POST http://127.0.0.1:5000/api/config/import \
  -H "Content-Type: application/json" \
  -d '{"config": "<base64-encoded-data>"}'
```

## Port

Listens on **127.0.0.1:5000** (localhost only - internal use).

## Notes

- Runs as root for access to system configuration files
- Do not expose to external network
- Configuration uses pickle serialization for full Python object support
