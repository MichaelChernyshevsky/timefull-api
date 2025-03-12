
from flask import Blueprint, request, jsonify, current_app as app, render_template
from flasgger import swag_from
from .chack import *
from ..list_packages import listPackages

from modules.tools.response import *



@swag_from('../swagger/info.yaml')
def info():
    try:
        data,message = listPackages(),'success'
        return response(data=data,message=message)
    except Exception as e:
        return ERROR(e)

