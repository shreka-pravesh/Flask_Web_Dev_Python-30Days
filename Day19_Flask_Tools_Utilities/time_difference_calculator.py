from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def time_diff():
    result = None
    if request.method == "POST":
        t1 = request.form["time1"]
        t2 = request.form["time2"]
        time1_obj = datetime.strptime(t1, "%H:%M")
        time2_obj = datetime.strptime(t2, "%H:%M")
        diff = abs((time2_obj - time1_obj).total_seconds() // 60)
        result = f"Time difference: {int(diff)} minutes"
    return render_template("index.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)
