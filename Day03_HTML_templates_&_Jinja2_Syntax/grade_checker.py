from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def grade():
    marks = 96
    return render_template('grade.html', marks=marks)
if __name__ == '__main__':
    app.run()
