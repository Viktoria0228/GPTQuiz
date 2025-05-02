import flask_login
from project.settings import DATABASE

class User(DATABASE.Model, flask_login.UserMixin):
    id= DATABASE.Column(DATABASE.Integer, primary_key= True)
    
    login= DATABASE.Column(DATABASE.String(40), nullable= False)
    name= DATABASE.Column(DATABASE.String(30), nullable= False)
    surname= DATABASE.Column(DATABASE.String(30), nullable= False)
    email= DATABASE.Column(DATABASE.String(255), nullable= False)
    password= DATABASE.Column(DATABASE.String(30), nullable= False)