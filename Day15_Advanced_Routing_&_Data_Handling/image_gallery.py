from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/', methods=['GET','POST'])
def gallery():
    if request.method == 'POST' and 'photo' in request.files:
        f = request.files['photo']
        if f.filename:
            path = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
            f.save(path)
        return redirect(url_for('gallery'))
    # list uploaded files
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    files = [f for f in files if not f.startswith('.')]
    return render_template('gallery.html', images=files)
if __name__=='__main__':
    app.run(debug=True)
