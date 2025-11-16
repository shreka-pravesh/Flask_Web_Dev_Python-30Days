from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = "cart123"
@app.route('/', methods=['GET', 'POST'])
def cart():
    if 'cart' not in session:
        session['cart'] = []
    if request.method == 'POST':
        item = request.form.get('item')
        session['cart'].append(item)
        session.modified = True
    return render_template("cart.html", cart=session['cart'])
if __name__ == '__main__':
    app.run(debug=True)
