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
        ]
    }
)
