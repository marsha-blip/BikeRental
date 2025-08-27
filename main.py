from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from services.userservice import UserService
from services.bikeservice import BikeService
from services.rentalservice import RentalService
from services.stationservice import StationService

def validate_int_input(prompt):
    """Helper function to validate integer input."""
    while True:
        try:
            value = input(prompt).strip()
            return int(value)
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("=== Bike Hire System ===")

    # Initialize SQLAlchemy session
    engine = create_engine('sqlite:///bike_rental.db', echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Initialize service instances
    try:
        user_service = UserService(session)
        bike_service = BikeService(session)
        rental_service = RentalService(session)
        station_service = StationService(session)
    except Exception as e:
        print(f"Error initializing services: {e}")
        session.close()
        return

    while True:
        print("\nWhat would you like to do?")
        print("1. Add Bike")
        print("2. Register User")
        print("3. Rent Bike")
        print("4. Return Bike")
        print("5. List All Rentals")
        print("6. Add Station")
        print("7. List Stations")
        print("8. Delete Bike")
        print("9. List All Users")
        print("10. Delete User")
        print("11. Delete Station")
        print("12. Exit")

        choice = input("Enter choice number: ").strip()

        try:
            if choice == "1":
                serial = input("Bike Serial Number: ").strip()
                model = input("Bike Model: ").strip()
                if not serial or not model:
                    print("Serial number and model cannot be empty.")
                    continue
                bike = bike_service.add_bike(serial, model)
                print(bike.print_bike_details())

            elif choice == "2":
                name = input("User Name: ").strip()
                email = input("User Email: ").strip()
                if not name or not email:
                    print("Name and email cannot be empty.")
                    continue
                new_user = user_service.register_user(name, email)
                print(f"User {new_user.name} registered successfully – ID {new_user.id}, "
                      f"Email {new_user.email}, Registered at {new_user.register_at}")

            elif choice == "3":
                user_id = validate_int_input("User ID renting the bike: ")
                bike_id = validate_int_input("Bike ID to rent: ")
                rental = rental_service.rent_bike(user_id, bike_id)
                print(f"Rental started – ID {rental.id}, User {rental.user_id}, Bike {rental.bike_id}")

            elif choice == "4":
                rental_id = validate_int_input("Rental ID to close: ")
                closed = rental_service.close_rental(rental_id)
                print(f"Rental closed – Fee: {closed.fee_cents / 100:.2f}")

            elif choice == "5":
                rentals = rental_service.list_all_rentals()
                if not rentals:
                    print("No rentals found.")
                else:
                    for r in rentals:
                        print(f"ID {r.id}, User {r.user_id}, Bike {r.bike_id}, "
                              f"Start: {r.start_time}, End: {r.end_time or 'Active'}, "
                              f"Fee: {(r.fee_cents / 100) if r.fee_cents else 0:.2f}")

            elif choice == "6":
                name = input("Station Name: ").strip()
                location = input("Station Location: ").strip()
                if not name or not location:
                    print("Name and location cannot be empty.")
                    continue
                station = station_service.add_station(name, location)
                print(f"Station added – ID {station.id}, Name {station.name}, Location {station.location}")

            elif choice == "7":
                stations = station_service.list_stations()
                if not stations:
                    print("No stations found.")
                else:
                    for s in stations:
                        print(f"ID {s.id}, Name {s.name}, Location {s.location}")

            elif choice == "8":
                bike_id = validate_int_input("Bike ID to delete: ")
                bike_service.delete_bike(bike_id)
                print(f"Bike with ID {bike_id} deleted successfully.")

            elif choice == "9":
                users = user_service.list_all_users()
                if not users:
                    print("No users found.")
                else:
                    for user in users:
                        print(f"User: {user.name}, Email: {user.email}, ID: {user.id}, "
                              f"Registered at {user.register_at}")

            elif choice == "10":
                user_id = validate_int_input("User ID to delete: ")
                user_service.delete_user(user_id)
                print(f"User with ID {user_id} deleted successfully.")

            elif choice == "11":
                station_id = validate_int_input("Station ID to delete: ")
                station_service.delete_station(station_id)
                print(f"Station with ID {station_id} deleted successfully.")

            elif choice == "12":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please select a number from 1 to 12.")

        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # Commit session after each operation to ensure data consistency
            session.commit()

    # Close session when exiting
    session.close()

if __name__ == "__main__":
    main()