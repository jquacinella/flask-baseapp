# -*- coding: utf-8 -*-
"""
    app.manage.users
    ~~~~~~~~~~~~~~~~~~~~~

    user management commands
"""

from flask import current_app
from flask.ext.script import Command, prompt, prompt_pass
from flask_security.forms import RegisterForm
from flask_security.registerable import register_user
from werkzeug.datastructures import MultiDict


class CreateUserCommand(Command):
    """Create a user"""

    def run(self):
        # email = prompt('Email')
        # password = prompt_pass('Password')
        # password_confirm = prompt_pass('Confirm Password')
        # data = MultiDict(dict(email=email, password=password, password_confirm=password_confirm))
        # form = RegisterForm(data, csrf_enabled=False)
        # if form.validate():
        #     user = register_user(email=email, password=password)
        #     print '\nUser created successfully'
        #     print 'User(id=%s email=%s)' % (user.id, user.email)
        #     return
        # print '\nError creating user:'
        # for errors in form.errors.values():
        #     print '\n'.join(errors)
        pass


class DeleteUserCommand(Command):
    """Delete a user"""

    def run(self):
        email = prompt('Email')
        user = User.query.filter_by(email=email).first()
        if not user:
            print 'Invalid user'
            return
        db.session.delete(user)
        db.session.commit()
        print 'User deleted successfully'
        #pass


class ListUsersCommand(Command):
    """List all users"""

    def run(self):
        # for u in users.all():
        #     print 'User(id=%s email=%s)' % (u.id, u.email)
        pass