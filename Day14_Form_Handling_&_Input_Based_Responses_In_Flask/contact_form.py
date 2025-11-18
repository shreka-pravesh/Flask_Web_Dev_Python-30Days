from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = "contact-key"
@app.route('/', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name','').strip()
        msg = request.form.get('message','').strip()
        if not name:
            flash("Please enter your name.", "error")
            return redirect(url_for('contact'))
        if len(msg) < 10:
            flash("Message must be at least 10 characters.", "error")
            return redirect(url_for('contact'))
        flash("Thank you — your message was sent.", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html')
if __name__ == '__main__':
    app.run(debug=True)
