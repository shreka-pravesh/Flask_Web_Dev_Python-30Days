from flask import Flask, render_template, request, flash, redirect, url_for
app = Flask(__name__)
app.secret_key = "pass-key"
def check_strength(pw):
    errors = []
    if len(pw) < 8:
        errors.append("Password must be at least 8 characters.")
    if not any(c.isdigit() for c in pw):
        errors.append("Include at least one digit.")
    if not any(c.isalpha() for c in pw):
        errors.append("Include at least one letter.")
    return errors
@app.route('/', methods=['GET','POST'])
def pwcheck():
    if request.method == 'POST':
        pw = request.form.get('password','')
        errors = check_strength(pw)
        if errors:
            for e in errors:
                flash(e, "error")
        else:
            flash("Strong password ", "success")
        return redirect(url_for('pwcheck'))
    return render_template('password.html')
if __name__ == '__main__':
    app.run(debug=True)
