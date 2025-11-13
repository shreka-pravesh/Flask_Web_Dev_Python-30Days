from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)
with sqlite3.connect("contacts.db") as con:
    con.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name TEXT, phone TEXT)")
@app.route('/')
def home():
    con = sqlite3.connect("contacts.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM contacts")
    data = cur.fetchall()
    con.close()
    return render_template('contacts.html', contacts=data)
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    phone = request.form['phone']
    con = sqlite3.connect("contacts.db")
    cur = con.cursor()
    cur.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
    con.commit()
    con.close()
    return "Contact Added Successfully!"
if __name__ == '__main__':
    app.run(debug=True)
