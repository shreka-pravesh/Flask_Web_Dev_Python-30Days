from flask import Flask, request, render_template
app = Flask(__name__)
goal = ""
@app.route("/", methods=["GET", "POST"])
def home():
    global goal
    if request.method == "POST":
        goal = request.form.get("goal")
    return render_template("goal.html", goal=goal)
if __name__ == "__main__":
    app.run(debug=True)
