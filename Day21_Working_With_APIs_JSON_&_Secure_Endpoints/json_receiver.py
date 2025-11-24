from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/receive", methods=["POST"])
def receive():
    data = request.get_json()
    return jsonify({
        "message": "JSON received successfully",
        "your_data": data
    })
if __name__ == "__main__":
    app.run(debug=True)
