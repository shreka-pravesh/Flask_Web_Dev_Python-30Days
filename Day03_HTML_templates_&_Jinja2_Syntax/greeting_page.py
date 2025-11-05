from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def greet():
    name = "Shreka"
    time = "Morning"
    return render_template('greeting.html', name=name, time=time)
if __name__ == '__main__':
    app.run()
