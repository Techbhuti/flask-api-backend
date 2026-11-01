from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "success",
        "message": "Welcome to the Python REST API Backend Service",
        "version": "1.0.0"
    })

@app.route("/api/leads", methods=["GET"])
def get_leads():
    sample_leads = [
        {"id": 1, "company": "Tech Solutions", "status": "Outreached"},
        {"id": 2, "company": "Apex Digital", "status": "Pending"}
    ]
    return jsonify(sample_leads), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
