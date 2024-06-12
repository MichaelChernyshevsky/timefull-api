from flask import Blueprint, request, jsonify, current_app as app, render_template
from http import HTTPStatus
from flasgger import swag_from
from .business import *



@swag_from('../swagger/news_get_all.yaml')
def get_all():
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
    

    
@swag_from('../swagger/news_add.yaml')
def add():
    try:
        _news = createNews(request.get_json())

  
        return jsonify(
                message = None,
                data = _news,
            ), HTTPStatus.OK
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(    
            message = None,
            data = None,
        ), HTTPStatus.INTERNAL_SERVER_ERROR


news_bp = Blueprint('news_bp', __name__)
news_bp.add_url_rule('/news/get/all',view_func=get_all, methods=["GET"])
news_bp.add_url_rule('/news/add',view_func=add, methods=["POST"])
