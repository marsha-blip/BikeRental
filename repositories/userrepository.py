from sqlalchemy.orm import Session
from models.user import User  

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, username: str, email: str) -> User:
        """Add a new user record to the database."""
        new_user = User(username=username, email=email)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def get_by_id(self, user_id: int) -> User:
        """Retrieve a user record by its ID."""
        return self.session.query(user).filter_by(id=user_id).first()

    def update(self, user_id: int, **kwargs) -> User:
        """
        Update specified fields of a user.
        Example usage: repo.update(user_id, email="new@example.com")
        """
        User = self.get_by_id(user_id)
        if User:
            for field, value in kwargs.items():
                if hasattr(User, field):
                    setattr(User, field, value)
            self.session.commit()
        return User

    def delete(self, user_id: int) -> None:
        """Delete a user record by its ID."""
        User = self.get_by_id(user_id)
        if User:
            self.session.delete(User)
            self.session.commit()
