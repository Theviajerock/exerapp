from flask import Flask, render_template, g, session, request, redirect, url_for, escape
import sqlite3

app = Flask(__name__)

@app.before_request
def before_request():
    g.db = sqlite3.connect('db.db')

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/', methods=["POST","GET"])
def index():
    if request.method=="POST":
        session['email'] = request.form['email']
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        base = "base_logged.html"
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

"""
@app.route('/register', methods=["POST","GET"])
def register():
    if request.method == "POST":
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        session['email'] = request.form['email']
        return redirect(url_for('index'))
    elif 'username' in session:
        return redirect(url_for('index'))
    else:
        base = "base_not_logged.html"
        return render_template('register.html', base=base)
"""

app.run(debug=True)
