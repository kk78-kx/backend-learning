# basic.py
# Python basics for backend developer

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def is_adult(age):
    if age >= 18:
        return True
    return False

users = [
    {"id": 1, "name": "Alice", "age": 20},
    {"id": 2, "name": "Bob", "age": 17},
]

for user in users:
    status = "Adult" if is_adult(user["age"]) else "Minor"
    print(f"{user['name']} is an {status}.")
