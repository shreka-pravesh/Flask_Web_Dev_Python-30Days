from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)
DB = "blog.db"
with sqlite3.connect(DB) as c:
    c.execute("CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, title TEXT, content TEXT)")
@app.route('/')
def index():
    con=sqlite3.connect(DB); cur=con.cursor()
    cur.execute("SELECT id,title,content FROM posts ORDER BY id DESC")
    posts = cur.fetchall(); con.close()
    return render_template('blog_index.html', posts=posts)
@app.route('/new', methods=['GET','POST'])
def new():
    if request.method=='POST':
        t = request.form['title']; c = request.form['content']
        con=sqlite3.connect(DB); cur=con.cursor()
        cur.execute("INSERT INTO posts (title,content) VALUES (?,?)",(t,c)); con.commit(); con.close()
        return redirect(url_for('index'))
    return render_template('blog_new.html')
if __name__=='__main__':
    app.run(debug=True)
