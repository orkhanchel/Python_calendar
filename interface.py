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


#Создаем экземпляр интерфейса
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






