


from flask import Blueprint, request, jsonify, current_app as app, render_template
from http import HTTPStatus
from flasgger import swag_from
from .business import *



@swag_from('../swagger/create.yaml')
def _create():
    try:
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
    
@swag_from('../swagger/edit_stat.yaml')
def _edit_stat():
    try:
        return jsonify(
                message = None,
                data = editStat(request.get_json()),
            ), HTTPStatus.OK
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(    
            message = None,
            data = None,
        ), HTTPStatus.INTERNAL_SERVER_ERROR

@swag_from('../swagger/edit_history.yaml')
def _edit_history():
    try:
        return jsonify(
                message = None,
                data = editHistory(request.get_json()),
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
                data = get(data=request.get_json(),serialize=True),
            ), HTTPStatus.OK
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(    
            message = None,
            data = None,
        ), HTTPStatus.INTERNAL_SERVER_ERROR

timer_bp = Blueprint('timer_bp', __name__)
timer_bp.add_url_rule('/timer/create',view_func=_create, methods=["POST"])
timer_bp.add_url_rule('/timer/delete',view_func=_delete, methods=["DELETE"])
timer_bp.add_url_rule('/timer/edit/stat',view_func=_edit_stat, methods=["PATCH"])
timer_bp.add_url_rule('/timer/edit/history',view_func=_edit_history, methods=["PATCH"])
timer_bp.add_url_rule('/timer/get',view_func=_get, methods=["POST"])




