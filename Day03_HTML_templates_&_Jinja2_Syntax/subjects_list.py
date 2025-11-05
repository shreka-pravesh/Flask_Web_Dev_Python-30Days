from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def subjects():
    subject_list = ["Python", "Flask", "HTML", "CSS", "SQL"]
    return render_template('subjects.html', subjects=subject_list)
if __name__ == '__main__':
    app.run()
