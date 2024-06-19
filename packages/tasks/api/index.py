


from flask import Blueprint, request, jsonify, current_app as app, render_template
from http import HTTPStatus
from flasgger import swag_from
from .business import *



@swag_from('../swagger/add.yaml')
def _add():
    try:
        return jsonify(
                message = None,
                data = add(request.get_json()),
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
                data = delete(request.get_json()),
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
        return jsonify(
                message = None,
                data = get(request.get_json()),
            ), HTTPStatus.OK
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(    
            message = None,
            data = None,
        ), HTTPStatus.INTERNAL_SERVER_ERROR

task_bp = Blueprint('task_bp', __name__)
task_bp.add_url_rule('/task/add',view_func=_add, methods=["POST"])
task_bp.add_url_rule('/task/delete',view_func=_delete, methods=["DELETE"])
task_bp.add_url_rule('/task/edit',view_func=_edit, methods=["PATCH"])
task_bp.add_url_rule('/task/get',view_func=_get, methods=["GET"])




