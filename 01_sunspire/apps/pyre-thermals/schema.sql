-- PyreWatch Thermal Monitoring Database Schema
-- MySQL database for Sunspire thermal safety monitoring

CREATE DATABASE IF NOT EXISTS pyrewatch;
USE pyrewatch;

-- Solar panel thermal data
CREATE TABLE panels (
    panel_id INT PRIMARY KEY AUTO_INCREMENT,
    serial_number VARCHAR(50) NOT NULL,
    location VARCHAR(200),
    install_date DATE,
    current_temp DECIMAL(5,2),
    threshold_temp DECIMAL(5,2) DEFAULT 85.00,
    status ENUM('normal', 'warning', 'critical', 'offline') DEFAULT 'normal',
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Thermal alerts
CREATE TABLE alerts (
    alert_id INT PRIMARY KEY AUTO_INCREMENT,
    panel_id INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    severity ENUM('info', 'warning', 'critical', 'emergency') DEFAULT 'info',
    message TEXT,
    acknowledged BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (panel_id) REFERENCES panels(panel_id)
);

-- Cooling systems
CREATE TABLE cooling_systems (
    system_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    location VARCHAR(200),
    status ENUM('active', 'standby', 'maintenance', 'failed') DEFAULT 'active',
    flow_rate DECIMAL(10,2),
    last_maintenance DATE
);

-- Thermal readings history
CREATE TABLE thermal_readings (
    reading_id INT PRIMARY KEY AUTO_INCREMENT,
    panel_id INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperature DECIMAL(5,2),
    ambient_temp DECIMAL(5,2),
    irradiance DECIMAL(10,2),
    FOREIGN KEY (panel_id) REFERENCES panels(panel_id)
);

-- Insert sample panels
INSERT INTO panels (serial_number, location, install_date, current_temp, threshold_temp, status) VALUES
('SP-2024-001', 'Roof Section A - North', '2024-01-15', 42.5, 85.00, 'normal'),
('SP-2024-002', 'Roof Section A - North', '2024-01-15', 45.2, 85.00, 'normal'),
('SP-2024-003', 'Roof Section A - South', '2024-01-15', 68.9, 85.00, 'warning'),
('SP-2024-004', 'Roof Section B - East', '2024-02-20', 51.3, 85.00, 'normal'),
('SP-2024-005', 'Roof Section B - East', '2024-02-20', 89.7, 85.00, 'critical'),
('SP-2024-006', 'Ground Array 1', '2024-03-10', 38.1, 85.00, 'normal'),
('SP-2024-007', 'Ground Array 1', '2024-03-10', 41.6, 85.00, 'normal'),
('SP-2024-008', 'Carport Structure', '2024-04-05', 55.8, 85.00, 'normal'),
('SP-2024-009', 'Warehouse Roof', '2024-05-12', 0.0, 85.00, 'offline'),
('SP-2024-010', 'Factory Building A', '2024-06-01', 62.4, 85.00, 'normal'),
('SP-2024-011', 'Factory Building A', '2024-06-01', 78.3, 85.00, 'warning'),
('SP-2024-012', 'Factory Building B', '2024-06-15', 44.9, 85.00, 'normal');

-- Insert sample alerts
INSERT INTO alerts (panel_id, severity, message, acknowledged) VALUES
(5, 'critical', 'Panel temperature exceeded critical threshold (89.7°C). Immediate inspection required.', FALSE),
(3, 'warning', 'Panel temperature approaching threshold (68.9°C). Monitoring closely.', FALSE),
(11, 'warning', 'Elevated temperature detected (78.3°C). Cooling system check recommended.', TRUE),
(9, 'info', 'Panel offline - scheduled maintenance in progress.', TRUE),
(5, 'emergency', 'THERMAL RUNAWAY RISK - Panel SP-2024-005 requires immediate shutdown.', FALSE),
(3, 'info', 'Temperature normalized after cloud cover.', TRUE),
(8, 'warning', 'Unexpected temperature spike detected. Investigating.', TRUE);

-- Insert cooling systems
INSERT INTO cooling_systems (name, location, status, flow_rate, last_maintenance) VALUES
('HVAC-A1', 'Roof Section A', 'active', 125.5, '2024-10-15'),
('HVAC-A2', 'Roof Section A', 'active', 118.2, '2024-10-15'),
('HVAC-B1', 'Roof Section B', 'standby', 0.0, '2024-09-20'),
('COOL-G1', 'Ground Array 1', 'active', 95.8, '2024-11-01'),
('COOL-W1', 'Warehouse', 'maintenance', 0.0, '2024-11-28'),
('COOL-F1', 'Factory Building A', 'active', 142.3, '2024-10-01'),
('COOL-F2', 'Factory Building B', 'failed', 0.0, '2024-08-15');

-- Insert thermal readings history
INSERT INTO thermal_readings (panel_id, timestamp, temperature, ambient_temp, irradiance) VALUES
(1, DATE_SUB(NOW(), INTERVAL 1 HOUR), 41.2, 28.5, 850.0),
(1, DATE_SUB(NOW(), INTERVAL 2 HOUR), 39.8, 27.2, 780.0),
(1, DATE_SUB(NOW(), INTERVAL 3 HOUR), 35.1, 25.8, 620.0),
(5, DATE_SUB(NOW(), INTERVAL 1 HOUR), 89.7, 32.1, 1050.0),
(5, DATE_SUB(NOW(), INTERVAL 2 HOUR), 85.2, 31.5, 980.0),
(5, DATE_SUB(NOW(), INTERVAL 3 HOUR), 78.9, 30.2, 920.0),
(5, DATE_SUB(NOW(), INTERVAL 4 HOUR), 72.1, 29.8, 850.0),
(3, DATE_SUB(NOW(), INTERVAL 1 HOUR), 68.9, 30.5, 920.0),
(3, DATE_SUB(NOW(), INTERVAL 2 HOUR), 65.4, 29.8, 880.0),
(11, DATE_SUB(NOW(), INTERVAL 1 HOUR), 78.3, 31.2, 950.0),
(11, DATE_SUB(NOW(), INTERVAL 2 HOUR), 74.1, 30.5, 910.0);

-- Create MySQL user for webapp
CREATE USER IF NOT EXISTS 'pyre'@'localhost' IDENTIFIED BY 'h1ewFWZG';
GRANT ALL PRIVILEGES ON pyrewatch.* TO 'pyre'@'localhost';
GRANT FILE ON *.* TO 'pyre'@'localhost';
FLUSH PRIVILEGES;
