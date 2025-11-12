from flask import Flask, render_template
import requests
app = Flask(__name__)
@app.route('/')
def convert():
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    data = response.json()
    inr_rate = data["rates"]["INR"]
    return render_template("currency.html", rate=inr_rate)
if __name__ == '__main__':
    app.run(debug=True)
