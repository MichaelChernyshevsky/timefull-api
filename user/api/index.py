


from flask import Blueprint, request, jsonify, current_app as app, render_template
from http import HTTPStatus
from flasgger import swag_from
from .business import *



@swag_from('../swagger/signin.yaml')
def signin():

    try:
        # data = createNews(request.get_json())
        print(request.get_json())

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
    
@swag_from('../swagger/signup.yaml')
def signup():
    try:
        data = create(request.get_json())

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
    
@swag_from('../swagger/edit.yaml')
def edit():
    try:
        # data = createNews(request.get_json())
        print(request.get_json())

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

@swag_from('../swagger/get.yaml')
def get():
    try:
        # data = createNews(request.get_json())
        print(request.get_json())

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


user_bp = Blueprint('user_bp', __name__)
user_bp.add_url_rule('/signin',view_func=signin, methods=["POST"])
user_bp.add_url_rule('/signup',view_func=signup, methods=["POST"])
user_bp.add_url_rule('/user/edit',view_func=edit, methods=["PATCH"])
user_bp.add_url_rule('/user',view_func=get, methods=["GET"])




