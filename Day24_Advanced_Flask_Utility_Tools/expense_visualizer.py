from flask import Flask, jsonify, request
app = Flask(__name__)
expenses = []
@app.route("/add", methods=["POST"])
def add():
    data = request.json
    expenses.append(data)
    return jsonify({"message": "Added", "total_items": len(expenses)})
@app.route("/data")
def data():
    return jsonify(expenses)
if __name__ == "__main__":
    app.run(debug=True)
