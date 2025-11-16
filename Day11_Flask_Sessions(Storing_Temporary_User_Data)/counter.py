from flask import Flask, session, render_template
app = Flask(__name__)
app.secret_key = "day11secret"
@app.route('/')
def counter():
    session['count'] = session.get('count', 0) + 1
    return render_template("counter.html", count=session['count'])
if __name__ == '__main__':
    app.run(debug=True)
