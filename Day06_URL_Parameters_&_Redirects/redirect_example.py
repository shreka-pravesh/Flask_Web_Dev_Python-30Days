from flask import Flask, redirect, url_for
app = Flask(__name__)
@app.route('/home')
def home():
    return redirect(url_for('welcome'))
@app.route('/welcome')
def welcome():
    return "<h2>Welcome! You’ve been redirected successfully </h2>"
if __name__ == '__main__':
    app.run(debug=True)
