from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def theme_toggle():
    return render_template('theme_toggle.html')
if __name__ == '__main__':
    app.run(debug=True)
