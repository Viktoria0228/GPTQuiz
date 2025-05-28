import flask
from project.settings import DATABASE
# from user_app.models import User

class Question(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)

    name = DATABASE.Column(DATABASE.String(100), nullable = False)
    type = DATABASE.Column(DATABASE.String(100), nullable = False)
    variant_1 = DATABASE.Column(DATABASE.String(100), nullable = False)
    variant_2 = DATABASE.Column(DATABASE.String(100), nullable = True)
    variant_3 = DATABASE.Column(DATABASE.String(100), nullable = True)
    variant_4 = DATABASE.Column(DATABASE.String(100), nullable = True)
    variant_5 = DATABASE.Column(DATABASE.String(100), nullable = True)

    quiz_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey('quiz.id'))

class Quiz(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    code_enter = DATABASE.Column(DATABASE.Integer)
    name = DATABASE.Column(DATABASE.String(100), nullable = False)
    description = DATABASE.Column(DATABASE.String, nullable = False)
    count_questions = DATABASE.Column(DATABASE.Integer, nullable = False)
    author_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey('user.id'))
    questions = DATABASE.relationship(Question, backref = 'quiz', lazy = True)