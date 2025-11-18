from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = "day14-secret-key"  
@app.route('/', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username','').strip()
        email = request.form.get('email','').strip()
        if not username or len(username) < 3:
            flash("Username must be at least 3 characters.", "error")
            return redirect(url_for('signup'))
        if '@' not in email or '.' not in email:
            flash("Please enter a valid email address.", "error")
            return redirect(url_for('signup'))
        flash(f"Welcome, {username}! Signup successful.", "success")
        return redirect(url_for('signup'))
    return render_template('signup.html')
if __name__ == '__main__':
    app.run(debug=True)
