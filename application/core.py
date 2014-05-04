from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore
from flask.ext.restful import Api
from flask.ext.migrate import Migrate


# Create Flask App Instance and import config from top-level and various sub modules
app = Flask(__name__, static_url_path='')
app.config.from_object('application.config.ProductionConfig')
app.config.from_object('application.users.config.ProductionUserConfig')


# Setup the HTTP MEthod rewriting middleware (this is needed for Flask-Login and Flask-Social) 
from .middleware import MethodRewriteMiddleware
app.wsgi_app = MethodRewriteMiddleware(app.wsgi_app)


# Setup logging
from logging import DEBUG
from logging.handlers import SysLogHandler
app.logger.setLevel(DEBUG)
handler = SysLogHandler(address = '/dev/log')
app.logger.addHandler(handler)


# Create DB object and instantiate all models
db = SQLAlchemy(app)
from models import *
db.create_all()


# Setup Migrations
migrate = Migrate(app, db)


# Setup app session handling with KVSession w/ Redis
import redis
from flask.ext.kvsession import KVSessionExtension
from simplekv.memory.redisstore import RedisStore
redisStore = RedisStore(redis.StrictRedis(host=app.config['REDIS_SERVER'], port=app.config['REDIS_PORT']))
sessionStore = KVSessionExtension(redisStore, app)


# Setup Flask-Security and Flask-Social
app.user_datastore = SQLAlchemyUserDatastore(db, User, Role)
app.social_datastore = SQLAlchemyConnectionDatastore(db, Connection)
app.security = Security(app, app.user_datastore)
app.social = Social(app, app.social_datastore)


# Create Mail object
mail = Mail(app)

# TODO: if you use angularjs as your frontend, there is a bit of a conflict with template
#  delimiters. Uncomment the next block to change Jinja's delimiters
# Update Jinja templating delimiters, to not mess with angularjs
# app.jinja_options = app.jinja_options.copy()
# app.jinja_options.update(dict(
#     block_start_string='<%',
#     block_end_string='%>',
#     variable_start_string='%%',
#     variable_end_string='%%',
#     comment_start_string='<#',
#     comment_end_string='#>'
# ))


# Import and register all blueprints
from views import mainBlueprint
from users.views import usersBlueprint
app.register_blueprint(mainBlueprint, url_prefix='/')
app.register_blueprint(usersBlueprint, url_prefix='/users')
# TODO: import custom blueprints


# Setup the RESTful API
api = Api(app)

# TODO: Setup custom API endpoints
# import modulename.api
# api.add_resource(modulename.api.ResourceClass, '/v%d/module/resource' % % app.config['API_VERSION'])


# Setup custom error handlers
from errors import *
from users.errors import *

# TODO: Setup custom errors
# from modulename.errors import *