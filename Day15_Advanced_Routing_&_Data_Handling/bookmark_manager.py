from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)
DB = "bookmarks.db"
with sqlite3.connect(DB) as c:
    c.execute("CREATE TABLE IF NOT EXISTS bookmarks (id INTEGER PRIMARY KEY, title TEXT, url TEXT, tag TEXT)")
@app.route('/')
def index():
    con=sqlite3.connect(DB); cur=con.cursor()
    cur.execute("SELECT * FROM bookmarks ORDER BY id DESC"); data=cur.fetchall(); con.close()
    return render_template('bookmarks.html', bookmarks=data)
@app.route('/add', methods=['POST'])
def add():
    title=request.form['title']; url=request.form['url']; tag=request.form.get('tag','')
    con=sqlite3.connect(DB); cur=con.cursor()
    cur.execute("INSERT INTO bookmarks (title,url,tag) VALUES (?,?,?)",(title,url,tag)); con.commit(); con.close()
    return redirect(url_for('index'))
@app.route('/delete/<int:id>')
def delete(id):
    con=sqlite3.connect(DB); cur=con.cursor(); cur.execute("DELETE FROM bookmarks WHERE id=?", (id,)); con.commit(); con.close()
    return redirect(url_for('index'))
if __name__=='__main__':
    app.run(debug=True)
