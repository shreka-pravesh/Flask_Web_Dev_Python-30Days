from flask import Flask, render_template, request, make_response
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def store_name():
    if request.method == 'POST':
        name = request.form.get('name')
        resp = make_response(render_template("cookie_saved.html", name=name))
        resp.set_cookie("username", name)
        return resp
    saved_name = request.cookies.get("username")
    return render_template("cookie_form.html", saved_name=saved_name)
if __name__ == '__main__':
    app.run(debug=True)
