<?php
/**
 * PyreWatch - Panel Details
 * View individual panel thermal data
 * 
 * VULNERABLE: SQL Injection via 'id' parameter
 * Allows INTO OUTFILE for webshell writing
 */

require_once 'config.php';
$conn = getDbConnection();

$panel = null;
$readings = null;
$error = null;

if (isset($_GET['id'])) {
    $id = $_GET['id'];
    
    $query = "SELECT * FROM panels WHERE panel_id = " . $id;
    $result = $conn->query($query);
    
    if ($result && $result->num_rows > 0) {
        $panel = $result->fetch_assoc();
        
        // Get thermal readings history for this panel
        $readings = $conn->query("
            SELECT * FROM thermal_readings 
            WHERE panel_id = " . $id . " 
            ORDER BY timestamp DESC 
            LIMIT 10
        ");
    } else {
        $error = "Panel not found or query error.";
    }
}

// Get all panels for listing
$all_panels = $conn->query("SELECT panel_id, serial_number, location, status, current_temp FROM panels ORDER BY panel_id");
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo SITE_NAME; ?> - Panel Monitor</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-brand">🔥 <?php echo SITE_NAME; ?></div>
        <ul class="nav-links">
            <li><a href="index.php">Dashboard</a></li>
            <li><a href="panels.php" class="active">Panels</a></li>
            <li><a href="alerts.php">Alerts</a></li>
        </ul>
        <div class="nav-info">
            <span class="version">v<?php echo SITE_VERSION; ?></span>
        </div>
    </nav>

    <main class="container">
        <h1>Panel Monitor</h1>

        <!-- Panel Search -->
        <section class="search-panel">
            <h2>🔍 Search Panel</h2>
            <form method="GET" action="panels.php">
                <div class="form-group">
                    <label for="id">Panel ID:</label>
                    <input type="text" name="id" id="id" value="<?php echo isset($_GET['id']) ? htmlspecialchars($_GET['id']) : ''; ?>" placeholder="Enter panel ID">
                    <button type="submit" class="btn">Search</button>
                </div>
            </form>
        </section>

        <?php if ($error): ?>
        <div class="alert alert-error">
            <?php echo htmlspecialchars($error); ?>
        </div>
        <?php endif; ?>

        <?php if ($panel): ?>
        <!-- Panel Details -->
        <section class="panel-details">
            <h2>📊 Panel Details: <?php echo htmlspecialchars($panel['serial_number']); ?></h2>
            <div class="detail-grid">
                <div class="detail-item">
                    <label>Serial Number</label>
                    <span><?php echo htmlspecialchars($panel['serial_number']); ?></span>
                </div>
                <div class="detail-item">
                    <label>Location</label>
                    <span><?php echo htmlspecialchars($panel['location']); ?></span>
                </div>
                <div class="detail-item">
                    <label>Install Date</label>
                    <span><?php echo date('M j, Y', strtotime($panel['install_date'])); ?></span>
                </div>
                <div class="detail-item">
                    <label>Status</label>
                    <span class="badge status-<?php echo $panel['status']; ?>"><?php echo strtoupper($panel['status']); ?></span>
                </div>
                <div class="detail-item highlight">
                    <label>Current Temperature</label>
                    <span class="temp <?php echo $panel['current_temp'] > TEMP_WARNING ? 'warn' : ''; ?><?php echo $panel['current_temp'] > TEMP_CRITICAL ? ' critical' : ''; ?>">
                        <?php echo number_format($panel['current_temp'], 1); ?>°C
                    </span>
                </div>
                <div class="detail-item">
                    <label>Threshold</label>
                    <span><?php echo number_format($panel['threshold_temp'], 1); ?>°C</span>
                </div>
            </div>

            <?php if ($readings && $readings->num_rows > 0): ?>
            <h3>📈 Recent Readings</h3>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>Timestamp</th>
                        <th>Temperature</th>
                        <th>Ambient</th>
                        <th>Irradiance</th>
                    </tr>
                </thead>
                <tbody>
                    <?php while ($reading = $readings->fetch_assoc()): ?>
                    <tr>
                        <td><?php echo date('M j, H:i:s', strtotime($reading['timestamp'])); ?></td>
                        <td class="<?php echo $reading['temperature'] > TEMP_WARNING ? 'warn' : ''; ?>"><?php echo number_format($reading['temperature'], 1); ?>°C</td>
                        <td><?php echo number_format($reading['ambient_temp'], 1); ?>°C</td>
                        <td><?php echo number_format($reading['irradiance'], 1); ?> W/m²</td>
                    </tr>
                    <?php endwhile; ?>
                </tbody>
            </table>
            <?php endif; ?>
        </section>
        <?php endif; ?>

        <!-- All Panels List -->
        <section class="panels-list">
            <h2>📋 All Panels</h2>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Serial</th>
                        <th>Location</th>
                        <th>Status</th>
                        <th>Temperature</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    <?php while ($p = $all_panels->fetch_assoc()): ?>
                    <tr>
                        <td><?php echo $p['panel_id']; ?></td>
                        <td><?php echo htmlspecialchars($p['serial_number']); ?></td>
                        <td><?php echo htmlspecialchars($p['location']); ?></td>
                        <td><span class="badge status-<?php echo $p['status']; ?>"><?php echo strtoupper($p['status']); ?></span></td>
                        <td class="<?php echo $p['current_temp'] > TEMP_WARNING ? 'warn' : ''; ?>"><?php echo number_format($p['current_temp'], 1); ?>°C</td>
                        <td><a href="panels.php?id=<?php echo $p['panel_id']; ?>" class="btn btn-small">View</a></td>
                    </tr>
                    <?php endwhile; ?>
                </tbody>
            </table>
        </section>
    </main>

    <footer>
        <p>PyreWatch Thermal Monitoring System &copy; Sunspire</p>
    </footer>
</body>
</html>
<?php $conn->close(); ?>
