from flask import Flask, render_template
import random
app = Flask(__name__)
words1 = ["Blue", "Fire", "Shadow", "Star", "Silent"]
words2 = ["Tiger", "Wolf", "Knight", "Ninja", "Coder"]
@app.route("/")
def username():
    name = random.choice(words1) + random.choice(words2) + str(random.randint(10, 99))
    return render_template("username.html", username=name)
if __name__ == "__main__":
    app.run(debug=True)
