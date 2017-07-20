class Event:

    events = []

    def __init__(self, date):
        "date: date object"
        self.date = date
        Event.add_event(self)

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
                    cls.events[i] = cls.events[i + 1]
                    cls.events[i + 1] = temporary
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
        self.add_event(self)

    def __str__(self):
        return "{} {}".format(self.date, __class__.__name__)


class PrivateMentoring(Event):

    MENTORS = ['Aga', 'Konrad', 'Mati', 'Hitler']
    events = []

    def __init__(self, date, prefered_mentor=None, goal=None):
        super().__init__(date)
        self.prefered_mentor = prefered_mentor
        self.goal = goal
        self.add_event(self)

    def __str__(self):
        return "{} Private mentoring with {} about {}".format(self.date, self.prefered_mentor, self.goal)

    def get_mentor(self):
        return self.prefered_mentor

    def get_goal(self):
        return self.goal

    @classmethod
    def add_event(cls, event):
        pass
