from models.station import Station

class StationRepository:
    def _init_(self, session):
        self.session = session

    def add(self, name, location):
        """Add a new station to the database."""
        station = Station(name=name, location=location)
        self.session.add(station)
        self.session.commit()
        return station

    def get_by_id(self, station_id):
        """Retrieve a station by ID."""
        return self.session.query(Station).filter_by(id=station_id).first()

    def list_all(self):
        """List all stations."""
        return self.session.query(Station).all()

    def delete(self, station_id):
        """Delete a station by ID."""
        station = self.get_by_id(station_id)
        if not station:
            raise ValueError("Station not found")
        self.session.delete(station)
        self.session.commit()