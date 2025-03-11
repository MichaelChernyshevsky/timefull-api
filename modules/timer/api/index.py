


from flask import Blueprint, request, jsonify, current_app as app, render_template
from http import HTTPStatus
from flasgger import swag_from
from .business import *
from  modules.tools.response import *
from modules.packages.api.chack import checkPackage


@swag_from('../swagger/update.yaml')
def _update():
    try:
        cont,message1 = checkPackage('timer',request.get_json()['userId'])
        if (cont):
            data,message = update(request.get_json())
            print(message)
            return response(data=data,message=message)
        else:
            return response(data={},message=message1)

    except Exception as e:
         return ERROR(e)



@swag_from('../swagger/get.yaml')
def _get():
    try:
        cont,message1 = checkPackage('timer',request.get_json()['userId'])
        if (cont):
            data,message = get(request.get_json())

            return response(data=data,message=message)
        else:

            return response(data={},message=message1)
        
        
    except Exception as e:
        return ERROR(e)

timer_bp = Blueprint('timer_bp', __name__)
timer_bp.add_url_rule('/timer/update',view_func=_update, methods=["PATCH"])
timer_bp.add_url_rule('/timer/get',view_func=_get, methods=["POST"])




