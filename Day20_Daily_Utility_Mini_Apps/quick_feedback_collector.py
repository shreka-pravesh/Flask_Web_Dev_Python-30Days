from flask import Flask, request, render_template
app = Flask(__name__)
feedback_list = []
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        fb = request.form.get("fb")
        feedback_list.append(fb)
    return render_template("feedback.html", items=feedback_list)
if __name__ == "__main__":
    app.run(debug=True)
