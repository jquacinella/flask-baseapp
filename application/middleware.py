# Taken from https://github.com/mattupstate/flask-social-example/blob/master/app/middleware.py
from werkzeug import url_decode


class MethodRewriteMiddleware(object):
    ''' Middleware that will allow the passing of METHOD_OVERRIDE to a url
    for HTTP verbs that cannot be done via <form>, like DELETE. '''
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        if 'METHOD_OVERRIDE' in environ.get('QUERY_STRING', ''):
            args = url_decode(environ['QUERY_STRING'])
            method = args.get('__METHOD_OVERRIDE__')
            if method:
                method = method.encode('ascii', 'replace')
                environ['REQUEST_METHOD'] = method
        return self.app(environ, start_response)