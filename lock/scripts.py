import sys
from lock import database
import pprint


def get_database():
    pprint.pprint(database.get_database('server.database'), indent=4)


def set_database():
    servers_dot_py, = sys.argv[1:]

    with open(servers_dot_py, 'rb') as f:
        database.set_database('server.database', f.read())


def list_locks():
    for lock in database.get_locks('server.database'):
        print lock


def get_server_by_host():
    from lock.getters import wait_for_first
    import sys

    host, = sys.argv[1:]

    def is_required_server(item):
        try:
            return host == item.get("HOST")
        except:
            return False


    server_data, lock = wait_for_first(is_required_server)

    for item in server_data.items():
        print '%s=%s' % item

    print "LOCK=%s" % lock
