from flask import Flask, render_template, request
import random
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def shuffle_word():
    shuffled = ""
    if request.method == "POST":
        word = request.form.get("word")
        if word:
            letters = list(word)
            random.shuffle(letters)
            shuffled = "".join(letters)
    return render_template("index.html", shuffled=shuffled)
if __name__ == "__main__":
    app.run(debug=True)
