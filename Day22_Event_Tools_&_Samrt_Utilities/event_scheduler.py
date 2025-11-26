from flask import Flask, render_template, request
app = Flask(__name__)
events = []
@app.route("/")
def home():
    return render_template("schedule.html", events=events)
@app.route("/add", methods=["POST"])
def add_event():
    event = request.form.get("event")
    date = request.form.get("date")
    if event and date:
        events.append({"event": event, "date": date})
    return render_template("schedule.html", events=events)
if __name__ == "__main__":
    app.run(debug=True)
