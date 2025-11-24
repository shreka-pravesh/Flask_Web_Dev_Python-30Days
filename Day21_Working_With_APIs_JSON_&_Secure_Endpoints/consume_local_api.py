from flask import Flask, jsonify
import requests
app = Flask(__name__)
@app.route("/get-local-tip")
def get_local_tip():
    url = "http://127.0.0.1:5001/demo-tip"
    response = requests.get(url).json()
    return jsonify({"received_from_other_api": response})
if __name__ == "__main__":
    app.run(port=5002, debug=True)
