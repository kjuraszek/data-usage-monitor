from flask import current_app as app
from flask import render_template
import json

@app.route('/', methods=['GET'])
def index():
    with open('data.json', 'r') as data_file:
        data = dict(json.load(data_file))
        data_usage = data.get('data_usage', 0)
    return render_template('home.html', data_usage=data_usage)