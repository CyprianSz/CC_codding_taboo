class Event:

    events = []

    def __init__(self, date):
        "date: date object"
        self.date = date

    def get_date(self):
        return self.date

    @classmethod
    def sort_events(cls):
        is_sorted = False

        while not is_sorted and len(cls.events) > 1:
            is_sorted = True
            for i in range(len(cls.events) - 1):
                if cls.events[i].date > cls.events[i + 1].date:
                    temporary = cls.events[i]
                    cls.events[i] = cls.event[i + 1]
                    cls.event[i + 1] = temporary
                    is_sorted = False

    @classmethod
    def add_event(cls, event):
        cls.events.append(event)
        cls.sort_events()

    @classmethod
    def get_events(cls):
        return cls.events


class Checkpoint(Event):

    events = []

    def __init__(self, date):
        super().__init__(date)
        super().add_event(self)
        __class__.add_event(self)

    def __str__(self):
        return "{} {}".format(self.date, __class__.__name__)


class PrivateMentoring(Event):

    events = []

    def __init__(self, date):
        super().__init__(date)
        self.prefered_mentor = None
        self.goal = None
        super().add_event(self)
        __class__.add_event(self)

    def __str__(self):
        return "{}\nPrivate mentoring with {} about {}".format(self.date, self.prefered_mentor, self.goal)
