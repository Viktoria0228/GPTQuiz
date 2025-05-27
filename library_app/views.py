import flask, flask_login
from .models import Quiz, Question
from project.settings import DATABASE

def render_library():
    
    return flask.render_template(
        'library.html',
        username = flask_login.current_user.login,
        create_quiz_id = len(Quiz.query.all()) + 1
        )

def render_create_quiz():
    questions = []
    if flask.request.method == 'POST':
        question = Question(
            name = 'Question1',
            type = 'enter answer',
            variant_1 = 'Variant',
            quiz_id = int(flask.request.cookies.get("draft"))
        )
        try:
            DATABASE.session.add(question)
            DATABASE.session.commit()
            return flask.redirect(flask.url_for('/create-quiz/'))
        except:
            print(Exception)
    if flask.request.cookies.get("draft"):
        cookies = int(flask.request.cookies.get("draft"))
        quiz = Quiz.query.get(cookies)
        if quiz:
            if quiz.questions != 0:
                print(quiz.questions)
                questions = quiz.questions
            else:
                questions = []
        else:
            quiz = Quiz(
                name = "draft",
                code_enter = 1234,
                description = 'draft',
                count_questions = 0,
                author_id = flask_login.current_user.id
            )
            try:
                DATABASE.session.add(quiz)
                DATABASE.session.commit()
            except:
                print(Exception)
    
    return flask.render_template(
        'create_quiz.html',
        username = flask_login.current_user.login,
        quiz = Quiz.query.get(ident = 1),
        questions = questions
        )
            