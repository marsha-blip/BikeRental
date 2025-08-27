from repositories.bike_repository import BikeRepository

class BikeService:
    def _init_(self, session):
        self.repository = BikeRepository(session)

    def add_bike(self, serial_number, model):
        """Add a new bike."""
        if not serial_number or not model:
            raise ValueError("Serial number and model cannot be empty")
        return self.repository.add(serial_number, model)

    def delete_bike(self, bike_id):
        """Delete a bike."""
        return self.repository.delete(bike_id)
