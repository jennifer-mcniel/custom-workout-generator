from flask import Flask, render_template, redirect, url_for, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route("/workout")
def hello_world():
    return render_template("workout-form.html")

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return render_template("login.html")
    

if __name__ == '__main__':
    app.run()