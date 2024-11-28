from .bp import packages_bp  

from flask import Blueprint, request, jsonify, current_app as app, render_template
from http import HTTPStatus
from flasgger import swag_from
from .chack import *
from ..list_packages import listPackages

from packages.tools.response import *



@swag_from('../swagger/info.yaml')
def _info():
    try:
        data,message = listPackages(),'success'
        return response(data=data,message=message)
    except Exception as e:
        return ERROR(e)
packages_bp.add_url_rule('/packages/info',view_func=_info, methods=["POST"])

