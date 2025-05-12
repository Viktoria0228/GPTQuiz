import flask, flask_login

def render_library():
    
    return flask.render_template(
        'library.html',
        username = flask_login.current_user.login
        )

def render_create_quiz():
    
    return flask.render_template(
        'create_quiz.html',
        username = flask_login.current_user.login
        )