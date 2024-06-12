from flask import Blueprint, request, jsonify, current_app as app, render_template
from http import HTTPStatus
from flasgger import swag_from



@swag_from('../swagger/news_get_all.yaml')
def news_get_all():
    try:
        return jsonify(
                message = None,
                data = {'news':''},
            ), HTTPStatus.OK
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(    
            message = None,
            data = None,
        ), HTTPStatus.INTERNAL_SERVER_ERROR


news_bp = Blueprint('news_bp', __name__)
news_bp.add_url_rule('/news/get_all',view_func=news_get_all, methods=["GET"])