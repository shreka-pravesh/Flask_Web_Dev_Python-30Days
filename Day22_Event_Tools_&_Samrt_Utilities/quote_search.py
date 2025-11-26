from flask import Flask, render_template, request
app = Flask(__name__)
quotes = [
    "Stay positive.",
    "Work hard in silence.",
    "Believe in yourself.",
    "Dream big and dare to fail."
]
@app.route("/")
def home():
    return render_template("quote.html")
@app.route("/search", methods=["POST"])
def search():
    word = request.form.get("word").lower()
    result = [q for q in quotes if word in q.lower()]
    return render_template("quote.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)
