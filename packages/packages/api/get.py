from .bp import packages_bp  

from flask import Blueprint, request, jsonify, current_app as app, render_template
from http import HTTPStatus
from flasgger import swag_from
from .chack import *
from ..list_packages import listPackages

from packages.tools.response import *

def get(data):
    try:
        package = Packages.find_by_user(data['userId'])
        return package.serialize(),'success'
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'

        
    

@swag_from('../swagger/get.yaml')
def _get():
    try:
        data,message = get(request.get_json())
        return response(data=data,message=message)
    except Exception as e:
        return ERROR(e)
    

packages_bp.add_url_rule('/packages/get',view_func=_get, methods=["POST"])
