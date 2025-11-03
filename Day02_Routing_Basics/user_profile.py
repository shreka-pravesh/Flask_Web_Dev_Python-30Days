from flask import Flask
app = Flask(__name__)
@app.route('/user/<ussername>')
def user_profile(username):
    return f"<h2>Welcome, {username}!</h2>"
if __name__ == '__main__':
    app.run()
