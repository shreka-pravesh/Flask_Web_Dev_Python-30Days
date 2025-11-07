from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def mood_board():
    return render_template('mood_board.html')
if __name__ == '__main__':
    app.run(debug=True)
