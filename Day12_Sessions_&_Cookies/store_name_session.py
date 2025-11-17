from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = "replace_with_a_strong_secret"  # change before publishing
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        session['name'] = request.form['name']
        return redirect(url_for('home'))
    name = session.get('name')
    return render_template('store_name.html', name=name)
@app.route('/clear')
def clear():
    session.pop('name', None)
    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=True)
