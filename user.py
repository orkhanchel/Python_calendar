from calendar import Calendar


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
