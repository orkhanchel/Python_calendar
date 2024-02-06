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


'''тестирование 
проекта 
для 
себя'''