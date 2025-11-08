from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def search_page():
    return render_template('search_bar.html')
@app.route('/result', methods=['GET'])
def result():
    query = request.args.get('query')
    return f"<h3>You searched for: <em>{query}</em></h3>"
if __name__ == '__main__':
    app.run(debug=True)
