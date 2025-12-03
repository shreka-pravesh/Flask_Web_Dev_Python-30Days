from flask import Flask, request, render_template_string
app = Flask(__name__)
HTML = """
<form method='POST'>
<textarea name='text' rows='5' cols='40' placeholder='Enter text...'></textarea><br><br>
<button type='submit'>Summarize</button>
</form>
{% if summary %}
<h3>Summary:</h3>
<p>{{ summary }}</p>
{% endif %}
"""
def summarize(text):
    sentences = text.split('.')
    if len(sentences) <= 2:
        return text
    return sentences[0] + "." + sentences[-2] + "."
@app.route("/", methods=["GET","POST"])
def index():
    summary = None
    if request.method == "POST":
        text = request.form.get("text","")
        summary = summarize(text)
    return render_template_string(HTML, summary=summary)
if __name__ == "__main__":
    app.run(debug=True)
