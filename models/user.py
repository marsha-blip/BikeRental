from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from models.Base import Base

class User(Base):

    __tablename__ = 'users' 
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    register_at = Column(DateTime, default=datetime.utcnow)

    def _repr_(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"
