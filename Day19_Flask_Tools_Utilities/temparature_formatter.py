from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def temp_tool():
    result = None
    if request.method == "POST":
        c = float(request.form["celsius"])
        f = (c * 9/5) + 32
        k = c + 273.15
        result = f"Fahrenheit: {f:.2f}, Kelvin: {k:.2f}"
    return render_template("index.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)
