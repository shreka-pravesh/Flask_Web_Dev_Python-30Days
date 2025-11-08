from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def feedback_page():
    return render_template('feedback_form.html')
@app.route('/submit', methods=['POST'])
def submit_feedback():
    feedback = request.form['feedback']
    return f"<h3>Thanks for your feedback! You said: {feedback}</h3>"
if __name__ == '__main__':
    app.run(debug=True)
