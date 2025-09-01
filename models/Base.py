from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Database connection string
DATABASE_URL = "sqlite:///bike_rental.db"  # Update as needed

# Create an engine that stores data in the local directory's bike_rental.db file
engine = create_engine(DATABASE_URL, echo=True)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables in the database (this will create the tables defined in your models)
Base.metadata.create_all(bind=engine)
