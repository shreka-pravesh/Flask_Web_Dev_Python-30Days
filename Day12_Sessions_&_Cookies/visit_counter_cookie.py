from flask import Flask, render_template
app = Flask(__name__)
visitor_count = 0
@app.route('/')
def counter():
    global visitor_count
    visitor_count += 1
    return render_template('Counter.html', count= visitor_count)
if __name__ == '__main__':
    app.run()
