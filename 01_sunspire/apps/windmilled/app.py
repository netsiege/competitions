#!/usr/bin/env python3
"""
Windmilled - Wind Turbine Configuration Manager
Internal API for managing Sunspire's wind turbine network

Runs on localhost:5000 (internal use only)
"""

import os
import json
import base64
import pickle
from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

CONFIG_FILE = "config.json"

def load_config():
    """Load turbine configuration from JSON file."""
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        return {"error": str(e)}

def save_config(config):
    """Save turbine configuration to JSON file."""
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=2)
        return True
    except Exception:
        return False

# ===============================
# PUBLIC ENDPOINTS
# ===============================

@app.route("/")
def index():
    """API index."""
    return jsonify({
        "service": "Windmilled",
        "description": "Wind Turbine Configuration Manager",
        "version": "1.3.2",
        "endpoints": {
            "/api/turbines": "List all turbines",
            "/api/turbines/<id>": "Get turbine details",
            "/api/status": "System status",
            "/api/maintenance": "Maintenance schedule",
            "/api/config/export": "Export configuration",
            "/api/config/import": "Import configuration (POST)"
        }
    })

@app.route("/api/turbines")
def list_turbines():
    """List all wind turbines."""
    config = load_config()
    return jsonify(config.get("turbines", []))

@app.route("/api/turbines/<turbine_id>")
def get_turbine(turbine_id):
    """Get details for a specific turbine."""
    config = load_config()
    for turbine in config.get("turbines", []):
        if turbine.get("id") == turbine_id:
            return jsonify(turbine)
    return jsonify({"error": "Turbine not found"}), 404

@app.route("/api/status")
def status():
    """Get system status."""
    config = load_config()
    turbines = config.get("turbines", [])
    
    operational = len([t for t in turbines if t.get("status") == "operational"])
    total_output = sum(t.get("output_kw", 0) for t in turbines)
    total_capacity = sum(t.get("capacity_kw", 0) for t in turbines)
    
    return jsonify({
        "timestamp": datetime.now().isoformat(),
        "total_turbines": len(turbines),
        "operational": operational,
        "maintenance": len(turbines) - operational,
        "total_output_kw": total_output,
        "total_capacity_kw": total_capacity,
        "efficiency": round((total_output / total_capacity * 100), 1) if total_capacity > 0 else 0
    })

@app.route("/api/maintenance")
def maintenance():
    """Get maintenance schedule."""
    config = load_config()
    return jsonify(config.get("maintenance_schedule", []))

# ===============================
# CONFIGURATION IMPORT/EXPORT
# ===============================

@app.route("/api/config/export")
def export_config():
    """
    Export current configuration.
    Returns base64-encoded serialized configuration for backup/transfer.
    """
    config = load_config()
    
    # Serialize configuration using pickle for complete Python object support
    serialized = pickle.dumps(config)
    encoded = base64.b64encode(serialized).decode('utf-8')
    
    return jsonify({
        "status": "success",
        "format": "pickle+base64",
        "data": encoded,
        "note": "Use /api/config/import to restore this configuration"
    })

@app.route("/api/config/import", methods=["POST"])
def import_config():
    """
    Import configuration from backup.
    Accepts base64-encoded serialized configuration data.
    
    POST JSON: {"config": "<base64-encoded-pickle-data>"}
    """
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400
    
    data = request.json.get("config")
    if not data:
        return jsonify({"error": "Missing 'config' field"}), 400
    
    try:
        # Decode and deserialize the configuration
        decoded = base64.b64decode(data)
        config = pickle.loads(decoded)
        
        # Save the imported configuration
        if save_config(config):
            return jsonify({
                "status": "success",
                "message": "Configuration imported successfully",
                "turbines_loaded": len(config.get("turbines", []))
            })
        else:
            return jsonify({"error": "Failed to save configuration"}), 500
            
    except base64.binascii.Error:
        return jsonify({"error": "Invalid base64 encoding"}), 400
    except pickle.UnpicklingError as e:
        return jsonify({"error": f"Deserialization failed: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Import failed: {str(e)}"}), 500

# ===============================
# RUN SERVER
# ===============================

if __name__ == "__main__":
    print("[*] Starting Windmilled - Wind Turbine Configuration Manager")
    print("[*] Listening on http://127.0.0.1:5000")
    print("[*] Internal use only - do not expose to external network")
    app.run(host="127.0.0.1", port=5000, debug=False)
