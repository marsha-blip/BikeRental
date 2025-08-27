from sqlalchemy.exc import IntegrityError
from models.bike import Bike

class BikeRepository:
    def _init_(self, session):
        self.session = session

    def add(self, serial_number, model):
        """Add a new bike to the database."""
        try:
            bike = Bike(serial_number=serial_number, model=model)
            self.session.add(bike)
            self.session.commit()
            return bike
        except IntegrityError:
            self.session.rollback()
            raise ValueError("Serial number already exists")

    def get_by_id(self, bike_id):
        """Retrieve a bike by ID."""
        return self.session.query(Bike).filter_by(id=bike_id).first()

    def delete(self, bike_id):
        """Delete a bike by ID."""
        bike = self.get_by_id(bike_id)
        if not bike:
            raise ValueError("Bike not found")
        self.session.delete(bike)
        self.session.commit()