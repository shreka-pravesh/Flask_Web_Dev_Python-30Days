from flask import Flask 
app = Flask(__name__)
@app.route('/')
def demo():
    return "Debug mode is not working"
if __name__ == '__main__':
    app.run(debug = True)
