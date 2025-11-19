from flask import Flask, render_template, request
import datetime
app = Flask(__name__)
visit_history = []
@app.route("/")
def home():
    visit_details = {
        "ip": request.remote_addr,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    visit_history.append(visit_details)
    return render_template("index.html", visits=visit_history)
if __name__ == "__main__":
    app.run(debug=True)
