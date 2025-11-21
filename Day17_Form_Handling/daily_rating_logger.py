from flask import Flask, render_template, request
app = Flask(__name__)
ratings = []
@app.route("/", methods=["GET", "POST"])
def log_rating():
    if request.method == "POST":
        rate = request.form.get("rate")
        if rate:
            ratings.append(rate)
    return render_template("index.html", ratings=ratings)
if __name__ == "__main__":
    app.run(debug=True)
