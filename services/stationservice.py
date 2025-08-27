from repositories.station_repository import StationRepository

class StationService:
    def _init_(self, session):
        self.repository = StationRepository(session)

    def add_station(self, name, location):
        """Add a new station."""
        if not name or not location:
            raise ValueError("Name and location cannot be empty")
        return self.repository.add(name, location)

    def list_stations(self):
        """List all stations."""
        return self.repository.list_all()

    def delete_station(self, station_id):
        """Delete a station."""
        return self.repository.delete(station_id)
