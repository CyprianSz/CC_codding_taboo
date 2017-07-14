class View:

    def print_all_events(self, events):
        for event in events:
            print(event)

    def print_main_menu(self):
        print("Choose option:\n1) Book private mentoring\n2) Book checkpoint\n3) Show all my events")

    def print_goodbye(self):
        print('Bye bye!')

    def get_choice(self):
        return input('Choose option: ')

    def get_checkpoint_details(self):
        return self.get_event_date()

    def get_event_date(self):
        return input('Enter the date: dd-mm-yyyy')

    def get_preferred_mentor(self):
        return input('Enter prefered mentor: ')

    def get_goal(self):
        return input('Enter your goal: ')
