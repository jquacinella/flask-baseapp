''' Exception base-level class tht all sub-exceptions should inherit from. '''
from flask import current_app

class BaseFlaskException(Exception):
    ''' Base class for all exceptions this app can throw. '''
    def __init__(self, status_code=None, exception=None):
        Exception.__init__(self)
        if status_code is not None:
            self.status_code = status_code
        self.exception = exception

        # Log the exception
        current_app.logger.exception(exception)

    def to_dict(self):
        rv = dict()
        if self.exception:
            rv['exception'] = str(self.exception)
        rv['message'] = self.message
        rv['status_code'] = self.status_code
        return rv

    def __str__(self):
        ''' Represent the exception as a string. '''
        if self.message:
            if self.exception:
                return "%s. exception: %s" % (self.message, self.exception)
            else:
                return "%s. " % (self.message, self.exception)
        else:
            return "No message associated with Exception!"