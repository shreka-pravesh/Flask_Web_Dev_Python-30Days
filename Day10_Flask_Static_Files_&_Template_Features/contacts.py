from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)
DB = "contacts.db"
with sqlite3.connect(DB) as c:
    c.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name TEXT, phone TEXT)")
@app.route('/')
def index():
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute("SELECT * FROM contacts"); rows = cur.fetchall(); con.close()
    return render_template('contacts.html', contacts=rows)
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']; phone = request.form['phone']
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
    con.commit(); con.close()
    return redirect(url_for('index'))
@app.route('/delete/<int:id>')
def delete(id):
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute("DELETE FROM contacts WHERE id=?", (id,))
    con.commit(); con.close()
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
