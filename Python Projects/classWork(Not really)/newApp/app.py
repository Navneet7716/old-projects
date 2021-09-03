from flask import Flask, session, redirect, url_for, render_template
from flask.globals import request

from markupsafe import escape


app = Flask(__name__)
app.secret_key = b'|(\xa0\x8d\xfb\xefZP\xbd~\xce\xe1\xd3A\x96\xb4\x04X\xa6,'


@app.route("/")
def index():
    if 'username' in session:
        return f"Logged in as {escape(session['username'])} <br> <a href='logout'>Logout</a>"
    return "<h1>You are not logged in </h1> <br><br> <a href='/login'>Login</a>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    else:
        return render_template("login.html")


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
