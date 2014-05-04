import os

class UserConfig(object):
    # Flask-Security Options
    SECURITY_CONFIRMABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_URL_PREFIX = '/users'

    # Custom views for post login and logout
    SECURITY_POST_LOGIN_VIEW = '/#/userhome'
    SECURITY_POST_LOGOUT_VIEW = '/#/publichome'
    SECURITY_POST_REGISTER_VIEW = SECURITY_POST_LOGIN_VIEW

    # Strong password hasing
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'

    # Change this per app
    SECURITY_EMAIL_SENDER = 'do-not-reply@domain.com'

    # TODO: change this
    SECURITY_PASSWORD_SALT = 'use uuidgen on linux to generate a unique salt'
    SECURITY_CONFIRM_SALT = 'use uuidgen on linux to generate a unique salt'
    SECURITY_RESET_SALT = 'use uuidgen on linux to generate a unique salt'
    SECURITY_LOGIN_SALT = 'use uuidgen on linux to generate a unique salt'
    SECURITY_REMEMBER_SALT = 'use uuidgen on linux to generate a unique salt'

    # Flask-Social configuration options
    SOCIAL_URL_PREFIX = '/social'
    SOCIAL_CONNECT_ALLOW_VIEW = SECURITY_POST_LOGIN_VIEW
    SOCIAL_CONNECT_DENY_VIEW = SECURITY_POST_LOGOUT_VIEW

    # Flask-Social configuration options
    # SOCIAL_TWITTER = {
    #    'consumer_key': 'twitter app id',
    #    'consumer_secret': 'twitter app secret'
    # }

    # SOCIAL_FACEBOOK = {
    #     'consumer_key': 'facebook app id',
    #     'consumer_secret': 'facebook app secret'
    # }

class ProductionUserConfig(UserConfig):
    pass

class DevelopmentUserConfig(UserConfig):
    pass

class TestingUserConfig(UserConfig):
    pass