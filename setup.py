from setuptools import setup


setup(
    name="lock",
    version="0.0",
    packages=["lock"],
    entry_points={
        'console_scripts': [
            'lock-get-database = lock.scripts:get_database',
            'lock-set-database = lock.scripts:set_database',
            'lock-list = lock.scripts:list_locks',
            'lock-get-server-by-host = lock.scripts:get_server_by_host',
            'lock-get-server-pair = lock.scripts:get_server_pair',
            'lock-get-single-server = lock.scripts:get_single_server',
            'lock-release = lock.scripts:release',
        ]
    }
)
