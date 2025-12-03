from flask import Flask, request, jsonify
app = Flask(__name__)
reminders = []
@app.route("/add_reminder", methods=["POST"])
def add_reminder():
    msg = request.json.get("message")
    reminders.append(msg)
    return jsonify({"status": "saved", "count": len(reminders)})
@app.route("/reminders")
def get_reminders():
    return jsonify(reminders)
if __name__ == "__main__":
    app.run(debug=True)
