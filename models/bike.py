from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Bike(Base):
    
    _tablename_ = 'bikes'

    id = Column(Integer, primary_key=True)
    serial_number = Column(String, nullable=False, unique=True)
    model = Column(String, nullable=False)

    def print_bike_details(self):
        return f"Bike registered – ID {self.id}, Serial {self.serial_number}, Model {self.model}"

    def _repr_(self):
        return f"<Bike(id={self.id}, serial_number={self.serial_number})>"