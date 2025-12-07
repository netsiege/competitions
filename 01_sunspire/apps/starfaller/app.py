#!/usr/bin/env python3
"""
Starfall Health Monitoring API
- External API on :5000 (health checks, history)
- Internal API on :5001 (config display)

Developed by fern (systems stewardess @ Sunspire)
"""

import os
import json
import subprocess
import requests
from datetime import datetime
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from threading import Thread

load_dotenv()

SYSTEMS_CONFIG = "systems.json"
HEALTH_LOG = "health_history.csv"
MAX_LOG_LINES = 50
STARFALLER_TOKEN = os.getenv("STARFALLER_TOKEN", "")

#:5000

external_app = Flask(__name__)

def load_systems():
    """Load systems configuration from JSON file."""
    try:
        with open(SYSTEMS_CONFIG, "r") as f:
            return json.load(f)
    except Exception as e:
        return {"systems": [], "error": str(e)}

def ping_host(ip):
    """Ping a host and return True if reachable."""
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "2", ip],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except Exception:
        return False

def log_health_check(hostname, ip, status):
    """Log health check result to CSV file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    line_count = 0
    if os.path.exists(HEALTH_LOG):
        with open(HEALTH_LOG, "r") as f:
            line_count = sum(1 for _ in f)
    
    # Clear file if more than 50 lines
    if line_count > MAX_LOG_LINES:
        open(HEALTH_LOG, "w").close()
    
    with open(HEALTH_LOG, "a") as f:
        if os.path.getsize(HEALTH_LOG) == 0:
            f.write("timestamp,hostname,ip,status\n")
        f.write(f"{timestamp},{hostname},{ip},{status}\n")

@external_app.route("/")
def index():
    """API index."""
    return jsonify({
        "service": "Starfall Health Monitor",
        "version": "1.0",
        "endpoints": {
            "/api/health/all": "Check health of all systems",
            "/api/health/history": "View health check history. Use ?file=<FILENAME> to specify log file. For example /api/health/history?file=health_history.csv"
        }
    })

@external_app.route("/api/health/all")
def health_all():
    """Check health of all configured systems using ping."""
    config = load_systems()
    results = []
    
    for system in config.get("systems", []):
        hostname = system.get("hostname", "unknown")
        ip = system.get("ip", "0.0.0.0")
        
        # Use ping command to check health (secure - no injection)
        is_healthy = ping_host(ip)
        status = "healthy" if is_healthy else "unreachable"
        
        # Log the health check
        log_health_check(hostname, ip, status)
        
        results.append({
            "hostname": hostname,
            "ip": ip,
            "status": status
        })
    
    return jsonify({
        "timestamp": datetime.now().isoformat(),
        "results": results
    })

@external_app.route("/api/health/history")
def health_history():
    """
    View health check history from CSV file.
    """
    log_file = request.args.get("file", HEALTH_LOG)
    
    try:
        result = subprocess.run(
            f"cat {log_file}",
            shell=True, 
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            lines = result.stdout.strip().split("\n")
            return jsonify({
                "file": log_file,
                "lines": len(lines),
                "content": result.stdout
            })
        else:
            return jsonify({
                "error": "Failed to read file",
                "details": result.stderr
            }), 404
            
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Command timed out"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#:5001

internal_app = Flask(__name__)

def get_system_ip(hostname):
    """Get IP address for a hostname from config."""
    config = load_systems()
    for system in config.get("systems", []):
        if system.get("hostname", "").lower() == hostname.lower():
            return system.get("ip")
    return None

def fetch_system_info(ip):
    """
    Fetch system info from remote API.
    Makes a GET request to http://<ip>:4000/api/info
    """
    try:
        headers = {
            "User-Agent": "STARFALLER"
        }
        params = {
            "token": STARFALLER_TOKEN
        }
        
        response = requests.get(
            f"http://{ip}:4000/api/info",
            headers=headers,
            params=params,
            timeout=5
        )
        
        return {
            "status": "success",
            "status_code": response.status_code,
            "data": response.text
        }
    except requests.exceptions.ConnectionError:
        return {
            "status": "error",
            "message": f"Could not connect to {ip}:4000"
        }
    except requests.exceptions.Timeout:
        return {
            "status": "error", 
            "message": "Request timed out"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

@internal_app.route("/")
def internal_index():
    """Internal API index."""
    return jsonify({
        "service": "Starfall Internal Config API",
        "version": "1.0",
        "note": "Internal use only",
        "endpoints": {
            "/api/config/display?hostname=<HOSTNAME>": "Display system configuration"
        }
    })

@internal_app.route("/api/config/display")
def config_display():
    """
    Display configuration for a system by hostname.
    Makes request to the system's IP:4000/api/info endpoint.
    """
    hostname = request.args.get("hostname", "").strip('"').strip("'")
    
    if not hostname:
        return jsonify({
            "error": "Missing hostname parameter",
            "usage": "/api/config/display?hostname=<HOSTNAME>"
        }), 400
    
    # Get IP for hostname
    ip = get_system_ip(hostname)
    
    if not ip:
        return jsonify({
            "error": f"Unknown hostname: {hostname}",
            "available": [s["hostname"] for s in load_systems().get("systems", [])]
        }), 404
    
    result = fetch_system_info(ip)
    
    return jsonify({
        "hostname": hostname,
        "ip": ip,
        "remote_info": result
    })

# ===============================
# RUN SERVERS
# ===============================

def run_external():
    """Run external API on port 5000."""
    external_app.run(host="0.0.0.0", port=5000, debug=False)

def run_internal():
    """Run internal API on port 5001 locally"""
    internal_app.run(host="127.0.0.1", port=5001, debug=False)

if __name__ == "__main__":
    print("[*] Starting Starfall Health Monitor...")
    print("[*] External API: http://0.0.0.0:5000")
    print("[*] Internal API: http://127.0.0.1:5001")
    
    internal_thread = Thread(target=run_internal, daemon=True)
    internal_thread.start()
    
    run_external()
