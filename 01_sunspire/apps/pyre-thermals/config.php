<?php
/**
 * PyreWatch - Database Configuration
 * Sunspire Thermal Monitoring System
 * 
 * WARNING: This file contains sensitive credentials.
 * Do not expose to unauthorized personnel.
 * Developed by Axel (software steward @ sunspire)
 */

define('DB_HOST', 'localhost');
define('DB_NAME', 'pyrewatch');
define('DB_USER', 'pyre');
define('DB_PASS', 'h1ewFWZG');

// Database connection
function getDbConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    if ($conn->connect_error) {
        die("Database connection failed: " . $conn->connect_error);
    }
    
    return $conn;
}

// Site configuration
define('SITE_NAME', 'PyreWatch');
define('SITE_VERSION', '15.5.0');
define('ALERT_EMAIL', 'thermal-alerts@sunspire.local');

// Temperature thresholds (Celsius)
define('TEMP_WARNING', 70);
define('TEMP_CRITICAL', 85);
define('TEMP_EMERGENCY', 95);
?>
