from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def split():
    result = None
    if request.method == "POST":
        total = float(request.form["amount"])
        people = int(request.form["people"])
        per_head = total / people
        result = f"Each person pays: ₹{per_head:.2f}"
    return render_template("index.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)
