"""
This module creates a Flask application instance using Application Factory pattern.
"""
from flask import Flask
from flask_cors import CORS
from backend.application.extensions import db, migrate, api


def init_app():
    """
    This function initializes Flask application.
    """
    app = Flask(__name__, instance_relative_config=False)
    CORS(app)
    app.config.from_object('backend.config.ProductionConfig' if app.config['ENV'] == 'production'
                           else 'backend.config.DevelopmentConfig')

    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        from backend.application.blueprints import api_bp  # pylint: disable=C0415
        from backend.application.resources import ns_single, ns_multi  # pylint: disable=C0415
        from . import models  # noqa: F401 pylint: disable=C0415,W0611
        app.register_blueprint(api_bp)
        api.add_namespace(ns_single)
        api.add_namespace(ns_multi)
        return app
