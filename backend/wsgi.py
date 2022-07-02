"""
This module is a main entry point for a Flask application.
"""
import configparser
import os
from backend.application import init_app


app = init_app()

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), 'data-usage-monitor.ini'))
    PORT = int(config.get('application', 'flask_port'))
    app.run(host='0.0.0.0', port=PORT)
