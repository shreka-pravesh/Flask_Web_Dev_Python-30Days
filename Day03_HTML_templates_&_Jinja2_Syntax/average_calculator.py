from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def average():
    marks = [85, 90, 78, 92, 88]
    avg = sum(marks) / len(marks)
    return render_template('average.html', marks=marks, avg=avg)
if __name__ == '__main__':
    app.run()
