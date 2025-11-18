from flask import Flask, render_template
import random
app = Flask(__name__)
@app.route("/")
def color():
    hex_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return render_template("color.html", color=hex_color)
if __name__ == "__main__":
    app.run(debug=True)
