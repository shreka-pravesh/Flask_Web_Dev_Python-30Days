from flask import Flask, request, jsonify
app = Flask(__name__)
API_KEY = "SECRET123"
@app.route("/secure-data")
def secure_data():
    key = request.headers.get("X-API-KEY")
    if key != API_KEY:
        return jsonify({"error": "Invalid or missing API Key"}), 401
    return jsonify({"message": "Access granted", "data": "Hidden content here"})
if __name__ == "__main__":
    app.run(debug=True)
