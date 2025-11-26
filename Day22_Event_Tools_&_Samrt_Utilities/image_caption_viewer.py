from flask import Flask, render_template
app = Flask(__name__)
images = [
    {"url": "https://picsum.photos/300", "caption": "Random Scene"},
    {"url": "https://picsum.photos/301", "caption": "Nature Mood"},
    {"url": "https://picsum.photos/302", "caption": "Urban Street"},
]
@app.route("/")
def home():
    return render_template("viewer.html", images=images)
if __name__ == "__main__":
    app.run(debug=True)
