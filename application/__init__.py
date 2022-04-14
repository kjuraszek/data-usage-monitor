from flask import Flask


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.ProductionConfig' if app.config['ENV'] == 'production'
                            else 'config.DevelopmentConfig')

    with app.app_context():
        from . import routes

        return app