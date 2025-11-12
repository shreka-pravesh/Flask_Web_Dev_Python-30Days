from flask import Flask, render_template
import requests
app = Flask(__name__)
@app.route('/')
def home():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    data = response.json()
    price = data["bpi"]["USD"]["rate"]
    time = data["time"]["updated"]
    return render_template("crypto.html", price=price, time=time)
if __name__ == '__main__':
    app.run(debug=True)
