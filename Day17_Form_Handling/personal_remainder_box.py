from flask import Flask, render_template, request
app = Flask(__name__)
reminders = []
@app.route("/", methods=["GET", "POST"])
def reminder_box():
    if request.method == "POST":
        r = request.form.get("reminder")
        if r:
            reminders.append(r)
    return render_template("index.html", reminders=reminders)
if __name__ == "__main__":
    app.run(debug=True)
