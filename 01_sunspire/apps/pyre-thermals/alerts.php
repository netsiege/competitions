<?php
/**
 * PyreWatch - Alert History
 * View and manage thermal alerts
 */

require_once 'config.php';
$conn = getDbConnection();

// Get filter parameters
$severity_filter = isset($_GET['severity']) ? $_GET['severity'] : '';
$status_filter = isset($_GET['status']) ? $_GET['status'] : '';

// Build query with filters
$where_clauses = [];
$query = "SELECT a.*, p.serial_number, p.location FROM alerts a JOIN panels p ON a.panel_id = p.panel_id";

if ($severity_filter && in_array($severity_filter, ['info', 'warning', 'critical', 'emergency'])) {
    $where_clauses[] = "a.severity = '" . $conn->real_escape_string($severity_filter) . "'";
}

if ($status_filter === 'active') {
    $where_clauses[] = "a.acknowledged = FALSE";
} elseif ($status_filter === 'acknowledged') {
    $where_clauses[] = "a.acknowledged = TRUE";
}

if (!empty($where_clauses)) {
    $query .= " WHERE " . implode(" AND ", $where_clauses);
}

$query .= " ORDER BY a.timestamp DESC LIMIT 50";
$alerts = $conn->query($query);

// Get alert statistics
$stats = $conn->query("
    SELECT 
        COUNT(*) as total,
        SUM(CASE WHEN acknowledged = FALSE THEN 1 ELSE 0 END) as active,
        SUM(CASE WHEN severity = 'critical' OR severity = 'emergency' THEN 1 ELSE 0 END) as critical
    FROM alerts
")->fetch_assoc();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo SITE_NAME; ?> - Alerts</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-brand">🔥 <?php echo SITE_NAME; ?></div>
        <ul class="nav-links">
            <li><a href="index.php">Dashboard</a></li>
            <li><a href="panels.php">Panels</a></li>
            <li><a href="alerts.php" class="active">Alerts</a></li>
        </ul>
        <div class="nav-info">
            <span class="version">v<?php echo SITE_VERSION; ?></span>
        </div>
    </nav>

    <main class="container">
        <h1>Alert Management</h1>

        <!-- Alert Statistics -->
        <section class="status-grid small">
            <div class="status-card">
                <h3>Total Alerts</h3>
                <span class="count"><?php echo $stats['total']; ?></span>
            </div>
            <div class="status-card warning">
                <h3>Active</h3>
                <span class="count"><?php echo $stats['active']; ?></span>
            </div>
            <div class="status-card critical">
                <h3>Critical/Emergency</h3>
                <span class="count"><?php echo $stats['critical']; ?></span>
            </div>
        </section>

        <!-- Filters -->
        <section class="filter-panel">
            <h2>🔍 Filter Alerts</h2>
            <form method="GET" action="alerts.php" class="filter-form">
                <div class="form-group">
                    <label for="severity">Severity:</label>
                    <select name="severity" id="severity">
                        <option value="">All</option>
                        <option value="info" <?php echo $severity_filter === 'info' ? 'selected' : ''; ?>>Info</option>
                        <option value="warning" <?php echo $severity_filter === 'warning' ? 'selected' : ''; ?>>Warning</option>
                        <option value="critical" <?php echo $severity_filter === 'critical' ? 'selected' : ''; ?>>Critical</option>
                        <option value="emergency" <?php echo $severity_filter === 'emergency' ? 'selected' : ''; ?>>Emergency</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="status">Status:</label>
                    <select name="status" id="status">
                        <option value="">All</option>
                        <option value="active" <?php echo $status_filter === 'active' ? 'selected' : ''; ?>>Active</option>
                        <option value="acknowledged" <?php echo $status_filter === 'acknowledged' ? 'selected' : ''; ?>>Acknowledged</option>
                    </select>
                </div>
                <button type="submit" class="btn">Apply Filter</button>
                <a href="alerts.php" class="btn btn-secondary">Clear</a>
            </form>
        </section>

        <!-- Alert List -->
        <section class="alerts-list">
            <h2>📋 Alert History</h2>
            <?php if ($alerts->num_rows > 0): ?>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Timestamp</th>
                        <th>Panel</th>
                        <th>Location</th>
                        <th>Severity</th>
                        <th>Message</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <?php while ($alert = $alerts->fetch_assoc()): ?>
                    <tr class="severity-<?php echo $alert['severity']; ?>">
                        <td><?php echo $alert['alert_id']; ?></td>
                        <td><?php echo date('M j, H:i:s', strtotime($alert['timestamp'])); ?></td>
                        <td><a href="panels.php?id=<?php echo $alert['panel_id']; ?>"><?php echo htmlspecialchars($alert['serial_number']); ?></a></td>
                        <td><?php echo htmlspecialchars($alert['location']); ?></td>
                        <td><span class="badge <?php echo $alert['severity']; ?>"><?php echo strtoupper($alert['severity']); ?></span></td>
                        <td><?php echo htmlspecialchars($alert['message']); ?></td>
                        <td>
                            <?php if ($alert['acknowledged']): ?>
                            <span class="badge status-active">ACK</span>
                            <?php else: ?>
                            <span class="badge status-failed">ACTIVE</span>
                            <?php endif; ?>
                        </td>
                    </tr>
                    <?php endwhile; ?>
                </tbody>
            </table>
            <?php else: ?>
            <p class="no-data">No alerts match the selected filters.</p>
            <?php endif; ?>
        </section>
    </main>

    <footer>
        <p>PyreWatch Thermal Monitoring System &copy; Sunspire Energy</p>
    </footer>
</body>
</html>
<?php $conn->close(); ?>
