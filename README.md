## BikeRental
# Project Overview

BikeRental is a Python-based application designed to manage bike rentals, including bike inventory, user management, station locations, and rental transactions. The system employs SQLAlchemy for ORM-based database interactions and follows a modular architecture for scalability and maintainability.

# Project Structure
BikeRental/
├── main.py                  # Entry point for the application
├── config.py                # Configuration settings
├── models/                  # Database models
│   ├── __init__.py
│   ├── bike.py
│   ├── rental.py
│   ├── station.py
│   └── user.py
├── repositories/            # Data access layer
│   ├── __init__.py
│   ├── bikerepository.py
│   ├── rentalrepository.py
│   ├── stationrepository.py
│   └── userrepository.py
└── services/                # Business logic layer
    ├── __init__.py
    ├── bikeservice.py
    ├── rentalservice.py
    ├── stationservice.py
    └── userservice.py

# Installation

Clone the repository:

git clone https://github.com/marsha-blip/BikeRental.git
cd BikeRental


# Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


# Install the required dependencies:

pip install -r requirements.txt


# Set up the database:

python main.py

Ensure that you have the necessary testing dependencies installed:

pip install -r requirements-dev.txt
# License

This project is licensed under the MIT License.
# Author 
# Mary Itumo
