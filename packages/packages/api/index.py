


from flask import Blueprint, request, jsonify, current_app as app, render_template
from http import HTTPStatus
from flasgger import swag_from
from .business import *
from ..list_packages import listPackages

from packages.tools.response import *




# # @swag_from('../swagger/change.yaml')
def _change():
    try:
        data,message = changeState(request.get_json())
        return response(data=data,message=message)
    except Exception as e:
        return ERROR(e)
    

# # @swag_from('../swagger/get.yaml')
def _get():
    try:
        data,message = get(request.get_json())
        return response(data=data,message=message)
    except Exception as e:
        return ERROR(e)
    
# # @swag_from('../swagger/info.yaml')
def _info():
    try:
        data,message = listPackages(),'success'
        return response(data=data,message=message)
    except Exception as e:
        return ERROR(e)

packages_bp = Blueprint('packages_bp', __name__)
packages_bp.add_url_rule('/packages/change',view_func=_change, methods=["POST"])
packages_bp.add_url_rule('/packages/get',view_func=_get, methods=["POST"])
packages_bp.add_url_rule('/packages/info',view_func=_info, methods=["POST"])







