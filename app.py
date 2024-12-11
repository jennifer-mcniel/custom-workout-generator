from flask import Flask, render_template, redirect, url_for, request, jsonify
from markupsafe import escape
from controller import generate_workout
from workoutsDB import create_table, json_to_insert, read_and_process_json

app = Flask(__name__)

# set up database
create_table()
read_and_process_json('./exercise10.json')

@app.route('/')
def index():
    return render_template('home.html')

@app.post('/api/generate-workout')
def workout_controller():
    try:
        # Extract JSON data from the request
        user_input = request.get_json()

        if not user_input:
            return jsonify({"error": "Invalid input. Please provide a valid JSON payload."}), 400

        # Pass the extracted data to the generate_workout function
        response = generate_workout(user_input)

        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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