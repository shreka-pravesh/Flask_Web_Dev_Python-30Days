from flask import Flask, render_template
import random
app = Flask(__name__)
quotes = [
    "Believe in yourself!",
    "Every day is a fresh start.",
    "Keep going, you’re doing great!",
    "Stay positive and work hard.",
    "Dream big, act bigger."
]
@app.route('/')
def wall():
    quote = random.choice(quotes)
    return render_template('inspiration_wall.html', quote=quote)
if __name__ == '__main__':
    app.run(debug=True)
