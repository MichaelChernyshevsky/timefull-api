from flask import Blueprint, request, jsonify, current_app as app, render_template
from http import HTTPStatus
from flasgger import swag_from
from .business import *



# # @swag_from('../swagger/get.yaml')
def get():
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
    
# # @swag_from('../swagger/get_category.yaml')
def get_category():
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
    


# # @swag_from('../swagger/add.yaml')
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
news_bp.add_url_rule('/news/get',view_func=get, methods=["GET"])
news_bp.add_url_rule('/news/get/category',view_func=get_category, methods=["GET"])

news_bp.add_url_rule('/news/add',view_func=add, methods=["POST"])



