from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)
with sqlite3.connect("students.db") as con:
    con.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, grade TEXT)")
@app.route('/')
def home():
    con = sqlite3.connect("students.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    con.close()
    return render_template('students.html', students=data)
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    grade = request.form['grade']
    con = sqlite3.connect("students.db")
    cur = con.cursor()
    cur.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (name, grade))
    con.commit()
    con.close()
    return "Student Record Added!"
if __name__ == '__main__':
    app.run(debug=True)
