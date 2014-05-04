#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand

from application.core import app
from application.manage import *

# Setup Flask-Script manager
manager = Manager(app)

# Session commands
manager.add_command('session_cleanup', CleanupSessionsCommand())

# DB commands
manager.add_command('db', MigrateCommand)

# User commands
manager.add_command('user_create', CreateUserCommand())
manager.add_command('user_delete', DeleteUserCommand())
manager.add_command('user_list', ListUsersCommand())

# Custom commands

# Run main manager script
if __name__ == "__main__":
    manager.run()