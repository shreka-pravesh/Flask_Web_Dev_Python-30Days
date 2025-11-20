from flask import Flask, render_template, request
app = Flask(__name__)
notes = []
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form.get("note")
        notes.append(text)
    return render_template("notes.html", notes=notes)
if __name__ == "__main__":
    app.run(debug=True)
