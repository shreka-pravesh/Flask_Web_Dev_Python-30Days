from flask import Flask, render_template, redirect, url_for, session, request
app = Flask(__name__)
app.secret_key = "replace_with_a_strong_secret"
@app.route('/')
def home():
    theme = session.get('theme', 'light')
    return render_template('theme_switcher.html', theme=theme)
@app.route('/toggle')
def toggle():
    current = session.get('theme', 'light')
    session['theme'] = 'dark' if current == 'light' else 'light'
    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=True)
