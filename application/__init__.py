"""
This module creates a Flask application instance using Application Factory pattern.
"""
from flask import Flask


def init_app():
    """
    This function initializes Flask application.
    """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.ProductionConfig' if app.config['ENV'] == 'production'
                           else 'config.DevelopmentConfig')

    with app.app_context():
        from . import routes  # noqa: F401 pylint: disable=C0415,W0611

        return app
