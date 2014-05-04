from application.core import db
from flask.ext.security import UserMixin, RoleMixin

import json

# Define User and Role models (that Flask-Security expects)
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('roles.id')))

class Role(db.Model, RoleMixin):
    ''' Role based security via Flask-Security '''
    __tablename__ = "roles"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    ''' User Model from Flask-Security '''
    __tablename__ = "users"

    # Base Flask-Security columns
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    # Flask-Security column for confirming users (SECURITY_CONFIRMABLE)
    confirmed_at = db.Column(db.DateTime())

    # Flask-Security column for tracking users (SECURITY_TRACKABLE)
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(length=40))
    current_login_ip = db.Column(db.String(length=40))
    login_count = db.Column(db.Integer())

    # Custom Data
    first_name = db.Column(db.String(length=40))
    last_name = db.Column(db.String(length=40))

    # Flask-Social column (found from flask-social-example)
    connections = db.relationship('Connection', backref=db.backref('user', lazy='joined'), cascade="all")

    def toJson(self):
        ''' Represent the user as a JSON object. This is used to initialize the AngularJS APP as well
        as being available via AJAX to get updates to user information. '''
        return json.dumps({'email': self.email, 'first_name': self.first_name, 'last_name': self.last_name})

class Connection(db.Model):
    ''' Connection table for Oauth, via Flask-Social'''
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    provider_id = db.Column(db.String(255))
    provider_user_id = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    secret = db.Column(db.String(255))
    full_name = db.Column(db.String(255))
    display_name = db.Column(db.String(255))
    profile_url = db.Column(db.String(512))
    image_url = db.Column(db.String(512))
    rank = db.Column(db.Integer)
    
    __tablename__ = "connections"

    # TODO: this was an attempt to solve issue with multiple oauths. check git issue for flask-social
    __table_args__ = (db.UniqueConstraint('provider_id', 'provider_user_id', name='_providerid_userid_uc'), {})
