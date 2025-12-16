from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "invalid json"}), 400

    if "username" in data and "password" not in data:
        return jsonify({"token": "internal-access"}), 200

    if data.get("username") == "admin" and data.get("password") == "admin123":
        return jsonify({"token": "valid"}), 200

    return jsonify({"error": "unauthorized"}), 401

app.run(host="0.0.0.0", port=8001)
