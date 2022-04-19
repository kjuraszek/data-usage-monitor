"""
Flask Application routing.
"""
import json
from flask import current_app as app
from flask import render_template


@app.route('/', methods=['GET'])
def index():
    """
    Function serves a template for a home page.
    """
    with open('data.json', 'r', encoding='utf8') as data_file:
        data = dict(json.load(data_file))
        data_usage = data.get('data_usage', 0)
    return render_template('home.html', data_usage=data_usage)
