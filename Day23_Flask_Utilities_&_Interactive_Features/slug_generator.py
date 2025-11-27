from flask import Flask, render_template, request
app = Flask(__name__)
def make_slug(text):
    return text.lower().replace(" ", "-")
@app.route("/", methods=["GET", "POST"])
def home():
    slug = ""
    if request.method == "POST":
        title = request.form.get("title")
        slug = make_slug(title)
    return render_template("slug.html", slug=slug)
if __name__ == "__main__":
    app.run(debug=True)
