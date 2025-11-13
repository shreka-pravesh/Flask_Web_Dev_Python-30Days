from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)
with sqlite3.connect("books.db") as con:
    con.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)")
@app.route('/')
def home():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM books")
    data = cur.fetchall()
    con.close()
    return render_template('books.html', books=data)
@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    author = request.form['author']
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    con.commit()
    con.close()
    return "Book added successfully!"
if __name__ == '__main__':
    app.run(debug=True)
