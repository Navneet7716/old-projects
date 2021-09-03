from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
	__tablename__ = "userlist"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)

	def __init__(self, username, password):
		self.username = username
		self.password = password 


class Notes(db.Model):
	__tablename__ = "notes"
	title = db.Column(db.String, nullable=False)
	content = db.Column(db.String, nullable=False)
	id = db.Column(db.Integer, primary_key=True)
	notes_id = db.Column(db.Integer, db.ForeignKey("userlist.id"), nullable=False)

	def __init__(self, title, content, notes_id):
		self.title = title
		self.content = content
		self.notes_id = notes_id