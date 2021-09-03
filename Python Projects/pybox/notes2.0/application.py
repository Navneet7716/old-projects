import os

from flask import Flask, render_template, request, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from model import *

app = Flask(__name__)

engine = create_engine("postgresql://postgres:dhruvrishi123@localhost:5432/notes")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/", methods=["GET","POST"])
def signup():
	return render_template("signup.html")


@app.route("/success", methods=["POST"])
def success():
	if request.method == "POST":
		email = request.form.get('email')
		password = request.form.get('password')
		db.execute("INSERT INTO userlist (username, password) VALUES (:username, :password)", {"username":email,"password":password})
		db.session.commit()
		return render_template("raw.html", title="SUCCESS", message="HEY, YOUR ID IS CREATED!!")



@app.route("/login", methods=["GET", "POST"])
def login():
	return render_template("login.html")

@app.route("/login/users", methods=["POST","GET"])
def user():
	if request.method == "POST":
		email = request.form.get('email')
		password = request.form.get('password')
		y = db.execute("SELECT * FROM userlist WHERE password = :assword AND username = :mail", {"mail":email,"assword":password}).fetchone()
		if y == None:
			return render_template("raw.html", title="FAIL", message="USER DOESN'T EXISTS!")
		
		return redirect(url_for('note', user_id= y.id))


@app.route("/login/users/<int:user_id>", methods=["POST", "GET"])
def note(user_id):
	if request.method == "GET":
		t = request.form.get('title')
		c = request.form.get('content')
		data = Notes(t,c,user_id)
		db.session.add(data)
		db.session.commit()
		notes = data.query.filter_by(notes_id=user_id).all()
		#notels = db.execute("SELECT * FROM notes WHERE notes_id = :id", {"id": user_id}).fetchall()
		return render_template("note.html", notels=notes, u_id=user_id)
	

@app.route("/clear/<int:user_id>", methods=["POST"])
def clear(user_id):
	if request.method == "POST":
		db.execute("DELETE FROM notes WHERE notes_id=:user", {"user": user_id})
		db.session.commit()
		return redirect(url_for('note', user_id = user_id))







if __name__ == "__main__":
	app.run(debug=True)