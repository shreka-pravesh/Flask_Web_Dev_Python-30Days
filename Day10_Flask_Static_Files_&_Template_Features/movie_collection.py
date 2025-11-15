from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)
DB = "movies.db"
with sqlite3.connect(DB) as c:
    c.execute("CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, title TEXT, year INTEGER)")
@app.route('/')
def index():
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute("SELECT * FROM movies"); movies = cur.fetchall(); con.close()
    return render_template('movies.html', movies=movies)
@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']; year = request.form['year'] or None
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute("INSERT INTO movies (title, year) VALUES (?, ?)", (title, year))
    con.commit(); con.close()
    return redirect(url_for('index'))
@app.route('/delete/<int:id>')
def delete(id):
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute("DELETE FROM movies WHERE id=?", (id,)); con.commit(); con.close()
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
