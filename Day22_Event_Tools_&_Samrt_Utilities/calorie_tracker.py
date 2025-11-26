from flask import Flask, render_template, request
app = Flask(__name__)
records = []
@app.route("/")
def home():
    return render_template("calories.html", records=records)
@app.route("/add", methods=["POST"])
def add():
    food = request.form.get("food")
    calories = request.form.get("calories")
    if food and calories:
        records.append({"food": food, "calories": calories})
    return render_template("calories.html", records=records)
if __name__ == "__main__":
    app.run(debug=True)
