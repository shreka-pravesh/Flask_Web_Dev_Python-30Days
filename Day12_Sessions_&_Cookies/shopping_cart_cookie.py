from flask import Flask, request, make_response, redirect, url_for, render_template
import json
app = Flask(__name__)
def read_cart(req):
    raw = req.cookies.get('cart')
    if not raw:
        return []
    try:
        return json.loads(raw)
    except:
        return []
@app.route('/', methods=['GET'])
def index():
    cart = read_cart(request)
    return render_template('cart.html', cart=cart)
@app.route('/add', methods=['POST'])
def add():
    item = request.form['item']
    cart = read_cart(request)
    cart.append(item)
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('cart', json.dumps(cart), max_age=60*60*24*30)  # 30 days
    return resp
@app.route('/clear')
def clear():
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('cart', '', max_age=0)
    return resp
if __name__ == '__main__':
    app.run(debug=True)
