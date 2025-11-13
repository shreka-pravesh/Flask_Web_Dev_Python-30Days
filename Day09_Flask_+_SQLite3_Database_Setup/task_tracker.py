from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)
with sqlite3.connect("tasks.db") as con:
    con.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT)")
@app.route('/')
def home():
    con = sqlite3.connect("tasks.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM tasks")
    data = cur.fetchall()
    con.close()
    return render_template('tasks.html', tasks=data)
@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    con = sqlite3.connect("tasks.db")
    cur = con.cursor()
    cur.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    con.commit()
    con.close()
    return "Task Added!"
if __name__ == '__main__':
    app.run(debug=True)
