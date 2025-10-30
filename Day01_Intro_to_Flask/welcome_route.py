from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "This is the Home Page"
@app.route('/welcome')
def welcome():
    return "Welcome to Flask!"
if __name__ == '__main__':
    app.run()
