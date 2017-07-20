from controller import *
from events import *
from view import *
from DAO import *


def main():

    chckp_dao = CheckpointDAO()
    mntr_dao = MentoringDAO()
    chckp_dao.load_checkpoints()
    mntr_dao.load_mentorings()
    controller = Controller()
    controller.start()
    chckp_dao.save_checkpoints()
    mntr_dao.save_mentorings()


if __name__ == "__main__":
    main()
