


from flask import Blueprint, request, jsonify, current_app as app, render_template
from http import HTTPStatus
from flasgger import swag_from
from .business import *



@swag_from('../swagger/signin.yaml')
def _signin():
    try:
        data,message = getId(request.get_json())
        return jsonify(
                message = message,
                data = data,
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
        data,message = create(request.get_json())
        return jsonify(
                message = message,
                data = data,
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
        data,message = edit(request.get_json())
        return jsonify(
                 message = message,
                data = data,
            ), HTTPStatus.OK
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(    
            message = None,
            data = None,
        ), HTTPStatus.INTERNAL_SERVER_ERROR


    

@swag_from('../swagger/info.yaml')
def _info():
    try:     
        print('-'*100) 
        data,message = info(request.get_json())
        print(data,message)

        return jsonify(
                 message = message,
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
        data,message = delete(request.get_json())
        return jsonify(
                 message = message,
                data =  data,
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
        data,message = delete(request.get_json())
        return jsonify(
                 message = message,
                data =  data,
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
        data,message = delete(request.get_json())
        return jsonify(
                 message = message,
                data = data,
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
        data,message = delete(request.get_json())
        return jsonify(
                message = message,
                data =  data,
            ), HTTPStatus.OK
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(    
            message = None,
            data = None,
        ), HTTPStatus.INTERNAL_SERVER_ERROR

@swag_from('../swagger/stat.yaml')
def _stat():
    try:
        data,message = stat(request.get_json())
        return jsonify(
                message = message,
                data =  data,
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
user_bp.add_url_rule('/user/info',view_func=_info, methods=["POST"])
user_bp.add_url_rule('/user/stat',view_func=_info, methods=["POST"])




