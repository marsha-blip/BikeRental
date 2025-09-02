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
    print("2. Get Bike")
    print("3. Delete Bike")
    print("4. Add Station")
    print("5. Update Station")
    print("6. Delete Station")
    print("7. Add User")
    print("8. Get User")
    print("9. Update User")
    print("10. Delete User")
    print("11. Start Rental")
    print("12. Delete Rental")
    print("13. End Rental")
    print("14. Exit")

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
                bike_obj = bike_svc.add_bike(serial, model)
                print(f"Added Bike – ID: {bike_obj.id}, Serial: {bike_obj.serial_number}, Model: {bike_obj.model}")
            else:
                print("Both serial number and model are required.")

        elif choice == '2':
            bike_id = input("Bike ID to fetch: ").strip()
            if bike_id.isdigit():
                bike_obj = bike_svc.get_bike(int(bike_id))
                if bike_obj:
                    print(f"Bike – ID: {bike_obj.id}, Serial: {bike_obj.serial_number}, Model: {bike_obj.model}")
                else:
                    print(f"No bike found with ID {bike_id}.")
            else:
                print("Invalid ID entered.")

        elif choice == '3':
            bike_id = input("Bike ID to delete: ").strip()
            if bike_id.isdigit():
                bike_svc.delete_bike(int(bike_id))
                print(f"Bike ID {bike_id} deleted (if existed).")
            else:
                print("Invalid ID entered.")

        elif choice == '4':
            name = input("Station Name: ").strip()
            location = input("Station Location: ").strip()
            if name and location:
                station_obj = station_svc.add_station(name, location)
                print(f"Added Station – ID: {station_obj.id}, Name: {station_obj.name}, Location: {station_obj.location}")
            else:
                print("Station name and location are required.")

        elif choice == '5':
            station_id = input("Station ID to update: ").strip()
            name = input("New Station Name (leave blank to keep current): ").strip()
            location = input("New Station Location (leave blank to keep current): ").strip()
            if station_id.isdigit():
                updated = station_svc.update_station(int(station_id), name or None, location or None)
                if updated:
                    print(f"Station ID {station_id} updated.")
                else:
                    print(f"No station found with ID {station_id}.")
            else:
                print("Invalid ID entered.")

        elif choice == '6':
            station_id = input("Station ID to delete: ").strip()
            if station_id.isdigit():
                station_svc.delete_station(int(station_id))
                print(f"Station ID {station_id} deleted (if existed).")
            else:
                print("Invalid ID entered.")

        elif choice == '7':
            username = input("Username: ").strip()
            email = input("Email: ").strip()
            if username and email:
                user_obj = user_svc.add_user(username, email)
                print(f"Added User – ID: {user_obj.id}, Username: {user_obj.username}, Email: {user_obj.email}")
            else:
                print("Both username and email are required.")

        elif choice == '8':
            user_id = input("User ID to fetch: ").strip()
            if user_id.isdigit():
                user_obj = user_svc.get_user(int(user_id))
                if user_obj:
                    print(f"User – ID: {user_obj.id}, Username: {user_obj.username}, Email: {user_obj.email}")
                else:
                    print(f"No user found with ID {user_id}.")
            else:
                print("Invalid ID entered.")

        elif choice == '9':
            user_id = input("User ID to update: ").strip()
            username = input("New Username (leave blank to keep current): ").strip()
            email = input("New Email (leave blank to keep current): ").strip()
            if user_id.isdigit():
                updated = user_svc.update_user(int(user_id), username or None, email or None)
                if updated:
                    print(f"User ID {user_id} updated.")
                else:
                    print(f"No user found with ID {user_id}.")
            else:
                print("Invalid ID entered.")

        elif choice == '10':
            user_id = input("User ID to delete: ").strip()
            if user_id.isdigit():
                user_svc.delete_user(int(user_id))
                print(f"User ID {user_id} deleted (if existed).")
            else:
                print("Invalid ID entered.")

        elif choice == '11':
            bike_id = input("Bike ID: ").strip()
            user_id = input("User ID: ").strip()
            station_id = input("Station ID: ").strip()
            if bike_id.isdigit() and user_id.isdigit() and station_id.isdigit():
                rental_obj = rental_svc.add_rental(int(bike_id), int(user_id), int(station_id))
                print(f"Rental started – ID: {rental_obj.id}, Bike: {rental_obj.bike_id}, User: {rental_obj.user_id}, Station: {rental_obj.station_id}")
            else:
                print("All IDs must be valid numbers.")

        elif choice == '12':
            rental_id = input("Rental ID to delete: ").strip()
            if rental_id.isdigit():
                deleted = rental_svc.delete_rental(int(rental_id))
                if deleted:
                    print(f"Rental ID {rental_id} deleted.")
                else:
                    print(f"No rental found with ID {rental_id}, or it was already ended.")
            else:
                print("Invalid ID entered.")

        elif choice == '13':
            rental_id = input("Rental ID to end: ").strip()
            if rental_id.isdigit():
                rental_svc.end_rental(int(rental_id))
                print(f"Rental ID {rental_id} ended (if active).")
            else:
                print("Invalid ID entered.")

        elif choice == '14':
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a valid number.")

        try:
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error while committing transaction: {e}")

    session.close()

if __name__ == "__main__":
    main()

