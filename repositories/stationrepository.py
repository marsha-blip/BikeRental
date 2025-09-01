from sqlalchemy.orm import Session
from models.station import Station 

class StationRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, name: str, location: str) -> Station:
        """Add a new station record to the database."""
        new = Station(name=name, location=location)
        self.session.add(new)
        self.session.commit()
        return new

    def get_by_id(self, station_id: int) -> Station:
        """Retrieve a station record by its ID."""
        return self.session.query(station).filter_by(id=station_id).first()

    def update(self, station_id: int, **kwargs) -> Station:
        """
        Update specified fields of a station.
        Example usage: repo.update(station_id, name="New Name").
        """
        Station = self.get_by_id(station_id)
        if Station:
            for field, value in kwargs.items():
                if hasattr(station, field):
                    setattr(station, field, value)
            self.session.commit()
        return station

    def delete(self, station_id: int) -> None:
        """Delete a station record by its ID."""
        Station = self.get_by_id(station_id)
        if Station:
            self.session.delete(Station)
            self.session.commit()

