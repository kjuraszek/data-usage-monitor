import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    DEBUG = False
    TESTING = False
    TEMPLATES_FOLDER = 'templates'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    TESTING = False


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
