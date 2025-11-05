from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def score():
    scores = {"Python": 88, "Flask": 89, "HTML": 92, "SQL": 85}
    return render_template('scores.html', scores=scores)
if __name__ == '__main__':
    app.run()
