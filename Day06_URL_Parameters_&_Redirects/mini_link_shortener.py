from flask import Flask, redirect
app = Flask(__name__)
links = {
    "gh": "https://github.com",
    "yt": "https://youtube.com",
    "py": "https://python.org"
}
@app.route('/go/<code>')
def go(code):
    if code in links:
        return redirect(links[code])
    else:
        return "<h3>Invalid code </h3>"
if __name__ == '__main__':
    app.run(debug=True)
