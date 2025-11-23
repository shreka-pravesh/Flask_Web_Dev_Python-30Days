from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def convert_units():
    result = ""
    if request.method == "POST":
        value = float(request.form.get("value"))
        mode = request.form.get("mode")
        if mode == "km_to_miles":
            result = value * 0.621371
        else:
            result = value / 0.621371
    return render_template("index.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)
