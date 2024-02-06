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
