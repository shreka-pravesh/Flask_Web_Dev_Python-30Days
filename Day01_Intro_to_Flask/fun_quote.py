from flask import Flask
import random
app = Flask(__name__)
quotes = [
    "Keep it simple, keep it clean",
    "Dream it, Bulit it. Deploy it",
    "Every bug teaches something new",
    "The best thing about times is, it changes "
]
@app.route('/')
def random_quote():
    return random.choice(quotes)
if __name__ == '__main__':
    app.run()
