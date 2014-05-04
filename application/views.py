import os

from flask import request, session, current_app, render_template, Blueprint, jsonify, abort, make_response
from flask_wtf.csrf import generate_csrf, validate_csrf
from flask.ext.login import current_user
from flask.ext.security import LoginForm

from models import User


mainBlueprint = Blueprint('main', __name__, template_folder="static")


@mainBlueprint.route('/', methods=['GET'])
def index():
    # Get user object ti put in the initial 'seed' portion of the AngularJS app
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
    else:
        user = None
    
    # TODO: deal with this after CSRF issue handled
    # Give the AngularJS app an initial CSRF token (which can be regenerated later)
    #csrf = generate_csrf()
    #csrf = LoginForm().csrf_token.current_token

    # Give the AngularJS app an initial boolean if the user is logged in via session cookie
    loggedIn = current_user.is_authenticated()

    return render_template('index.html', user=user, loggedIn=loggedIn)
    
# TODO: deal with this after CSRF issue handled
# @mainBlueprint.route('csrf', methods=['GET'])
# def csrf():
#     return jsonify({"csrf": LoginForm().csrf_token.current_token})