from flask import Flask, render_template, request, redirect, jsonify
import sqlite3

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = 'my-secret-key'
app.config['SESSION_TYPE'] = 'filesystem'

conn = sqlite3.connect('collection.db')

@app.route('/', methods=['GET', 'POST'])
def index():

    if(request.method == "POST"):
        email = request.form['email']
        password = request.form['password']

        if(email == "a@b.com" and password == "pass"):
            return jsonify({"text": "Hello World"});
        else:
            return "Hello"

    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():

    if(request.method == "POST"):
        data = request.get_json()
        email = data['email']
        password = data['password']

        cur = conn.execute("SELECT * FROM `users` WHERE `email` = '" + email + "'")
        data = cur.fetchall()
        
        if len(data) > 0:
            if(data[0][1] == password):
                return jsonify({"status": "Login successful!"})
            else:
                return jsonify({"status": "Incorrect password!"})
        else:
            return jsonify({"status": "Account does not exist!"})
