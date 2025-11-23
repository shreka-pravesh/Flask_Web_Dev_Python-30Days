from flask import Flask, render_template
import random
app = Flask(__name__)
@app.route("/")
def lucky_number():
    number = random.randint(1, 999)
    return render_template("index.html", number=number)
if __name__ == "__main__":
    app.run(debug=True)
