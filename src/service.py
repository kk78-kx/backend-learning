# service.py
# Backend-style logic

users = [
    {"id": 1, "name": "Alice", "age": 20},
    {"id": 2, "name": "Bob", "age": 17},
]

def get_all_users():
    """Return the list of all users."""
    return users

def get_user_by_id(user_id):
    """Return a user by their ID."""
    for user in users:
        if user["id"] == user_id:
            return user
    return None

def create_user(name, age):
    """Create a new user."""
    new_id = len(users) + 1
    user = {
        "id": new_id,
        "name": name,
        "age": age
    }
    users.append(user)
    return user

if __name__ == "__main__":
    print(get_all_users())
    print(get_user_by_id(1))
    print(create_user("Charlie", 25))
    print(get_all_users())