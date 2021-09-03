from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
	__tablename__ = "flights"
	id = db.Column(db.Integer, primary_key=True)
	origin = db.Column(db.String, nullable=False)
	destination = db.Column(db.String, nullable=False)
	duration = db.Column(db.Integer, nullable=False)

	def __str__(self):
		return f"Added Flight from {self.origin} to {self.destination} lasting {self.duration}"

class Passenger(db.Model):
	__tablename__ = "passengers"
	name = db.Column(db.String, nullable=False)
	id = db.Column(db.Integer, primary_key=True)
	flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
