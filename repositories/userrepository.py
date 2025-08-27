from sqlalchemy.exc import IntegrityError
from models.user import User

class UserRepository:
    def _init_(self, session):
        self.session = session

    def add(self, name, email):
        """Add a new user to the database."""
        try:
            user = User(name=name, email=email)
            self.session.add(user)
            self.session.commit()
            return user
        except IntegrityError:
            self.session.rollback()
            raise ValueError("Email already exists")

    def get_by_id(self, user_id):
        """Retrieve a user by ID."""
        return self.session.query(User).filter_by(id=user_id).first()

    def list_all(self):
        """List all users."""
        return self.session.query(User).all()

    def delete(self, user_id):
        """Delete a user by ID."""
        user = self.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        self.session.delete(user)
        self.session.commit()