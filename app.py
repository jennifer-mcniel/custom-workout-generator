from flask import Flask, render_template, redirect, url_for, request
from markupsafe import escape
from controller import generate_workout

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/api/generate-workout', methods=['POST'])
def workout_controller():
    return generate_workout(request)

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