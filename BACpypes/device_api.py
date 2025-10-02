from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory device list
devices = [
    {"id": 1, "name": "Thermostat", "status": "online"},
    {"id": 2, "name": "Light Sensor", "status": "offline"}
]

@app.route('/')
def home():
    return "Device API is running. Try /devices"

# Get all devices
@app.route('/devices', methods=['GET'])
def get_devices():
    return jsonify(devices)

# Get a specific device by ID
@app.route('/devices/<int:device_id>', methods=['GET'])
def get_device(device_id):
    device = next((d for d in devices if d["id"] == device_id), None)
    return jsonify(device) if device else ("Device not found", 404)

# Add a new device
@app.route('/devices', methods=['POST'])
def add_device():
    new_device = request.get_json()
    devices.append(new_device)
    return jsonify(new_device), 201

# Update a device
@app.route('/devices/<int:device_id>', methods=['PUT'])
def update_device(device_id):
    updated_data = request.get_json()
    for device in devices:
        if device["id"] == device_id:
            device.update(updated_data)
            return jsonify(device)
    return ("Device not found", 404)

# Delete a device
@app.route('/devices/<int:device_id>', methods=['DELETE'])
def delete_device(device_id):
    global devices
    devices = [d for d in devices if d["id"] != device_id]
    return ("Deleted", 204)

if __name__ == '__main__':
    app.run(debug=True)