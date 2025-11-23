from flask import Flask, render_template, request
from collections import Counter
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def count_characters():
    counts = {}
    if request.method == "POST":
        text = request.form.get("text", "").replace(" ", "")
        counts = Counter(text)
    return render_template("index.html", counts=counts)
if __name__ == "__main__":
    app.run(debug=True)
