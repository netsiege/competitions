from flask import Flask, jsonify, request, abort
from flasgger import Swagger
import json
import os

app = Flask(__name__)
swagger = Swagger(app)
INVENTORY_FILE = 'inventory-4b37de.json'
API_TOKEN = "phobos_phaQI7aKlSTahAY9stEhOjuwu"

# ----------------------------
# Helper functions
# ----------------------------
def load_inventory():
    if not os.path.exists(INVENTORY_FILE):
        return []
    with open(INVENTORY_FILE, 'r') as f:
        return json.load(f)

def save_inventory(data):
    with open(INVENTORY_FILE, 'w') as f:
        json.dump(data, f, indent=2)
def require_token():
    token = request.headers.get("Authorization")
    if f"{API_TOKEN}" not in token:
        abort(401, description="Unauthorized: Invalid or missing token")
# ----------------------------
# Routes
# ----------------------------

@app.route('/ping', methods=['GET'])
def ping():
    """
    Health check endpoint
    ---
    responses:
      200:
        description: Pong response
        examples:
          application/json: { "message": "pong" }
    """
    return jsonify({"message": "pong"}), 200

@app.route('/servers', methods=['GET'])
def get_servers():
    """
    Get all servers (requires Authorization header)
    ---
    parameters:
      - name: Authorization
        in: header
        required: true
        type: string
        description: Bearer API token
      - name: include_credentials
        in: query
        type: boolean
        required: false
        description: Whether to include admin credentials
    responses:
      200:
        description: A list of servers
    """
    require_token()
    include_credentials = request.args.get('include_credentials', 'false').lower() == 'true'
    
    inventory = load_inventory()

    if not include_credentials:
        for server in inventory:
            server.pop('admin', None)

    return jsonify(inventory), 200

@app.route('/echo', methods=['POST'])
def echo():
    """
    Echo endpoint
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            message:
              type: string
              example: Hello
    responses:
      200:
        description: Echoed response
        schema:
          type: object
          properties:
            echoed:
              type: string
    """
    data = request.get_json()
    return jsonify({"echoed": data.get("message", "")}), 200

@app.route('/servers', methods=['POST'])
def add_server():
    """
    Add a new server to the inventory (requires Authorization header)
    ---
    parameters:
      - name: Authorization
        in: header
        required: true
        type: string
        description: Bearer API token
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            hostname: { type: string }
            os: { type: string }
            ip: { type: string }
            function: { type: string }
            admin:
              type: object
              properties:
                username: { type: string }
                password: { type: string }
            virtualized: { type: boolean }
            days_online: { type: integer }
    responses:
      201:
        description: Server added successfully
    """
    require_token()
    data = request.get_json()
    inventory = load_inventory()
    inventory.append(data)
    save_inventory(inventory)
    return jsonify({"message": "Server added"}), 201

@app.route('/debug/readfile', methods=['GET'])
def read_any_file():
    """
    Read contents of any file on disk
    ---
    parameters:
      - name: path
        in: query
        required: true
        type: string
        description: Full file path to read
    responses:
      200:
        description: File contents returned
      400:
        description: Missing path
      500:
        description: File read error
    """
    file_path = request.args.get("path")
    if not file_path:
        return jsonify({"error": "Missing 'path' parameter"}), 400

    try:
        with open(file_path, "r") as f:
            contents = f.read()
        return jsonify({
            "path": file_path,
            "contents": contents
        }), 200
    except Exception as e:
        return jsonify({"error": f"Could not read file: {str(e)}"}), 500


@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Phobos Inventory System API!",
        "docs_url": "/apidocs/"
    })

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=8000, debug=True)
