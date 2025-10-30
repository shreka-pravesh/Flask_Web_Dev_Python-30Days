from flask import Flask
app = Flask(__name__)
@app.route('/hello/<username>')
def hello_user(username):
    return f"Hello {username}!"
if __name__ == '__main__':
    app.run()
