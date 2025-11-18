from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def check_palindrome():
    result = None
    if request.method == "POST":
        word = request.form["word"]
        result = "Yes, it is!" if word == word[::-1] else "No, it's not."
    return render_template("palindrome.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)
