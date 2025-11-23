from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def encrypt():
    result = None
    if request.method == "POST":
        text = request.form["text"]
        encrypted = ""
        for ch in text:
            encrypted += chr(ord(ch) + 2)
        result = encrypted
    return render_template("index.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)
