from flask import Flask
app = Flask(__name__)
@app.route('/')
def hoem ():
    return "Hoem Page"
@app.route('/about')
def about():
    return "About Page"
@app.route('/contact')
def contact():
    return "Contact Page"
if __name__ == '__main__':
    app.run

    
