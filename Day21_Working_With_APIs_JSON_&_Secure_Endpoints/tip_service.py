from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/calculate-tip", methods=["POST"])
def calculate_tip():
    data = request.get_json()
    amount = data.get("amount", 0)
    percent = data.get("percent", 10)
    tip = amount * (percent / 100)
    total = amount + tip
    return jsonify({
        "amount": amount,
        "tip": tip,
        "total": total
    })
if __name__ == "__main__":
    app.run(debug=True)
