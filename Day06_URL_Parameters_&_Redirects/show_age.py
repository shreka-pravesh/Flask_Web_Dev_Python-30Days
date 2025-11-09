from flask import Flask
app = Flask(__name__)
@app.route('/info/<name>/<int:age>')
def info(name, age):
    return f"<h3>{name} is {age} years old </h3>"
if __name__ == '__main__':
    app.run(debug=True)
