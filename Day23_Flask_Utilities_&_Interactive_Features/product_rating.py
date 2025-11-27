from flask import Flask, render_template, request
app = Flask(__name__)
ratings = []
@app.route("/", methods=["GET", "POST"])
def rate():
    if request.method == "POST":
        product = request.form.get("product")
        stars = request.form.get("stars")
        ratings.append((product, stars))
    return render_template("rating.html", ratings=ratings)
if __name__ == "__main__":
    app.run(debug=True)
