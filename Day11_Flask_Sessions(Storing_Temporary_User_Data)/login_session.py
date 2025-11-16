from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = "sessionlogin"
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        session['user'] = request.form.get("username")
        return redirect('/dashboard')
    return render_template("login_form.html")
@app.route('/dashboard')
def dashboard():
    user = session.get("user")
    return render_template("dashboard.html", user=user)
if __name__ == '__main__':
    app.run(debug=True)
