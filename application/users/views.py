import json 

from flask import render_template, redirect, request, current_app, session, flash, url_for, Blueprint, jsonify
from flask.ext.login import current_user
from flask.ext.security import LoginForm, RegisterForm, current_user, login_required, login_user, auth_token_required
from flask.ext.security.views import logout
from flask.ext.social.utils import get_provider_or_404
from flask.ext.social.views import connect_handler
from application.core import app


usersBlueprint = Blueprint('users', __name__, template_folder='templates/users')


@usersBlueprint.route('/user_details',  methods=['GET'])
@login_required
def user_details():
    return current_user.toJson()


@usersBlueprint.route('/profile')
@login_required
def profile():
    return render_template('security/profile.html', content='Profile Page', twitter_conn=app.social.twitter.get_connection())


@usersBlueprint.route('/profile/<provider_id>/post', methods=['POST'])
@login_required
def social_post(provider_id):
    message = request.form.get('message', None)

    if message:
        provider = get_provider_or_404(provider_id)
        api = provider.get_api()

        if provider_id == 'twitter':
            display_name = 'Twitter'
            api.PostUpdate(message)
        if provider_id == 'facebook':
            display_name = 'Facebook'
            api.put_object("me", "feed", message=message)

        flash('Message posted to %s: %s' % (display_name, message), 'info')

    return redirect(url_for('users.profile'))


@usersBlueprint.route('/register', methods=['GET', 'POST'])
@usersBlueprint.route('/register/<provider_id>', methods=['GET', 'POST'])
def register(provider_id=None):

    if current_user.is_authenticated():
        return redirect(request.referrer or current_app.config['SECURITY_POST_LOGIN_VIEW'])

    form = RegisterForm()

    if provider_id:
        provider = get_provider_or_404(provider_id)
        connection_values = session.get('failed_login_connection', None)
    else:
        provider = None
        connection_values = None

    if form.validate_on_submit():
        ds = current_app.security.datastore
        user = ds.create_user(email=form.email.data, password=form.password.data)
        ds.commit()

        # See if there was an attempted social login prior to registering
        # and if so use the provider connect_handler to save a connection
        connection_values = session.pop('failed_login_connection', None)

        if connection_values:
            connection_values['user_id'] = user.id
            connect_handler(connection_values, provider)

        if login_user(user):
            ds.commit()
            flash('Account created successfully', 'info')
            return redirect(url_for('security.profile'))

        return render_template('security/thanks.html', user=user)

    login_failed = int(request.args.get('login_failed', 0))
    return render_template('security/register_user.html', register_user_form=form, provider=provider, login_failed=login_failed, connection_values=connection_values)