from flask import Flask, render_template, request
app = Flask(__name__)
dictionary = {
    "hello": "vanakkam",
    "love": "anbu",
    "television": "tholaikaatchi",
    "friend": "nanban"
}
@app.route("/")
def home():
    return render_template("translate.html")
@app.route("/convert", methods=["POST"])
def convert():
    word = request.form.get("word").lower()
    meaning = dictionary.get(word, "No translation found")
    return render_template("translate.html", meaning=meaning)
if __name__ == "__main__":
    app.run(debug=True)
