from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)
DB = "snippets.db"
with sqlite3.connect(DB) as c:
    c.execute("CREATE TABLE IF NOT EXISTS snippets (id INTEGER PRIMARY KEY, title TEXT, lang TEXT, code TEXT)")
@app.route('/')
def index():
    con=sqlite3.connect(DB); cur=con.cursor()
    cur.execute("SELECT * FROM snippets ORDER BY id DESC"); data=cur.fetchall(); con.close()
    return render_template('snippets.html', snippets=data)
@app.route('/add', methods=['POST'])
def add():
    title=request.form['title']; lang=request.form['lang']; code=request.form['code']
    con=sqlite3.connect(DB); cur=con.cursor()
    cur.execute("INSERT INTO snippets (title,lang,code) VALUES (?,?,?)",(title,lang,code)); con.commit(); con.close()
    return redirect(url_for('index'))
@app.route('/delete/<int:id>')
def delete(id):
    con=sqlite3.connect(DB); cur=con.cursor(); cur.execute("DELETE FROM snippets WHERE id=?", (id,)); con.commit(); con.close()
    return redirect(url_for('index'))
if __name__=='__main__':
    app.run(debug=True)
