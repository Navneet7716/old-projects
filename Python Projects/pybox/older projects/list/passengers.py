import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("postgresql://postgres:dhruvrishi123@localhost:5432/postgres")
db = scoped_session(sessionmaker(bind=engine))

def main():

	flights = db.execute("SELECT id, origin, destination, duration FROM flights").fetchall()
	for flight in flights:
		print(f"Flight {flight.id}: {flight.origin} to {flight.destination}, in {flight.duration} mins")

	flight_id = int(input("\nFlight ID: "))
	flight = db.execute("SELECT origin, destination, duration FROM flights WHERE id = :id", {"id":flight_id}).fetchone()

	if flight is None:
		print("ERROR: NO SUCH FLIGHT")
		return

	passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id", {"flight_id":flight_id}).fetchall()

	print("\nPassengers:")
	for p in passengers:
		print(p.name)
	if len(passengers) == 0:
		print("NULL")