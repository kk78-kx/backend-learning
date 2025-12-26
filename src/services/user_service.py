from src.models.user import User

__fake_db = [
    User(id=1, name="Alice", age=30),
    User(id=2, name="Bob", age=25),
]

def get_all_users() -> list[User]:
    """Return the list of all users."""
    return __fake_db