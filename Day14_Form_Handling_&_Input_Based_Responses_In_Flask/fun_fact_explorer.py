from flask import Flask, render_template
import random
app = Flask(__name__)
facts = [
    "Honey never spoils.",
    "Bananas are berries, but strawberries aren't.",
    "Octopuses have three hearts.",
    "A day on Venus is longer than a year on Venus.",
    "Some cats are allergic to humans."
]
@app.route('/')
def fun_fact():
    fact = random.choice(facts)
    return render_template("facts.html", fact=fact)
if __name__ == "__main__":
    app.run(debug=True)
