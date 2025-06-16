import flask, flask_login
from library_app.models import Quiz
from project import login_manager

def render_admin_page():
    quizes= Quiz.query.all()
    return flask.render_template(
        template_name_or_list= 'admin.html',
        username = flask_login.current_user.login,
        quizes = quizes
    )