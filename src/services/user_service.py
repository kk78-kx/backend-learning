from src.models.user import User, UserCreate

__fake_db = [
    User(id=1, name="Alice", age=30),
    User(id=2, name="Bob", age=25),
]

_next_id = 3

def get_all_users() -> list[User]:
    """Return the list of all users."""
    return __fake_db

def create_user(user: UserCreate) -> User:
    global __next_id

    new_user = User(
        id=__next_id, 
        name=user.name, 
        age=user.age
        )
    
    __fake_db.append(new_user)
    __next_id += 1
    
    return new_user