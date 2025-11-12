from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
@app.route('/')
def form():
    return render_template('submit.html')
@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.to_dict()
    return jsonify({
        "status": "success",
        "message": f"Data received for {data.get('name')}"
    })
if __name__ == '__main__':
    app.run(debug=True)
