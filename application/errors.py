from application.core import app
from flask import jsonify, render_template, redirect, url_for, request

# Setup 404 handler (HTML)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Setup 401 handler (JSON)
@app.errorhandler(401)
def unauthorized():
    # Check if this is a JSON request; if so send proper response; otherwise redirect to login
    if request.headers['Content-Type'] == 'application/json':
        response = jsonify({'message': "You are not currently logged in"})
        return response, 401
    else:
        return redirect(app.config['SECURITY_POST_LOGOUT_VIEW'])

app.login_manager.unauthorized_handler(unauthorized)