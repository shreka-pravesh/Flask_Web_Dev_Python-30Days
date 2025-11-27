from flask import Flask, session, render_template
app = Flask(__name__)
app.secret_key = "visit123"
@app.route("/")
def home():
    if "visited" in session:
        msg = "Welcome back!"
    else:
        session["visited"] = True
        msg = "Hello, first time visitor!"
    return render_template("visit.html", msg=msg)
if __name__ == "__main__":
    app.run(debug=True)
