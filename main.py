# main.py
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import bike, user, station, rental
from services.bikeservice import BikeService
from services.stationservice import StationService
from services.userservice import UserService
from services.rentalservice import RentalService
from models.Base import Base

DATABASE_URL = 'sqlite:///bike_rental.db'

def setup_db():
    engine = create_engine(DATABASE_URL, echo=True)
    Base.metadata.create_all(bind=engine)
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

def print_menu():
    print("\n=== Bike Rental System CLI ===")
    print("1. Add Bike")
    print("2. Delete Bike")
    print("3. Add Station")
    print("4. Delete Station")
    print("5. Add User")
    print("6. Delete User")
    print("7. Start Rental")
    print("8. End Rental")
    print("9. Exit")

def main():
    SessionLocal = setup_db()
    session = SessionLocal()
    bike_svc = BikeService(session)
    station_svc = StationService(session)
    user_svc = UserService(session)
    rental_svc = RentalService(session)

    while True:
        print_menu()
        choice = input("Enter choice number: ").strip()

        if choice == '1':
            serial = input("Bike Serial Number: ").strip()
            model = input("Bike Model: ").strip()
            if serial and model:
                bike = bike_svc.add_bike(serial, model)
                print(f"Added Bike – ID: {bike.id}, Serial: {bike.serial_number}, Model: {bike.model}")
            else:
                print("Both serial number and model are required.")

        elif choice == '2':
            bike_id = input("Bike ID to delete: ").strip()
            if bike_id.isdigit():
                bike_svc.delete_bike(int(bike_id))
                print(f"Bike ID {bike_id} deleted (if existed).")
            else:
                print("Invalid ID entered.")

        elif choice == '3':
            name = input("Station Name: ").strip()
            location = input("Station Location: ").strip()
            if name and location:
                station = station_svc.add_station(name, location)
                print(f"Added Station – ID: {station.id}, Name: {station.name}, Location: {station.location}")
            else:
                print("Station name and location are required.")

        elif choice == '4':
            station_id = input("Station ID to delete: ").strip()
            if station_id.isdigit():
                station_svc.delete_station(int(station_id))
                print(f"Station ID {station_id} deleted (if existed).")
            else:
                print("Invalid ID entered.")

        elif choice == '5':
            username = input("Username: ").strip()
            email = input("Email: ").strip()
            if username and email:
                user = user_svc.add_user(username, email)
                print(f"Added User – ID: {user.id}, Username: {user.username}, Email: {user.email}")
            else:
                print("Both username and email are required.")

        elif choice == '6':
            user_id = input("User ID to delete: ").strip()
            if user_id.isdigit():
                user_svc.delete_user(int(user_id))
                print(f"User ID {user_id} deleted (if existed).")
            else:
                print("Invalid ID entered.")

        elif choice == '7':
            bike_id = input("Bike ID: ").strip()
            user_id = input("User ID: ").strip()
            station_id = input("Station ID: ").strip()
            if bike_id.isdigit() and user_id.isdigit() and station_id.isdigit():
                rental = rental_svc.add_rental(int(bike_id), int(user_id), int(station_id))
                print(f"Rental started – ID: {rental.id}, Bike: {rental.bike_id}, User: {rental.user_id}, Station: {rental.station_id}")
            else:
                print("All IDs must be valid numbers.")

        elif choice == '8':
            rental_id = input("Rental ID to end: ").strip()
            if rental_id.isdigit():
                rental_svc.end_rental(int(rental_id))
                print(f"Rental ID {rental_id} ended (if active).")
            else:
                print("Invalid ID entered.")

        elif choice == '9':
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a valid number.")

        session.commit()  # Ensure changes are persisted

    session.close()

if __name__ == "__main__":
    main()
