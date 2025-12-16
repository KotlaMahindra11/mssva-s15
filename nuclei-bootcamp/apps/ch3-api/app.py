from flask import Flask, request, jsonify

app = Flask(__name__)

ORDERS = {
    "1": {"user": "elanthriyan", "item": "laptop"},
    "2": {"user": "mohit", "item": "phone"}
}

@app.route("/api/orders/<oid>")
def order(oid):
    token = request.headers.get("Authorization")

    if not token:
        return "Unauthorized", 401

    return jsonify(ORDERS.get(oid, {}))

app.run(host="0.0.0.0", port=8003)
