"""
usage: nukedb.py

A tool to drop all tables and clear all migrations. This action is
destructive and cannot be undone.
"""

import sys
import shutil
import os
from app import db

# Confirm execution
print("WARNING: This program will drop all tables and clear all " \
    "migrations. This action is destructive and cannot be undone.")
while True:
    confirm = input("Continue? (y/n) ")
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        break
    elif confirm.lower() == 'n' or confirm.lower() == 'no':
        exit()
    else:
        print("Please enter either yes (y) or no (n).")

# Remove tables
tables = db.engine.execute('SHOW TABLES')
print('Found ', tables.rowcount, ' tables', sep='')
while tables.rowcount > 0:
    for table in tables:
        print('Attempting to drop ' + table[0])
        try:
            db.engine.execute('DROP TABLE ' + table[0])
        except BaseException as error:
            print('Drop failed')
    tables = db.engine.execute('SHOW TABLES')

# Kill migrations
migratePath = os.getcwd() + '/migrations'
if (os.path.isdir(migratePath)):
    print('Clearing migrations dir ' + migratePath)
    for path in os.listdir(migratePath + '/'):
        if (os.path.isdir(migratePath + '/' + path)):
            print('Removing directory: ' + path)
            shutil.rmtree(migratePath + '/' + path)
        else:
            print('Removing file: ' + path)
            os.remove(migratePath + '/' + path)
else:
    print('Could not find migrations dir')
