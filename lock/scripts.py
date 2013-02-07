from lock import database
import pprint


def get_database():
    pprint.pprint(database.get_database('server.database'), indent=4)
