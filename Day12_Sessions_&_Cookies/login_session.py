from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = "replace_with_a_strong_secret"
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        session['user'] = user
        return redirect(url_for('profile'))
    if 'user' in session:
        return redirect(url_for('profile'))
    return render_template('login.html')
@app.route('/profile')
def profile():
    user = session.get('user')
    if not user:
        return redirect(url_for('login'))
    return render_template('profile.html', user=user)
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(debug=True)
