import flask
import flask_migrate, flask_sqlalchemy

project = flask.Flask(
    import_name= 'project',
    template_folder= 'templates',
    static_folder= 'static'
)

project.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

DATABASE= flask_sqlalchemy.SQLAlchemy(app= project)

migrate= flask_migrate.Migrate(app= project, db= DATABASE)

