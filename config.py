"""
Configuration classes for Flask application.
"""
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:  # pylint: disable=too-few-public-methods
    """
    Main configuration class.
    """
    DEBUG = False
    TESTING = False
    TEMPLATES_FOLDER = 'templates'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):  # pylint: disable=too-few-public-methods
    """
    Production configuration class.
    """
    TESTING = False


class DevelopmentConfig(Config):  # pylint: disable=too-few-public-methods
    """
    Development configuration class.
    """
    ENV = "development"
    DEVELOPMENT = True
