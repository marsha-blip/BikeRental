from repositories.userrepository import UserRepository

class UserService:
    def __init__(self, session):
        self.user_repository = UserRepository(session)

    def add_user(self, username: str, email: str):
        """Add a new user."""
        return self.user_repository.add(username, email)

    def get_user(self, user_id: int):
        """Retrieve a user by ID."""
        return self.user_repository.get_by_id(user_id)

    def update_user(self, user_id: int, **kwargs):
        """Update user information."""
        return self.user_repository.update(user_id, **kwargs)

    def delete_user(self, user_id: int):
        """Delete a user."""
        self.user_repository.delete(user_id)
