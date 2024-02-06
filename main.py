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

    def create_user(self, user_id, username, password):
        hashed_password = self.hash_password(password)
        self.users[user_id] = {'username': username, 'password': hashed_password}

    def verify_credentials(self, user_id, password):
        hashed_password = self.hash_password(password)
        return self.users.get(user_id, {}).get('password') == hashed_password


class Event:
    def __init__(self, event_id, title, description, participants, recurring=False):
        self.event_id = event_id
        self.title = title
        self.description = description
        self.participants = participants
        self.recurring = recurring

    def __str__(self):
        return f"Event ID: {self.event_id}\nTitle: {self.title}\nDescription: {self.description}\nParticipants: {', '.join(self.participants)}\nRecurring: {self.recurring}"

    def update_event(self, title=None, description=None, participants=None, recurring=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if participants:
            self.participants = participants
        if recurring is not None:
            self.recurring = recurring


class Calendar:
    def __init__(self, user_id):
        self.user_id = user_id
        self.events = {}

    def add_event(self, event_id, title, description, participants):
        self.events[event_id] = {'title': title, 'description': description, 'participants': participants}

    def delete_event(self, event_id):
        if event_id in self.events:
            del self.events[event_id]
        else:
            print("Event not found.")

    def get_events(self):
        return self.events


class User:
    def __init__(self, user_id, username, backend):
        self.user_id = user_id
        self.username = username
        self.backend = backend

    def create_calendar(self):
        self.backend.calendars[self.user_id] = Calendar(self.user_id)

    def get_calendar(self):
        return self.backend.calendars.get(self.user_id)

    def create_event(self, event_id, title, description, participants):
        calendar = self.get_calendar()
        if calendar:
            calendar.add_event(event_id, title, description, participants)
        else:
            print("User has no calendar.")

    def delete_event(self, event_id):
        calendar = self.get_calendar()
        if calendar:
            calendar.delete_event(event_id)
        else:
            print("User has no calendar.")


class Interface:
    def __init__(self):
        self.backend = Backend()

    def register_user(self, user_id, username, password):
        if user_id not in self.backend.users:
            self.backend.create_user(user_id, username, password)
            print("User created successfully.")
        else:
            print("User already exists.")

    def login(self, user_id, password):
        if self.backend.verify_credentials(user_id, password):
            print("Login successful.")
            return User(user_id, self.backend.users[user_id]['username'], self.backend)
        else:
            print("Invalid credentials.")



# Создаем экземпляр интерфейса
interface = Interface()

# Регистрируем нового пользователя
interface.register_user("Orkhan", "Ismayilov", "12345")

# Входим в систему под созданным пользователем
user = interface.login("Orkhan", "12345")

# Если вход успешен, добавляем событие в календарь пользователя
if user:
    user.create_calendar()
    user.create_event("event1", "Встреча", "Обсудить проект", ["Orkhan"])

user.create_event("event1", "Встреча", "Обсудить проект", ["Orkhan"])
events = user.get_calendar().get_events()
for event_id, event_data in events.items():
    print(f"Event ID: {event_id}, Title: {event_data['title']}, Description: {event_data['description']}, Participants: {', '.join(event_data['participants'])}")

