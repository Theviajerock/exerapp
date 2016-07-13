from flask import Flask, render_template, g, session, request, redirect, url_for, escape
import sqlite3

app = Flask(__name__)

@app.before_request
def before_request():
    g.db = sqlite3.connect('db.db')

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.commit()
        g.db.close()

@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "POST":
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        query = g.db.execute('SELECT * FROM USERS WHERE USERNAME = ?;',[username]).fetchall()
        if len(query) > 0:
            base = "base_not_logged.html"
            return render_template('index.html', base=base)
        else:
            session['email'] = email
            session['username'] = username
            session['password'] = username
            g.db.execute('INSERT INTO USERS(USERNAME, PASSWORD, EMAIL) VALUES(?,?,?);', [username, password, email])
            a = g.db.execute('SELECT * FROM USERS').fetchall()
            print(a)
            base = "base_logged.html"
            print(base)
            username = session['username']
            return render_template('index.html', base=base, username=username)
    if 'username' in session:
        base = "base_logged.html"
        username = session['username']
        return render_template("index.html", base=base, username=username)
    else:
        base = "base_not_logged.html"
        return render_template("index.html", base=base)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

app.secret_key = 'victorhernandez'

@app.route('/login')
def login():
    return "hola"

app.run(debug=True)
