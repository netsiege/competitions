<?php
/**
 * PyreWatch - Thermal Monitoring Dashboard
 * Main dashboard showing system overview
 */

require_once 'config.php';
$conn = getDbConnection();

// Get panel statistics
$stats = $conn->query("
    SELECT 
        COUNT(*) as total,
        SUM(CASE WHEN status = 'normal' THEN 1 ELSE 0 END) as normal,
        SUM(CASE WHEN status = 'warning' THEN 1 ELSE 0 END) as warning,
        SUM(CASE WHEN status = 'critical' THEN 1 ELSE 0 END) as critical,
        SUM(CASE WHEN status = 'offline' THEN 1 ELSE 0 END) as offline,
        AVG(current_temp) as avg_temp
    FROM panels
")->fetch_assoc();

// Get recent alerts
$alerts = $conn->query("
    SELECT a.*, p.serial_number 
    FROM alerts a 
    JOIN panels p ON a.panel_id = p.panel_id 
    WHERE a.acknowledged = FALSE 
    ORDER BY a.timestamp DESC 
    LIMIT 5
");

// Get cooling system status
$cooling = $conn->query("
    SELECT * FROM cooling_systems ORDER BY status DESC
");
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo SITE_NAME; ?> - Dashboard</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-brand">🔥 <?php echo SITE_NAME; ?></div>
        <ul class="nav-links">
            <li><a href="index.php" class="active">Dashboard</a></li>
            <li><a href="panels.php">Panels</a></li>
            <li><a href="alerts.php">Alerts</a></li>
        </ul>
        <div class="nav-info">
            <span class="version">v<?php echo SITE_VERSION; ?></span>
        </div>
    </nav>

    <main class="container">
        <h1>Thermal Monitoring Dashboard</h1>
        
        <!-- Status Overview -->
        <section class="status-grid">
            <div class="status-card normal">
                <h3>Normal</h3>
                <span class="count"><?php echo $stats['normal']; ?></span>
                <p>panels operating normally</p>
            </div>
            <div class="status-card warning">
                <h3>Warning</h3>
                <span class="count"><?php echo $stats['warning']; ?></span>
                <p>panels need attention</p>
            </div>
            <div class="status-card critical">
                <h3>Critical</h3>
                <span class="count"><?php echo $stats['critical']; ?></span>
                <p>panels require action</p>
            </div>
            <div class="status-card offline">
                <h3>Offline</h3>
                <span class="count"><?php echo $stats['offline']; ?></span>
                <p>panels offline</p>
            </div>
        </section>

        <!-- Average Temperature -->
        <section class="temp-display">
            <h2>System Average Temperature</h2>
            <div class="temp-value <?php echo $stats['avg_temp'] > TEMP_WARNING ? 'warn' : ''; ?>">
                <?php echo number_format($stats['avg_temp'], 1); ?>°C
            </div>
        </section>

        <!-- Recent Alerts -->
        <section class="alerts-panel">
            <h2>⚠️ Active Alerts</h2>
            <?php if ($alerts->num_rows > 0): ?>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>Time</th>
                        <th>Panel</th>
                        <th>Severity</th>
                        <th>Message</th>
                    </tr>
                </thead>
                <tbody>
                    <?php while ($alert = $alerts->fetch_assoc()): ?>
                    <tr class="severity-<?php echo $alert['severity']; ?>">
                        <td><?php echo date('M j, H:i', strtotime($alert['timestamp'])); ?></td>
                        <td><a href="panels.php?id=<?php echo $alert['panel_id']; ?>"><?php echo htmlspecialchars($alert['serial_number']); ?></a></td>
                        <td><span class="badge <?php echo $alert['severity']; ?>"><?php echo strtoupper($alert['severity']); ?></span></td>
                        <td><?php echo htmlspecialchars($alert['message']); ?></td>
                    </tr>
                    <?php endwhile; ?>
                </tbody>
            </table>
            <?php else: ?>
            <p class="no-data">No active alerts. All systems nominal.</p>
            <?php endif; ?>
        </section>

        <!-- Cooling Systems -->
        <section class="cooling-panel">
            <h2>🌀 Cooling Systems</h2>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>System</th>
                        <th>Location</th>
                        <th>Status</th>
                        <th>Flow Rate</th>
                        <th>Last Maintenance</th>
                    </tr>
                </thead>
                <tbody>
                    <?php while ($system = $cooling->fetch_assoc()): ?>
                    <tr>
                        <td><?php echo htmlspecialchars($system['name']); ?></td>
                        <td><?php echo htmlspecialchars($system['location']); ?></td>
                        <td><span class="badge status-<?php echo $system['status']; ?>"><?php echo strtoupper($system['status']); ?></span></td>
                        <td><?php echo $system['flow_rate'] > 0 ? $system['flow_rate'] . ' L/min' : '-'; ?></td>
                        <td><?php echo date('M j, Y', strtotime($system['last_maintenance'])); ?></td>
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
