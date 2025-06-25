from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
latest_location = {}

@app.route('/')
def home():
    return "WRU API çalışıyor"

@app.route('/update', methods=['POST'])
def update_location():
    data = request.get_json()
    token = data.get("token")

    if token != "wru1234":  # 💡 İstediğin gibi değiştirebilirsin
        return jsonify({"error": "Unauthorized"}), 403

    latest_location["lat"] = data.get("lat")
    latest_location["lng"] = data.get("lng")
    latest_location["timestamp"] = datetime.utcnow().isoformat()
    return jsonify({"status": "ok"})

@app.route('/latest', methods=['GET'])
def get_location():
    return jsonify(latest_location)
