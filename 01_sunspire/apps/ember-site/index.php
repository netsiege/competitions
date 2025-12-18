<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ember - Legacy Systems</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            min-height: 100vh;
            color: #e4e4e4;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        header {
            text-align: center;
            margin-bottom: 50px;
        }
        h1 {
            font-size: 3rem;
            color: #ff6b35;
            text-shadow: 0 0 20px rgba(255, 107, 53, 0.5);
            margin-bottom: 10px;
        }
        .subtitle {
            color: #888;
            font-size: 1.1rem;
        }
        .warning-banner {
            background: rgba(255, 107, 53, 0.1);
            border: 1px solid #ff6b35;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 40px;
            text-align: center;
        }
        .warning-banner h3 {
            color: #ff6b35;
            margin-bottom: 10px;
        }
        .status-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }
        .status-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 25px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .status-card h3 {
            color: #ff6b35;
            margin-bottom: 15px;
            font-size: 1.1rem;
        }
        .status-item {
            display: flex;
            justify-content: space-between;
            padding: 8px 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }
        .status-item:last-child {
            border-bottom: none;
        }
        .status-online {
            color: #4ade80;
        }
        .status-offline {
            color: #f87171;
        }
        .links {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 25px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .links h3 {
            color: #ff6b35;
            margin-bottom: 15px;
        }
        .links ul {
            list-style: none;
        }
        .links li {
            padding: 10px 0;
        }
        .links a {
            color: #60a5fa;
            text-decoration: none;
        }
        .links a:hover {
            text-decoration: underline;
        }
        footer {
            text-align: center;
            margin-top: 50px;
            color: #666;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🔥 EMBER</h1>
            <p class="subtitle">Legacy Infrastructure Management</p>
        </header>

        <div class="warning-banner">
            <h3>⚠️ DEPRECATION NOTICE</h3>
            <p>This server is scheduled for decommissioning. Please migrate workloads to new infrastructure.</p>
        </div>

        <div class="status-grid">
            <div class="status-card">
                <h3>System Status</h3>
                <div class="status-item">
                    <span>Web Server</span>
                    <span class="status-online">● Online</span>
                </div>
                <div class="status-item">
                    <span>File Share</span>
                    <span class="status-online">● Online</span>
                </div>
                <div class="status-item">
                    <span>Maintenance</span>
                    <span class="status-online">● Scheduled</span>
                </div>
            </div>

            <div class="status-card">
                <h3>Server Information</h3>
                <div class="status-item">
                    <span>Hostname</span>
                    <span>EMBER</span>
                </div>
                <div class="status-item">
                    <span>Role</span>
                    <span>Legacy File Server</span>
                </div>
                <div class="status-item">
                    <span>Age</span>
                    <span>7+ years</span>
                </div>
            </div>
        </div>

        <div class="links">
            <h3>Quick Links</h3>
            <ul>
                <li><a href="/info.php">Server Information</a> - PHP configuration and system details</li>
                <li><a href="file://ember/Scripts">Scripts Share</a> - Maintenance scripts repository</li>
            </ul>
        </div>

        <footer>
            <p>Ember Legacy Server &copy; Sunspire Infrastructure</p>
            <p>Contact IT if you need access to this system.</p>
        </footer>
    </div>
</body>
</html>
