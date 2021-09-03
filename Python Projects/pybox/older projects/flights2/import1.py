import csv
import os

from flask import Flask, render_template, request
from model import *

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:dhruvrishi123@localhost:5432/lecture4"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db.init_app(app)

def main():
	f = open("fl.csv")
	reader = csv.reader(f)

	for origin, destination, duration in reader:
		flight = Flight(origin=origin, destination=destination, duration=duration)
		db.session.add(flight)
		print(flight)
	db.session.commit()

if __name__ == "__main__":
	with app.app_context():
		main()