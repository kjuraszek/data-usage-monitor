"""
This module creates a Flask application instance using Application Factory pattern.
"""
from flask import Flask
from .extensions import db, migrate


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
        from .blueprints import home_bp, usage_stamp_bp, usage_stamps_bp
        from . import models  # noqa: F401 pylint: disable=C0415,W0611
        app.register_blueprint(home_bp)
        app.register_blueprint(usage_stamp_bp)
        app.register_blueprint(usage_stamps_bp)

        return app
