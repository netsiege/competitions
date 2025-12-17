#!/usr/bin/env python3
"""
Forge Manufacturing Control API
Port 4000 - Component fabrication monitoring and control

Forge is Sunspire's manufacturing facility responsible for producing
solar panel components and sustainable materials.

Developed by mason (manufacturing engineer @ Sunspire)
"""

import os
import json
from flask import Flask, jsonify, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuration
MATERIALS_FILE = "materials.json"
JOBS_FILE = "jobs.json"
FORGE_TOKEN = os.getenv("FORGE_TOKEN", "")

def load_json_file(filepath):
    """Load data from JSON file."""
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except Exception as e:
        return {"error": str(e)}

def validate_starfaller_request():
    """
    Validate incoming request from Starfaller internal API.
    Requires correct User-Agent header and token parameter.
    """
    user_agent = request.headers.get("User-Agent", "")
    token = request.args.get("token", "")
    
    if user_agent != "STARFALLER":
        return False
    if token != FORGE_TOKEN:
        return False
    return True

# ===============================
# PUBLIC ENDPOINTS
# ===============================

@app.route("/")
def index():
    """API index with facility status."""
    return jsonify({
        "service": "Forge Manufacturing Control",
        "facility": "Component Fabrication Center",
        "version": "2.1.0",
        "status": "operational",
        "endpoints": {
            "/api/status": "Current production status",
            "/api/materials": "Raw materials inventory",
            "/api/jobs": "Active manufacturing jobs",
            "/api/info": "System information (restricted)"
        }
    })

@app.route("/api/status")
def status():
    """Current production status."""
    jobs_data = load_json_file(JOBS_FILE)
    materials_data = load_json_file(MATERIALS_FILE)
    
    active_jobs = len([j for j in jobs_data.get("jobs", []) if j.get("status") == "in_progress"])
    pending_jobs = len([j for j in jobs_data.get("jobs", []) if j.get("status") == "pending"])
    
    low_stock = [m["name"] for m in materials_data.get("materials", []) 
                 if m.get("quantity", 0) < m.get("minimum_threshold", 100)]
    
    return jsonify({
        "facility": "Forge Manufacturing Center",
        "operational": True,
        "production": {
            "active_jobs": active_jobs,
            "pending_jobs": pending_jobs,
            "completed_today": 12
        },
        "alerts": {
            "low_stock_materials": low_stock,
            "equipment_warnings": []
        },
        "last_updated": "2024-12-16T08:30:00Z"
    })

@app.route("/api/materials")
def materials():
    """Raw materials inventory."""
    data = load_json_file(MATERIALS_FILE)
    return jsonify(data)

@app.route("/api/jobs")
def jobs():
    """Active manufacturing jobs."""
    data = load_json_file(JOBS_FILE)
    return jsonify(data)

@app.route("/api/info")
def info():
    """
    System information endpoint.
    Restricted to Starfaller internal API requests.
    
    Returns environment configuration when properly authenticated.
    """
    if not validate_starfaller_request():
        return jsonify({
            "error": "Access denied",
            "message": "This endpoint requires internal authorization"
        }), 403
    
    # Authenticated request - return full system info including env vars
    return jsonify({
        "hostname": "forge",
        "facility": "Component Manufacturing Center",
        "location": "Building 7, Sunspire Industrial Complex",
        "system": {
            "os": "Ubuntu 24.04 LTS",
            "uptime": "47 days",
            "load": [0.42, 0.38, 0.35]
        },
        "environment": {
            "FORGE_USER": os.getenv("FORGE_USER", "forge"),
            "FORGE_HOME": os.getenv("FORGE_HOME", "/home/forge"),
            "ROOT_PASSWORD": os.getenv("ROOT_PASSWORD", ""),
            "DB_HOST": os.getenv("DB_HOST", "localhost"),
            "API_PORT": os.getenv("API_PORT", "4000"),
            "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
            "BACKUP_PATH": os.getenv("BACKUP_PATH", "/var/backups/forge")
        },
        "services": [
            {"name": "forge-api", "status": "running", "port": 4000},
            {"name": "git-daemon", "status": "running", "port": 80},
            {"name": "sshd", "status": "running", "port": 22}
        ]
    })

# ===============================
# RUN SERVER
# ===============================

if __name__ == "__main__":
    print("[*] Starting Forge Manufacturing Control API...")
    print("[*] Listening on http://0.0.0.0:4000")
    app.run(host="0.0.0.0", port=4000, debug=False)
