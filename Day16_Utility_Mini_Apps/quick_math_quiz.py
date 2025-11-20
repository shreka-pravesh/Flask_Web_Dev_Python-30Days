from flask import Flask, render_template
import random
app = Flask(__name__)
@app.route("/")
def quiz():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return render_template("quiz.html", a=a, b=b, answer=a+b)
if __name__ == "__main__":
    app.run(debug=True)
