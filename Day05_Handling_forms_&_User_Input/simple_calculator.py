from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def calculator_page():
    return render_template('simple_calculator.html')
@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    total = num1 + num2
    return f"<h3>The sum of {num1} and {num2} is: {total}</h3>"
if __name__ == '__main__':
    app.run(debug=True)
