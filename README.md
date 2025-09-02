<<<<<<< HEAD
## Bike Rental CLI

A simple, command-line interface (CLI) application for managing bike rentals using Python and SQLAlchemy.

## Table of Contents

. Overview

. Features

. Getting Started

. Prerequisites

. Installation

. Usage

. Project Structure

. Contributing

. License

## Overview

This project implements a simple CLI application for a bike rental system. It lets users add and manage bikes, stations, users, and rentals using a SQLite database with SQLAlchemy ORM as the underlying persistence layer.

## Features

1. Add, retrieve, and delete Bikes

2. Add, update, and delete Stations

3. Add, retrieve, update, and delete Users

4. Start, end, and delete Rentals

5. Interactive text-based menu driven by user input

## Getting Started
Prerequisites

Python 3.8+

Virtual environment (highly recommended)

SQLite (bundled with Python)

## Installation
# Clone the repository
git clone https://your-repo-url.git
cd BikeRental

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt  # assumes SQLAlchemy included

# Run the CLI
python main.py

## Usage

Launch the CLI by running python main.py.

Choose from the menu to perform operations like adding bikes, stations, users, rentals, etc.

Follow on-screen prompts for entering required data (e.g., IDs, names, locations).

The app commits changes after each action and handles input validation gracefully.

Exit by choosing the "Exit" menu option.

## Project Structure

Here’s how the project is organized:

BikeRental/
├── main.py                   
├── models/
│   ├── Base.py             
│   ├── bike.py              
│   ├── user.py              
│   ├── station.py           
│   └── rental.py            
├── services/
│   ├── bikeservice.py       
│   ├── userservice.py       
│   ├── stationservice.py    
│   └── rentalservice.py     
├── repositories/            
│   ├── bike_repository.py
│   ├── user_repository.py
│   ├── station_repository.py
│   └── rental_repository.py
├── bike_rental.db           # SQLite database file (auto-generated)
├── requirements.txt         # Python package dependencies
└── README.md                # Project README (that you're reading)


main.py — contains the menu loop and user interaction flow.

models/ — defines the data models based on SQLAlchemy ORM.

services/ — encapsulates business logic; each service uses models/repositories for operations.

repositories/ — optional layer to abstract database operations further.

bike_rental.db — the SQLite database created on first run.

requirements.txt — locks Python dependencies for reproducible installs.

## Contributing

Contributions are welcome! Please:

## License

This project is open source and available under the MIT License
.

 ## Mary Itumo
=======
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
>>>>>>> bf76d315e7b696334b56fa828daadd7287f38cf4
