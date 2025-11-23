from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def reverse_text():
    result = ""
    if request.method == "POST":
        text = request.form.get("text")
        result = text[::-1] if text else ""
    return render_template("index.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)
