from flask import Flask, request, redirect, render_template_string
import hashlib
app = Flask(__name__)
storage = {}
HTML = """
<form method='POST'>
<input name='url' placeholder='Enter URL...' size='40'>
<button type='submit'>Shorten</button>
</form>
{% if short %}
<p>Your short URL: <b>{{ short }}</b></p>
{% endif %}
"""
def create_short(url):
    short = hashlib.md5(url.encode()).hexdigest()[:6]
    storage[short] = url
    return short
@app.route("/", methods=["GET","POST"])
def home():
    short = None
    if request.method == "POST":
        long_url = request.form.get("url")
        code = create_short(long_url)
        short = request.host_url + code
    return render_template_string(HTML, short=short)
@app.route("/<code>")
def redirect_to_original(code):
    return redirect(storage.get(code, "/"))
if __name__ == "__main__":
    app.run(debug=True)
