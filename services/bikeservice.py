from repositories.bikerepository import BikeRepository

class BikeService:
    def __init__(self, session):
        self.bikerepository = BikeRepository(session)

    def add_bike(self, serial_number, model):
        """Add a new bike to the system."""
        return self.bikerepository.add(serial_number, model)

    def get_bike(self, bike_id):
        """Retrieve a bike by ID."""
        return self.bikerepository.get_by_id(bike_id)

    def delete_bike(self, bike_id):
        """Delete a bike by ID."""
        self.bikerepository.delete(bike_id)

