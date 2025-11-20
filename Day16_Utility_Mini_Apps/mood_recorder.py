from flask import Flask, render_template, request
app = Flask(__name__)
moods = []
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        mood = request.form.get("mood")
        moods.append(mood)
    return render_template("mood.html", moods=moods)
if __name__ == "__main__":
    app.run(debug=True)
