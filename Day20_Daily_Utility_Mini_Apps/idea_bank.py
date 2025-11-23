from flask import Flask, request, render_template
app = Flask(__name__)
ideas = []
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        idea = request.form.get("idea")
        ideas.append(idea)
    return render_template("ideas.html", ideas=ideas)
if __name__ == "__main__":
    app.run(debug=True)
