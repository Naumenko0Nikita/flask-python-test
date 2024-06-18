import flask, flask_sqlalchemy, flask_migrate
import os

project_app = flask.Flask(
    import_name = "project",
    instance_path = os.path.abspath(__file__ + "/..")
)
project_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

DATABASE = flask_sqlalchemy.SQLAlchemy(app = project_app)

migrate = flask_migrate.Migrate(app = project_app, db = DATABASE)