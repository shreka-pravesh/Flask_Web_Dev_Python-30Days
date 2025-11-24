from flask import Flask, request, jsonify
app = Flask(__name__)
notes = []
@app.route("/add-note", methods=["POST"])
def add_note():
    data = request.get_json()
    note = data.get("note")
    notes.append(note)
    return jsonify({"message": "Note added", "total_notes": len(notes)})
@app.route("/notes")
def get_notes():
    return jsonify({"notes": notes})
if __name__ == "__main__":
    app.run(debug=True)
