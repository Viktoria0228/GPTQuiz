import flask, flask_login
from .models import Quiz, Question
from project.settings import DATABASE

def render_library():
    
    return flask.render_template(
        'library.html',
        username = flask_login.current_user.login
        )

def render_create_quiz():
    
    if flask.request.method == 'POST':
        question = Question(
            name = 'Question1',
            type = 'enter answer',
            variant_1 = 'Variant',
            quiz_id = 1
        )
        try:
            DATABASE.session.add(question)
            DATABASE.session.commit()
        except:
            print(Exception)

        
        
    return flask.render_template(
        'create_quiz.html',
        username = flask_login.current_user.login,
        quiz = Quiz.query.get(ident = 1)
        
        )