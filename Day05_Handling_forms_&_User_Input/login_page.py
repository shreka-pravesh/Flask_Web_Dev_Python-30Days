from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def login_page():
    return render_template('login_page.html')
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == "admin" and password == "1234":
        return "<h2>Login successful! </h2>"
    else:
        return "<h3>Invalid credentials. Try again </h3>"
if __name__ == '__main__':
    app.run(debug=True)
