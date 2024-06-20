


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

@swag_from('../swagger/stat.yaml')
def _stat():
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
    
economy_bp = Blueprint('economy_bp', __name__)
economy_bp.add_url_rule('/economy/add',view_func=_add, methods=["POST"])
economy_bp.add_url_rule('/economy/delete',view_func=_delete, methods=["DELETE"])
economy_bp.add_url_rule('/economy/get',view_func=_get, methods=["POST"])
economy_bp.add_url_rule('/economy/stat',view_func=_stat, methods=["POST"])




