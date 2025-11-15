from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)
DB = "wishlist.db"
with sqlite3.connect(DB) as c:
    c.execute("CREATE TABLE IF NOT EXISTS wishlist (id INTEGER PRIMARY KEY, item TEXT, url TEXT)")
@app.route('/')
def index():
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute("SELECT * FROM wishlist"); items = cur.fetchall(); con.close()
    return render_template('wishlist.html', items=items)
@app.route('/add', methods=['POST'])
def add():
    item = request.form['item']; url = request.form.get('url','')
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute("INSERT INTO wishlist (item, url) VALUES (?, ?)", (item, url))
    con.commit(); con.close()
    return redirect(url_for('index'))
@app.route('/delete/<int:id>')
def delete(id):
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute("DELETE FROM wishlist WHERE id=?", (id,)); con.commit(); con.close()
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
