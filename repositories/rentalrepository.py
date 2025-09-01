from datetime import datetime
from sqlalchemy.orm import Session
from models.rental import Rental  

class RentalRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, bike_id: int, user_id: int, station_id: int) -> Rental:
        new = Rental(bike_id=bike_id, user_id=user_id, station_id=station_id)
        self.session.add(new)
        self.session.commit()
        return new

    def get_by_id(self, rental_id: int) -> Rental:
        return self.session.query(Rental).filter_by(id=rental_id).first()

    def end_rental(self, rental_id: int) -> None:
        Rental = self.get_by_id(rental_id)
        if Rental and Rental.returned_at is None:
            Rental.returned_at = datetime.utcnow()
            self.session.commit()

    def delete(self, rental_id: int) -> None:
        Rental = self.get_by_id(rental_id)
        if Rental:
            self.session.delete(Rental)
            self.session.commit()
