from flask import Flask, request, jsonify, make_response
import uuid

app = Flask(__name__)
store = {}

@app.route("/init")
def init():
    sid = str(uuid.uuid4())
    store[sid] = {"stage": 1}
    resp = make_response(jsonify({"status": "ok"}))
    resp.set_cookie("sid", sid)
    return resp

@app.route("/advance")
def advance():
    sid = request.cookies.get("sid")
    if sid in store:
        store[sid]["stage"] = 2
    return jsonify({"status": "ok"})

@app.route("/commit")
def commit():
    sid = request.cookies.get("sid")

    if sid not in store:
        return jsonify({"result": "done"})

    if store[sid]["stage"] == 1:
        # ❌ state desync: stage 2 never enforced
        return jsonify({
            "result": "done",
            "details": {"mode": "extended", "ops": 3}
        })

    return jsonify({"result": "done"})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9020)
