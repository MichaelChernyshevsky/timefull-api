


from flask import Blueprint, request, jsonify, current_app as app, render_template
from http import HTTPStatus
from flasgger import swag_from
from .business import *



@swag_from('../swagger/signin.yaml')
def _signin():

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
def _signup():
    try:
        
        print(User.query.all())
        return jsonify(
                message = None,
                data = create(request.get_json()),
            ), HTTPStatus.OK
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(    
            message = None,
            data = None,
        ), HTTPStatus.INTERNAL_SERVER_ERROR
    
@swag_from('../swagger/edit.yaml')
def _edit():
    try:
        return jsonify(
                message = None,
                data = edit(request.get_json()),
            ), HTTPStatus.OK
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(    
            message = None,
            data = None,
        ), HTTPStatus.INTERNAL_SERVER_ERROR

@swag_from('../swagger/get.yaml')
def _get():
    try:
        data = get(request.get_json())

      
        return jsonify(
                message = None,
                data = data,
            ), HTTPStatus.OK
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(    
            message = None,
            data = None,
        ), HTTPStatus.INTERNAL_SERVER_ERROR
@swag_from('../swagger/delete.yaml')
def _delete():
    try:
        return jsonify(
                message = None,
                data = {'news': delete(request.get_json())},
            ), HTTPStatus.OK
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(    
            message = None,
            data = None,
        ), HTTPStatus.INTERNAL_SERVER_ERROR

@swag_from('../swagger/addPackage.yaml')
def _add_package():
    try:
        return jsonify(
                message = None,
                data = {'news': delete(request.get_json())},
            ), HTTPStatus.OK
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(    
            message = None,
            data = None,
        ), HTTPStatus.INTERNAL_SERVER_ERROR
    
@swag_from('../swagger/deletePackage.yaml')
def _delete_package():
    try:
        return jsonify(
                message = None,
                data = {'news': delete(request.get_json())},
            ), HTTPStatus.OK
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(    
            message = None,
            data = None,
        ), HTTPStatus.INTERNAL_SERVER_ERROR

@swag_from('../swagger/packages.yaml')
def _packages():
    try:
        return jsonify(
                message = None,
                data = {'news': delete(request.get_json())},
            ), HTTPStatus.OK
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(    
            message = None,
            data = None,
        ), HTTPStatus.INTERNAL_SERVER_ERROR

user_bp = Blueprint('user_bp', __name__)
user_bp.add_url_rule('/signin',view_func=_signin, methods=["POST"])
user_bp.add_url_rule('/signup',view_func=_signup, methods=["POST"])
user_bp.add_url_rule('/user/edit',view_func=_edit, methods=["PATCH"])
user_bp.add_url_rule('/user/delete',view_func=_delete, methods=["DELETE"])
user_bp.add_url_rule('/user/package/add',view_func=_add_package, methods=["PATCH"])
user_bp.add_url_rule('/user/package/delete',view_func=_delete_package, methods=["DELETE"])
user_bp.add_url_rule('/user/package/info',view_func=_packages, methods=["POST"])

user_bp.add_url_rule('/user',view_func=_get, methods=["POST"])




