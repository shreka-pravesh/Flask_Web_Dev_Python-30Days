from flask import Flask, render_template, request
app = Flask(__name__)
habits = []
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        habit = request.form.get("habit")
        habits.append(habit)
    return render_template("habits.html", habits=habits)
if __name__ == "__main__":
    app.run(debug=True)
