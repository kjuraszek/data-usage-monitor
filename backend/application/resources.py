"""
Flask Application resources.
"""
from http import HTTPStatus

from flask import jsonify, request
from flask_restx import Resource, Namespace
from backend.application.extensions import db, api
from backend.application.models import UsageStamp

ns_single = Namespace('usage-stamp', description='Single Usage Stamp operations')
ns_multi = Namespace('usage-stamps', description='Multiple Usage Stamps operations')

@ns_single.route('/')
class UsageStampAPI(Resource):
    """
    Single Usage Stamp operations.
    """
    @api.doc('list_cats')
    @api.response(HTTPStatus.OK.value, 'Get the last usage stamp')
    def get(self):
        """
        Return the last jsonified UsageStamp object
        """
        usage_stamp = UsageStamp.get_newest_by_date()
        return jsonify(usage_stamp)

    @api.doc('list_cats')
    @api.response(HTTPStatus.OK.value, 'Insert new usage stamp')
    def put(self):
        """
        Insert jsonified UsageStamp object
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


@ns_multi.route('/')
class UsageStampsAPI(Resource):
    """
    Multiple Usage Stamps operations.
    """
    @api.doc('list_cats')
    @api.response(HTTPStatus.OK.value, 'Get the last 12 usage stamps')
    def get(self):
        """
        Returns the last 12 usage stamps
        """
        usage_stamps = UsageStamp.get_multiple_newest_by_date()
        return jsonify(usage_stamps)
