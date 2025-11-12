from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/api/user')
def get_user():
    user = {
        "name": "Leena Pravesh",
        "age": 21,
        "email": "leena@example.com",
        "skills": ["Python", "Flask", "HTML"]
    }
    return jsonify(user)
if __name__ == '__main__':
    app.run(debug=True)
