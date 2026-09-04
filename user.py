def get_user():
    return {
        "id": 1,
        "name": "tester",
        "age": 30,
        "role": "tester"
    }

def is_admin(user):
    return user["role"] == "admin"