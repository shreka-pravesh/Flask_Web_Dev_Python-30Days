from flask import Flask, render_template, request
import datetime
app = Flask(__name__)
log = []
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mood = request.form.get("mood")
        weather = request.form.get("weather")
        log.append({
            "mood": mood,
            "weather": weather,
            "time": datetime.datetime.now().strftime("%H:%M:%S")
        })
    return render_template("mood_weather.html", log=log)
if __name__ == "__main__":
    app.run(debug=True)
