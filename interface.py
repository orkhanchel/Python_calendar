from backend import Backend
from user import User


class Interface:
    def __init__(self):
        self.backend = Backend()

    def login(self, user_id, password):
        if self.backend.verify_credentials(user_id, password):
            print("Login successful.")
            return User(user_id, self.backend.users[user_id]['username'], self.backend)
        else:
            print("Invalid credentials.")

    def register_user(self, user_id, username, password):
        if user_id not in self.backend.users:
            self.backend.register_user(user_id, username, password)
            print("User created successfully.")
        else:
            print("User already exists.")








