from flask import Flask, render_template
import random
app = Flask(__name__)
QUOTES = [
    "Believe you can and you're halfway there.",
    "Every day is a second chance.",
    "Dream big and dare to fail.",
    "Small steps every day lead to big results.",
    "Your only limit is your mind."
]
@app.route("/")
def home():
    quote = random.choice(QUOTES)
    return render_template("quote.html", quote=quote)
if __name__ == "__main__":
    app.run(debug=True)
