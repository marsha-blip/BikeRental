from repositories.userrepository import UserRepository

class UserService:
    def _init_(self, session):
        self.repository = UserRepository(session)

    def register_user(self, name, email):
        """Register a new user."""
        if not name or not email:
            raise ValueError("Name and email cannot be empty")
        return self.repository.add(name, email)

    def list_all_users(self):
        """List all users."""
        return self.repository.list_all()

    def delete_user(self, user_id):
        """Delete a user."""
        return self.repository.delete(user_id)