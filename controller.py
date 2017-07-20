from datetime import date
# import date_handle
from view import View
from events import *
import os
import sys


class Controller:

    def __init__(self):
        self.view = View()

    def start(self):
        while True:
            # os.system('clear')
            self.view.print_main_menu()
            choice = self.view.get_choice()
            if choice == '1':
                self.book_private_menotring()
            elif choice == '2':
                self.book_checkpoint()
            elif choice == '3':
                self.print_all_events()
            else:
                self.say_goodbye()
                break
            redundant = input("Enter Enter 2 continue")

    def print_all_events(self):
        self.view.print_all_events(Event.get_events())

    def book_event(self):
        date = self.view.get_event_date()
        date = self.__class__.convert_date(date)
        return date

    def book_checkpoint(self):
        date = self.book_event()
        Checkpoint(date)

    def book_private_menotring(self):
        mentor = self.choose_mentor()
        goal = self.view.get_goal()
        date = self.book_event()
        PrivateMentoring(date, mentor, goal)

    def choose_mentor(self):
        self.view.print_list(PrivateMentoring.MENTORS)
        return self.choose_from_list(PrivateMentoring.MENTORS)

    def choose_from_list(self, lst):
        choice = self.view.get_preferred_mentor()
        return lst[int(choice) - 1]

    def say_goodbye(self):
        self.view.print_goodbye()

    @staticmethod
    def convert_date(date_str):
        date_list = date_str.split('-')
        return (date(int(date_list[2]), int(date_list[1]), int(date_list[0])))
