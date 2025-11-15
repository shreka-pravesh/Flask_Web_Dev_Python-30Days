from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)
DB = "recipes.db"
with sqlite3.connect(DB) as c:
    c.execute("CREATE TABLE IF NOT EXISTS recipes (id INTEGER PRIMARY KEY, name TEXT, steps TEXT)")
@app.route('/')
def index():
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute("SELECT * FROM recipes"); recipes = cur.fetchall(); con.close()
    return render_template('recipes.html', recipes=recipes)
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']; steps = request.form['steps']
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute("INSERT INTO recipes (name, steps) VALUES (?, ?)", (name, steps))
    con.commit(); con.close()
    return redirect(url_for('index'))
@app.route('/delete/<int:id>')
def delete(id):
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute("DELETE FROM recipes WHERE id=?", (id,)); con.commit(); con.close()
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
