from flask import Flask, render_template
import random
app = Flask(__name__)
affirmations = [
    "You are doing better than you think.",
    "Every day is a new start.",
    "Believe in yourself — you are stronger than you know.",
    "Small steps still move you forward.",
    "You deserve good things."
]
@app.route('/')
def home():
    message = random.choice(affirmations)
    return render_template("affirmation.html", message=message)
if __name__ == "__main__":
    app.run(debug=True)
