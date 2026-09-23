import json

def get_stored_username():
    """get stored username if available"""
    filename = "username.json"

    try:
        with open(filename, "r") as name:
            username = json.load(name)

    except FileNotFoundError:
        return None

    else:
        return username

def greet_user():
    """greet user by name"""

    username = get_stored_username()

    if username:
        print(f"Welcome back {username}")

    else:
        username = input("What is your name: ")
        filename = "username.json"
        with open(filename, "w") as writename:
            json.dump(username, writename)
            print(f"We'll remember you name when you come back {username}")

greet_user()
