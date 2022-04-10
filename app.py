from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    with open('data.json', 'r') as data_file:
        data = dict(json.load(data_file))
        data_usage = data.get('data_usage', 0)
    return render_template('app.html', data_usage=data_usage)
