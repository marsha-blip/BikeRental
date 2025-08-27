from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Rental(Base):
    
    _tablename_ = 'rentals'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    bike_id = Column(Integer, ForeignKey('bikes.id'), nullable=False)
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime, nullable=True)
    fee_cents = Column(Integer, nullable=True)

    def _repr_(self):
        return f"<Rental(id={self.id}, user_id={self.user_id}, bike_id={self.bike_id})>"
