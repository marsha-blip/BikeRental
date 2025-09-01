from repositories.rentalrepository import RentalRepository

class RentalService:
    def __init__(self, session):
        self.rental_repository = RentalRepository(session)

    def add_rental(self, bike_id: int, user_id: int, station_id: int):
        """Create a new rental record."""
        return self.rental_repository.add(bike_id, user_id, station_id)

    def get_rental(self, rental_id: int):
        """Retrieve a rental by its ID."""
        return self.rental_repository.get_by_id(rental_id)

    def end_rental(self, rental_id: int):
        """Mark a rental as returned."""
        self.rental_repository.end_rental(rental_id)

    def delete_rental(self, rental_id: int):
        """Delete a rental record."""
        self.rental_repository.delete(rental_id)
