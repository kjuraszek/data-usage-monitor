"""
Flask Application routing.
"""
from flask import Blueprint, jsonify, render_template, request
from .extensions import db
from .models import UsageStamp


home_bp = Blueprint('home', __name__, 'templates')
usage_stamp_bp = Blueprint('usage_stamp', __name__)
usage_stamps_bp = Blueprint('usage_stamps', __name__)


@home_bp.route('/', methods=['GET'])
def index():
    """
    Function serves a template for a home page.
    """
    usage_stamp = UsageStamp.get_newest_by_date()
    data_usage, empty = ((0.0, True) if usage_stamp is None else
                         (usage_stamp.current_month_download + usage_stamp.current_month_upload, False))
    return render_template('home.html', data_usage=data_usage, empty=empty)


@usage_stamp_bp.route('/api/usage-stamp', methods=['GET'])
def get_usage_stamp():
    """
    Function returns last usage stamp.
    """
    usage_stamp = UsageStamp.get_newest_by_date()
    return jsonify(usage_stamp)


@usage_stamp_bp.route('/api/usage-stamp', methods=['PUT'])
def put_usage_stamp():
    """
    Function inserts usage stamp.
    """
    current_month_download = request.args.get('current_month_download', None)
    current_month_upload = request.args.get('current_month_upload', None)
    time_stamp = request.args.get('time_stamp', None)
    if any(arg is None for arg in [current_month_download, current_month_upload, time_stamp]):
        return "Bad request - missing parameter", 400
    usage_stamp = UsageStamp(current_month_download=current_month_download,
                             current_month_upload=current_month_upload,
                             time_stamp=time_stamp)
    db.session.add(usage_stamp)
    db.session.commit()
    return jsonify(usage_stamp)


@usage_stamps_bp.route('/api/usage-stamps', methods=['GET'])
def get_usage_stamps():
    """
    Function returns last 12 usage stamps.
    """
    usage_stamps = UsageStamp.get_multiple_newest_by_date()
    return jsonify(usage_stamps)
