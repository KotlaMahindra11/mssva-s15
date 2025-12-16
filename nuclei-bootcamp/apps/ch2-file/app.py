from flask import Flask, request, send_file
import os

app = Flask(__name__)

BASE = "/tmp/files"
os.makedirs(BASE, exist_ok=True)

@app.route("/download")
def download():
    f = request.args.get("file", "")
    path = os.path.normpath(os.path.join(BASE, f))

    if not path.startswith(BASE):
        return "Not allowed", 403

    if os.path.exists(path):
        return send_file(path)

    return "Not found", 404

app.run(host="0.0.0.0", port=8002)
