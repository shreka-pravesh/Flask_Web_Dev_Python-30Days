from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('form_redirect.html')
@app.route('/login', methods=['POST'])
def login():
    user = request.form['username']
    return redirect(url_for('profile', username=user))
@app.route('/profile/<username>')
def profile(username):
    return f"<h2>Welcome, {username}! 🎉 You’re now logged in.</h2>"
if __name__ == '__main__':
    app.run(debug=True)
