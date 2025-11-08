from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('greeting_form.html')
@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['username']
    return f"<h2>Hello, {name}! Welcome to Flask Forms </h2>"
if __name__ == '__main__':
    app.run(debug=True)
