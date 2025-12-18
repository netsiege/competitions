# Energy Heatmap - Sunspire

Real-time energy consumption monitoring dashboard for Sunspire infrastructure.

## Deployment

```bash
# Install dependencies
apt-get install -y apache2 php libapache2-mod-php jq

# Copy files to webroot
cp -Rf energy-heatmap/* /var/www/html/

# Set permissions
chown -R www-data:www-data /var/www/html
chmod -R 755 /var/www/html

# Restart Apache
systemctl restart apache2
```

## Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Main dashboard |
| `/api.php?action=stats` | Get all energy data |
| `/api.php?action=filter&region=<region>` | Filter by region |
| `/api.php?action=filter&source=<source>` | Filter by energy source |
| `/api.php?action=zones` | List all zones |

## Regions

- `north` - Northern facilities
- `south` - Southern facilities  
- `east` - Eastern facilities
- `west` - Western facilities
- `central` - Central HQ

## Energy Sources

- `solar` - Solar panel arrays
- `wind` - Wind turbines
- `thermal` - Thermal generators
- `grid` - Grid storage/batteries

## Requirements

- Apache2 with PHP
- jq (JSON processor)
- Port 80
