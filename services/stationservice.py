from repositories.stationrepository import StationRepository


class StationService:
    def __init__(self, session):
        self.station_repository = StationRepository(session)

    def add_station(self, name: str, location: str):
        """Add a new station."""
        return self.station_repository.add(name, location)

    def get_station(self, station_id: int):
        """Retrieve a station by its ID."""
        return self.station_repository.get_by_id(station_id)

    def update_station(self, station_id: int, **kwargs):
        """Update specific attributes of a station."""
        return self.station_repository.update(station_id, **kwargs)

    def delete_station(self, station_id: int):
        """Remove a station from the system."""
        self.station_repository.delete(station_id)

