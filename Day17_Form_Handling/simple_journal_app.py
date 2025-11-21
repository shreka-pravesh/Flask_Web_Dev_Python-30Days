from flask import Flask, render_template, request
app = Flask(__name__)
journal_entries = []
@app.route("/", methods=["GET", "POST"])
def journal():
    if request.method == "POST":
        entry = request.form.get("entry")
        if entry:
            journal_entries.append(entry)
    return render_template("index.html", entries=journal_entries)
if __name__ == "__main__":
    app.run(debug=True)
