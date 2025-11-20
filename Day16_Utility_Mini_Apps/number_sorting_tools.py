from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def sort_numbers():
    result = []
    if request.method == "POST":
        nums = request.form.get("numbers")
        if nums:
            try:
                lst = list(map(int, nums.split(",")))
                result = sorted(lst)
            except:
                result = ["Invalid input"]
    return render_template("sort.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)
