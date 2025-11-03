from flask import Flask 
app = Flask(__name__)
@app.route('/')
def home():
    return '<h2>Home Page</h2><a href="/contact">Go to Contact</a>'
@app.route('/contact')
def contact():
    return '<h2>Contact Page</h2><a href="/">Back to Home</a>'
if __name__ == '__main__':
    app.run()
    
