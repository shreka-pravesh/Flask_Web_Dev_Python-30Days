from flask import Flask, render_template
import requests
app = Flask(__name__)
API_URL = "https://dummyjson.com/products/1"
@app.route("/")
def home():
    try:
        response = requests.get(API_URL)
        data = response.json()

        product_name = data.get("title", "Unknown Product")
        price = data.get("price", "N/A")
        description = data.get("description", "No description available")

        return render_template(
            "product_price.html",
            product=product_name,
            price=price,
            description=description
        )
    except:
        return "Could not fetch price at the moment."
if __name__ == "__main__":
    app.run(debug=True)
