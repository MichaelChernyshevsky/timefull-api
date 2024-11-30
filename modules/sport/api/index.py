from flask import Blueprint, request, jsonify, current_app as app, render_template
from flasgger import swag_from
from .business import *
from modules.tools.response import *
from modules.packages.api.chack import checkPackage

@swag_from('../swagger/get.yaml')
def _get():
    try:
        cont,message1 = checkPackage('sport',request.get_json()['userId'])
        if (cont):
            data,message = get(request.get_json())
            return response(data=data,message=message)
        else:
            return response(data={},message=message1)
    except Exception as e:
        return ERROR(e)
    
@swag_from('../swagger/add.yaml')
def _add():
    try:
        cont,message1 = checkPackage('sport',request.get_json()['userId'])
        if (cont):
            data,message = add(request.get_json())
            return response(data=data,message=message)
        else:
            return response(data={},message=message1)
    except Exception as e:
        return ERROR(e)
@swag_from('../swagger/delete.yaml')
def _delete():
    try:
        cont,message1 = checkPackage('sport',request.get_json()['userId'])
        if (cont):
            data,message = delete(request.get_json())
            return response(data=data,message=message)
        else:
            return response(data={},message=message1)
    except Exception as e:
        return ERROR(e)
    



    
sport_bp = Blueprint('sport_bp', __name__)
sport_bp.add_url_rule('/sort/get',view_func=_get, methods=["POST"])
sport_bp.add_url_rule('/sort/add',view_func=_add, methods=["POST"])
sport_bp.add_url_rule('/sort/delete',view_func=_delete, methods=["DELETE"])

