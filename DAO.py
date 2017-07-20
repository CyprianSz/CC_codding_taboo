import csv
from events import *
from datetime import date


class DAO:
    """
    This class contains methods to import and export data.
    """
    def load_csv(self, csv_file):
        '''
        Loads data from csv file

        Parameter:
        ----------
        users_csv - str (filename of csv file)

        Return:
        -------
        lst of lst of str
        '''
        with open(csv_file, 'r') as u_file:
            data_list = [line for line in csv.reader(u_file)]
        if not data_list:
            raise FileNotFoundError('Missing data in {}'.format(csv_file))
        return data_list

    def save_csv(self, data_list, csv_file):
        with open(csv_file, 'w') as save_file:
            for row in data_list:
                csv.writer(save_file).writerow(row)

    def make_date(self, string):
        return date(*[int(data) for data in string.split('-')])


class CheckpointDAO(DAO):

    DATABASE_FILE = 'checkpoints.csv'

    def load_checkpoints(self):
        """
        Gets all checkpoints

        Return:
        -------
        None
        """
        events_list = self.load_csv(self.DATABASE_FILE)
        for checkpoint in events_list:
            Checkpoint(self.make_date(checkpoint[0]))

    def save_checkpoints(self):
        """
        Saves Checkpoint type objects to csv file_name
        """
        data_to_save = []
        for event in Checkpoint.events:
                data_to_save.append([event.get_date()])
        self.save_csv(data_to_save, self.DATABASE_FILE)


class MentoringDAO(DAO):

    DATABASE_FILE = 'mentorings.csv'

    def load_mentorings(self):
        """
        Gets all checkpoints

        Return:
        -------
        None
        """
        events_list = self.load_csv(self.DATABASE_FILE)
        for mentoring` in events_list:
            # mentoring = event.split(',')
            PrivateMentoring(self.make_date(mentoring[0]), mentoring[1], mentoring[2])

    def save_mentorings(self):
        """
        Saves Checkpoint type objects to csv file_name
        """
        data_to_save = []
        for event in PrivateMentoring.events:
                data_to_save.append([event.get_date(), event.get_mentor(), event.get_goal()])
        self.save_csv(data_to_save, self.DATABASE_FILE)
