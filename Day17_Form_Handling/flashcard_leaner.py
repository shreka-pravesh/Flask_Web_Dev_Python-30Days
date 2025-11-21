from flask import Flask, render_template
app = Flask(__name__)
flashcards = {
    "Python": "A popular programming language.",
    "Flask": "A lightweight Python web framework.",
    "API": "Allows communication between applications."
}
@app.route("/")
def cards():
    return render_template("index.html", cards=flashcards)
if __name__ == "__main__":
    app.run(debug=True)
