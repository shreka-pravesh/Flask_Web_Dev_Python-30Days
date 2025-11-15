from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)
DB = "tasks.db"
with sqlite3.connect(DB) as c:
    c.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT, done INTEGER DEFAULT 0)")
@app.route('/')
def index():
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute("SELECT * FROM tasks"); tasks = cur.fetchall(); con.close()
    return render_template('tasks.html', tasks=tasks)
@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute("INSERT INTO tasks (title) VALUES (?)", (title,)); con.commit(); con.close()
    return redirect(url_for('index'))
@app.route('/toggle/<int:id>')
def toggle(id):
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute("SELECT done FROM tasks WHERE id=?", (id,)); done = cur.fetchone()[0]
    cur.execute("UPDATE tasks SET done=? WHERE id=?", (0 if done else 1, id))
    con.commit(); con.close()
    return redirect(url_for('index'))
@app.route('/delete/<int:id>')
def delete(id):
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute("DELETE FROM tasks WHERE id=?", (id,)); con.commit(); con.close()
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
