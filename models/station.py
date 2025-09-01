from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from models.Base import Base

class Station(Base):

    __tablename__ = 'stations'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

    def _repr_(self):
        return f"<Station(id={self.id}, name={self.name})>"
