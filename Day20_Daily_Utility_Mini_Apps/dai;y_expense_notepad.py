from flask import Flask, request, render_template
app = Flask(__name__)
saved_note = ""  
@app.route("/", methods=["GET", "POST"])
def home():
    global saved_note
    if request.method == "POST":
        saved_note = request.form.get("note")
    return render_template("index.html", note=saved_note)
if __name__ == "__main__":
    app.run(debug=True)
