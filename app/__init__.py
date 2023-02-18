import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# load env var form .env to env
load_dotenv()

# create SQL database extension    
db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = os.getenv('SECRET_KEY'),
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # configure the SQLite database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"]        = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_ECHO']                = os.getenv('SQLALCHEMY_ECHO')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    
    # initialize the app with the extension
    db.init_app(app)

    
    from .database import sql_db
    with app.app_context():
         db.create_all()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    from . import dashboard_view,view
    app.register_blueprint(dashboard_view.bp)
    app.register_blueprint(view.bp)

    return app

application = create_app()