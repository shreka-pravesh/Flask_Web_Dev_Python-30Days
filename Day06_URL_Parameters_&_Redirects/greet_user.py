from flask import Flask
app = Flask(__name__)
@app.route('/user/<name>')
def user(name):
    return f"<h2>Hello, {name}!  Welcome to Flask URL parameters.</h2>"
if __name__ == '__main__':
    app.run(debug=True)
