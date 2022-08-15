"""
Global extensions module.
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from backend.application.blueprints import api_bp

db = SQLAlchemy()
migrate = Migrate(compare_type=True)
api = Api(api_bp, version='0.1.0', title='Data Usage Monitor API',
          description='API reference for Data Usage Monitor')
