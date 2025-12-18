<?php
/**
 * Sunspire Energy Heatmap Dashboard
 * Real-time energy consumption monitoring across Sunspire regions
 */
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Energy Heatmap - Sunspire</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>⚡ Sunspire Energy Heatmap</h1>
            <p class="subtitle">Real-time power consumption monitoring</p>
        </header>

        <div class="controls">
            <div class="filter-group">
                <label for="region">Region:</label>
                <select id="region" onchange="updateHeatmap()">
                    <option value="all">All Regions</option>
                    <option value="north">North - Solar Array</option>
                    <option value="south">South - Wind Farm</option>
                    <option value="east">East - Thermal Plant</option>
                    <option value="west">West - Grid Storage</option>
                    <option value="central">Central - HQ</option>
                </select>
            </div>
            <div class="filter-group">
                <label for="source">Energy Source:</label>
                <select id="source" onchange="updateHeatmap()">
                    <option value="all">All Sources</option>
                    <option value="solar">Solar</option>
                    <option value="wind">Wind</option>
                    <option value="thermal">Thermal</option>
                    <option value="grid">Grid</option>
                </select>
            </div>
            <button onclick="updateHeatmap()" class="refresh-btn">🔄 Refresh</button>
        </div>

        <div class="dashboard">
            <div class="heatmap-container">
                <h2>Energy Grid</h2>
                <div id="heatmap" class="heatmap">
                    <!-- Populated by JavaScript -->
                </div>
            </div>

            <div class="stats-panel">
                <h2>Statistics</h2>
                <div id="stats" class="stats">
                    <!-- Populated by JavaScript -->
                </div>
            </div>
        </div>

        <div class="data-panel">
            <h2>Filtered Data</h2>
            <pre id="data-output">Select a region to view detailed data...</pre>
        </div>

        <footer>
            <p>Sunspire Energy Management System v2.4.1</p>
            <p>Data refreshed every 5 minutes | <a href="/api.php?action=stats">API Status</a></p>
        </footer>
    </div>

    <script>
        function updateHeatmap() {
            const region = document.getElementById('region').value;
            const source = document.getElementById('source').value;
            
            // Fetch filtered data from API
            let url = 'api.php?action=filter';
            if (region !== 'all') {
                url += '&region=' + encodeURIComponent(region);
            }
            if (source !== 'all') {
                url += '&source=' + encodeURIComponent(source);
            }
            
            fetch(url)
                .then(response => response.text())
                .then(data => {
                    document.getElementById('data-output').textContent = data;
                    try {
                        const parsed = JSON.parse(data);
                        renderHeatmap(parsed);
                        renderStats(parsed);
                    } catch (e) {
                        // If not valid JSON, just show raw output
                        console.log('Raw output:', data);
                    }
                })
                .catch(error => {
                    document.getElementById('data-output').textContent = 'Error: ' + error;
                });
        }

        function renderHeatmap(data) {
            const heatmap = document.getElementById('heatmap');
            heatmap.innerHTML = '';
            
            const zones = Array.isArray(data) ? data : [data];
            
            zones.forEach(zone => {
                if (zone && zone.region) {
                    const cell = document.createElement('div');
                    cell.className = 'heatmap-cell';
                    
                    // Color based on efficiency
                    const efficiency = zone.efficiency || 0;
                    if (efficiency >= 90) {
                        cell.classList.add('efficiency-high');
                    } else if (efficiency >= 70) {
                        cell.classList.add('efficiency-medium');
                    } else {
                        cell.classList.add('efficiency-low');
                    }
                    
                    cell.innerHTML = `
                        <div class="cell-title">${zone.name || zone.region}</div>
                        <div class="cell-value">${zone.consumption_kwh || 0} kWh</div>
                        <div class="cell-efficiency">${efficiency}% eff</div>
                    `;
                    heatmap.appendChild(cell);
                }
            });
            
            if (heatmap.innerHTML === '') {
                heatmap.innerHTML = '<div class="no-data">No data for selected filters</div>';
            }
        }

        function renderStats(data) {
            const stats = document.getElementById('stats');
            const zones = Array.isArray(data) ? data : [data];
            
            let totalConsumption = 0;
            let totalGeneration = 0;
            let avgEfficiency = 0;
            let count = 0;
            
            zones.forEach(zone => {
                if (zone && zone.consumption_kwh) {
                    totalConsumption += zone.consumption_kwh;
                    totalGeneration += zone.generation_kwh || 0;
                    avgEfficiency += zone.efficiency || 0;
                    count++;
                }
            });
            
            if (count > 0) {
                avgEfficiency = (avgEfficiency / count).toFixed(1);
            }
            
            stats.innerHTML = `
                <div class="stat-item">
                    <span class="stat-label">Total Consumption</span>
                    <span class="stat-value">${totalConsumption.toLocaleString()} kWh</span>
                </div>
                <div class="stat-item">
                    <span class="stat-label">Total Generation</span>
                    <span class="stat-value">${totalGeneration.toLocaleString()} kWh</span>
                </div>
                <div class="stat-item">
                    <span class="stat-label">Avg Efficiency</span>
                    <span class="stat-value">${avgEfficiency}%</span>
                </div>
                <div class="stat-item">
                    <span class="stat-label">Active Zones</span>
                    <span class="stat-value">${count}</span>
                </div>
            `;
        }

        // Load initial data
        document.addEventListener('DOMContentLoaded', function() {
            fetch('api.php?action=stats')
                .then(response => response.text())
                .then(data => {
                    try {
                        const parsed = JSON.parse(data);
                        if (parsed.zones) {
                            renderHeatmap(parsed.zones);
                            renderStats(parsed.zones);
                        }
                    } catch (e) {
                        console.log('Initial load error:', e);
                    }
                });
        });
    </script>
</body>
</html>
