from repositories.rental_repository import RentalRepository
from repositories.user_repository import UserRepository
from repositories.bike_repository import BikeRepository

class RentalService:
    def _init_(self, session):
        self.rental_repository = RentalRepository(session)
        self.user_repository = UserRepository(session)
        self.bike_repository = BikeRepository(session)

    def rent_bike(self, user_id, bike_id):
        """Rent a bike to a user."""
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        bike = self.bike_repository.get_by_id(bike_id)
        if not bike:
            raise ValueError("Bike not found")
        active_rental = self.rental_repository.get_active_by_bike_id(bike_id)
        if active_rental:
            raise ValueError("Bike is already rented")
        return self.rental_repository.add(user_id, bike_id)

    def close_rental(self, rental_id):
        """Close a rental and calculate fee."""
        return self.rental_repository.close(rental_id)

    def list_all_rentals(self):
        """List all rentals."""
        return self.rental_repository.list_all()