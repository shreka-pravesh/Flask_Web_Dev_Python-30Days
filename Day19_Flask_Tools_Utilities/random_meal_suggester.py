from flask import Flask, render_template
import random
app = Flask(__name__)
meals = ["Pasta", "Veg Biryani", "Fried Rice", "Idli-Sambar", "Paneer Roll", "Parotta & Kurma"]
@app.route("/")
def suggest():
    meal = random.choice(meals)
    return render_template("index.html", meal=meal)
if __name__ == "__main__":
    app.run(debug=True)
