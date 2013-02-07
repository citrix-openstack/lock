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


def get_server_pair():
    from lock.getters import wait_for
    from lock.selectors import first_pair_where_vlans_match


    items, lock = wait_for(first_pair_where_vlans_match)

    for idx, server in enumerate(items):
        for key, value in server.items():
            print "%s%s=%s" % (key, idx, value)

    print "LOCK=%s" % lock


def get_single_server():
    from lock.getters import wait_for_first


    def is_server(item):
        try:
            return bool(item.get("HOST"))
        except:
            return False


    server_data, lock = wait_for_first(is_server)

    for item in server_data.items():
        print '%s=%s' % item

    print "LOCK=%s" % lock


def release():
    lock, = sys.argv[1:]

    database.release_lock('server.database', lock)
