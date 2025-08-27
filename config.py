from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.bike import Bike
from models.rental import Rental
from models.station import Station
from sqlalchemy.ext.declarative import declarative_base

# Create SQLAlchemy engine and session
engine = create_engine('sqlite:///bike_rental.db', echo=False)
Session = sessionmaker(bind=engine)

# Create tables (equivalent to previous schema setup)
Base = declarative_base()
Base.metadata.create_all(engine)
