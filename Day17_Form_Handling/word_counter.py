from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def count_words():
    count = None
    if request.method == "POST":
        text = request.form.get("text", "")
        count = len(text.split())
    return render_template("index.html", count=count)
if __name__ == "__main__":
    app.run(debug=True)
