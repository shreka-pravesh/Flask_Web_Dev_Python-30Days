from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)
with sqlite3.connect("feedback.db") as con:
    con.execute("CREATE TABLE IF NOT EXISTS feedback (id INTEGER PRIMARY KEY, name TEXT, message TEXT)")
@app.route('/')
def home():
    con = sqlite3.connect("feedback.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM feedback")
    data = cur.fetchall()
    con.close()
    return render_template('feedback.html', feedbacks=data)
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    message = request.form['message']
    con = sqlite3.connect("feedback.db")
    cur = con.cursor()
    cur.execute("INSERT INTO feedback (name, message) VALUES (?, ?)", (name, message))
    con.commit()
    con.close()
    return "Feedback submitted successfully!"
if __name__ == '__main__':
    app.run(debug=True)
