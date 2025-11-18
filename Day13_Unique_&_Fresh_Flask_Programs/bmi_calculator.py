from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def bmi():
    bmi_value = None
    if request.method == "POST":
        h = float(request.form["height"]) / 100
        w = float(request.form["weight"])
        bmi_value = round(w / (h * h), 2)
    return render_template("bmi.html", bmi=bmi_value)
if __name__ == "__main__":
    app.run(debug=True)
