# PyreWatch - Thermal Monitoring System

Sunspire's thermal safety monitoring dashboard for solar panel infrastructure.

## Overview

PyreWatch monitors temperature data across all solar panel installations, providing:
- Real-time thermal status
- Alert management
- Cooling system monitoring
- Historical data analysis

## Requirements

- Apache2 with PHP 7.4+
- MySQL 5.7+ or MariaDB
- PHP MySQL extension

## Installation

1. Copy files to webroot:
```bash
cp -r pyre-thermals/* /var/www/html/
```

2. Import database schema:
```bash
mysql -u root -p < schema.sql
```

3. Configure MySQL for file writes (required for export features):
```bash
# In /etc/mysql/mysql.conf.d/mysqld.cnf
# Set: secure_file_priv = ""
```

4. Restart MySQL:
```bash
systemctl restart mysql
```

## Database Credentials

- **User**: pyre
- **Password**: h1ewFWZG
- **Database**: pyrewatch

## Files

| File | Description |
|------|-------------|
| index.php | Main dashboard |
| panels.php | Panel details and search |
| alerts.php | Alert management |
| config.php | Database configuration |
| style.css | Styling |
| schema.sql | Database setup |

## Security Notice

⚠️ **FOR CTF USE ONLY** - This application contains intentional vulnerabilities:

- SQL Injection in panels.php (id parameter)
- MySQL FILE privilege allows writing to disk
- Credentials stored in plaintext config

Do not deploy in production environments.

## Vulnerability Details

### SQL Injection → Webshell

The `panels.php` file accepts unsanitized input:

```
panels.php?id=1 UNION SELECT 1,2,3,4,5,6,7,8 INTO OUTFILE '/var/www/html/shell.php'
```

With `secure_file_priv = ""` and FILE privilege, attackers can write PHP shells to webroot.
