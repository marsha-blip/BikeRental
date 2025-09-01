from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from models.bike import Bike

class BikeRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, serial_number: str, model: str) -> Bike:
        """Add a new bike to the database."""
        new_bike = Bike(serial_number=serial_number, model=model)
        self.session.add(new_bike)
        self.session.commit()
        return new_bike

    def get_by_id(self, bike_id: int) -> Bike:
        """Retrieve a bike by its ID."""
        return self.session.query(Bike).filter_by(id=bike_id).first()

    def delete(self, bike_id: int) -> None:
        """Delete a bike by its ID."""
        Bike = self.get_by_id(bike_id)
        if Bike:
            self.session.delete(Bike)
            self.session.commit()
