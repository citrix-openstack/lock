import sys
from lock import database
import pprint


def get_database():
    pprint.pprint(database.get_database('server.database'), indent=4)


def set_database():
    servers_dot_py, = sys.argv[1:]

    with open(servers_dot_py, 'rb') as f:
        database.set_database('server.database', f.read())
