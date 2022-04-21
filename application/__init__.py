"""
This module creates a Flask application instance using Application Factory pattern.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def init_app():
    """
    This function initializes Flask application.
    """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.ProductionConfig' if app.config['ENV'] == 'production'
                           else 'config.DevelopmentConfig')

    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        from . import routes  # noqa: F401 pylint: disable=C0415,W0611
        from . import models  # noqa: F401 pylint: disable=C0415,W0611
        
        return app
