from flask import Flask, request, render_template
app = Flask(__name__)
sleep_log = []
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        hours = request.form.get("hours")
        sleep_log.append(hours)
    return render_template("sleep.html", logs=sleep_log)
if __name__ == "__main__":
    app.run(debug=True)
