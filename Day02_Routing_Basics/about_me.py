from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def about():
    name = "Shreka Pravesh"
    hobby = "Cooking & Playing Badminton"
    return render_template('about.html', name=name, hobby=hobby)
if __name__ == '__main__':
    app.run(debug=True)
