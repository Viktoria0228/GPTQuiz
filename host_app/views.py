from library_app.models import Quiz
import flask

def render_host_app(quizid):

    quiz = Quiz.query.get(ident=quizid)
        
    return flask.render_template("host.html", quiz = quiz)