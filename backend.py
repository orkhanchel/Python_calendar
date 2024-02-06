import csv
from hashlib import sha256


class Backend:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.users = {}
            cls._instance.calendars = {}
            cls._instance.events = {}
        return cls._instance

    def save_to_csv(self):
        with open('users.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for user_id, user_data in self.users.items():
                writer.writerow([user_id, user_data['username'], user_data['password']])

    def load_from_csv(self):
        with open('users.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.users[row[0]] = {'username': row[1], 'password': row[2]}

    def hash_password(self, password):
        return sha256(password.encode()).hexdigest()

    def register_user(self, user_id, username, password):
        hashed_password = self.hash_password(password)
        self.users[user_id] = {'username': username, 'password': hashed_password}

    def verify_credentials(self, user_id, password):
        hashed_password = self.hash_password(password)
        return self.users.get(user_id, {}).get('password') == hashed_password
