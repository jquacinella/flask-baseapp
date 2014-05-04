import os
from datetime import timedelta

_basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    ADMINS = frozenset(['youremail@yourdomain.com'])    # TODO: Change this!
    SECRET_KEY = 'SecretKeyForSessionSigning'           # TODO: Change this!
    DOMAIN = "example.com"                              # TODO: Change this!
    API_VERSION = 1                                     # TODO: Change this when needed

    # SQLAlchemy Options
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(_basedir, 'db_repository')
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_RECORD_QUERIES = False

    # Operations
    THREADS_PER_PAGE = 8

    # CSRF Settings
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "somethingimpossibletoguess"     # TODO: Change this!

    # Redis Settings
    REDIS_SERVER = 'localhost'
    REDIS_PORT = 6379

    # Session Settings
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    # SMTP Settings
    # TODO: Change this!
    MAIL_SERVER = "email-smtp.us-east-1.amazonaws.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "SMTP username"
    MAIL_PASSWORD = "SMTP password"
    MAIL_DEFAULT_SENDER = "do-not-reply@%s" % DOMAIN

class ProductionConfig(Config):
    #SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    #SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'
    DEBUG = True
    SQLALCHEMY_RECORD_QUERIES = True

class TestingConfig(Config):
    #SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'
    TESTING = True
    SQLALCHEMY_RECORD_QUERIES = True