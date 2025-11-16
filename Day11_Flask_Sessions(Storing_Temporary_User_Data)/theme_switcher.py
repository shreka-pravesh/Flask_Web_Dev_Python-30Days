from flask import Flask, request, render_template, make_response
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def theme():
    if request.method == "POST":
        theme = request.form.get("theme")
        resp = make_response(render_template("theme_done.html", theme=theme))
        resp.set_cookie("theme", theme)
        return resp
    saved_theme = request.cookies.get("theme", "light")
    return render_template("theme_form.html", theme=saved_theme)
if __name__ == '__main__':
    app.run(debug=True)
