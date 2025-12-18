<?php
/**
 * Database configuration for Energy Heatmap
 * Used for historical data storage
 */

define('DB_HOST', 'localhost');
define('DB_USER', 'inspire');
define('DB_PASS', 'aN8ivVL3');
define('DB_NAME', 'sunspire_energy');

function getDbConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    if ($conn->connect_error) {
        error_log("Database connection failed: " . $conn->connect_error);
        return null;
    }
    
    return $conn;
}
?>
