"""
usage: setup_roles.py [-h]

Creates essential roles within the database (currently Admin, Agent, Farmer)
And updates them if the desired roles are different from existing roles

optional arguments:
    -h, --help show this help message and exit
"""

import argparse
from .. import app
from app import db # noqa
from app.models import * # noqa
import datetime

# Create help description
parser = argparse.ArgumentParser(
    description="Creates essential roles in the database (currently Admin, Agent, Farmer).")

print("Setting up roles...")
# This list of role names and whether they are enabled allows us to test the add and update functionality of database
role_names = ['Admin', 'Agent', 'Farmer']
enabled = [False, True, False]

# loop through role_names and enabled lists in parallel
for role_name, enabled in zip(role_names, enabled):
    # get role based on the role name, this breaks if role name is not unique
    user_role = db.session.query(Role).filter_by(role=role_name).first()
    # if role doesn't already exist, create it
    if not user_role:
        user_role = Role()
        user_role.role = role_name
        user_role.createdAt = datetime.datetime.now()
        user_role.updatedAt = datetime.datetime.now()
        user_role.enabled = True
    # if row does exist but the enabled field is different (just an example) update it
    elif user_role.enabled != enabled:
        user_role.updatedAt = datetime.datetime.now()
        user_role.enabled = enabled
    # commit changes
    db.session.add(user_role)
    db.session.commit()
print("Roles have been set up")
