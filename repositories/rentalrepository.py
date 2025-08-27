from sqlalchemy.exc import IntegrityError
from models.rental import Rental
from datetime import datetime

class RentalRepository:
    def _init_(self, session):
        self.session = session

    def add(self, user_id, bike_id):
        """Add a new rental to the database."""
        try:
            rental = Rental(user_id=user_id, bike_id=bike_id)
            self.session.add(rental)
            self.session.commit()
            return rental
        except IntegrityError:
            self.session.rollback()
            raise ValueError("Error creating rental")

    def get_by_id(self, rental_id):
        """Retrieve a rental by ID."""
        return self.session.query(Rental).filter_by(id=rental_id).first()

    def get_active_by_bike_id(self, bike_id):
        """Retrieve an active rental for a bike (end_time is NULL)."""
        return self.session.query(Rental).filter_by(bike_id=bike_id, end_time=None).first()

    def close(self, rental_id):
        """Close a rental by setting end_time and calculating fee."""
        rental = self.get_by_id(rental_id)
        if not rental:
            raise ValueError("Rental not found")
        if rental.end_time:
            raise ValueError("Rental already closed")
        rental.end_time = datetime.utcnow()
        # Simple fee calculation: $0.10 per minute
        duration_minutes = (rental.end_time - rental.start_time).total_seconds() / 60
        rental.fee_cents = int(duration_minutes * 10)  # 10 cents per minute
        self.session.commit()
        return rental

    def list_all(self):
        """List all rentals."""
        return self.session.query(Rental).all()