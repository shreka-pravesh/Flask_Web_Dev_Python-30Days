from flask import Flask
import random
app = Flask(__name__)
messages = [
    "Small steps make big changes."
    "Every day is a new chance."
]
@app.route('/')
def quote():
    return f"<h3>{random.choice(messages)}</h3>"
if __name__ == '__main__':
    app.run()
