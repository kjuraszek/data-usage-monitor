"""
Configuration classes for Flask application.
"""
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))


class Config:  # pylint: disable=too-few-public-methods
    """
    Main configuration class.
    """
    DEBUG = False
    TESTING = False
    TEMPLATES_FOLDER = 'templates'
    SECRET_KEY = os.environ.get('SECRET_KEY') or str(os.urandom(24))
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = (f'postgresql://{os.environ.get("POSTGRES_USER")}:'
                               f'{os.environ.get("POSTGRES_PASSWORD")}@{os.environ.get("POSTGRES_HOST")}:'
                               f'{os.environ.get("POSTGRES_PORT")}/{os.environ.get("POSTGRES_DATABASE")}')


class ProductionConfig(Config):  # pylint: disable=too-few-public-methods
    """
    Production configuration class.
    """


class DevelopmentConfig(Config):  # pylint: disable=too-few-public-methods
    """
    Development configuration class.
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True
