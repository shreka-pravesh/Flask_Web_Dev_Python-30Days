from flask import Flask, render_template, request, flash, redirect, url_for
app = Flask(__name__)
app.secret_key = "flashdemo123"
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_msg = request.form.get("message")
        flash(f"You submitted: {user_msg}")
        return redirect(url_for("home"))
    return render_template("flash_demo.html")
if __name__ == "__main__":
    app.run(debug=True)
