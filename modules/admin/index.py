from flask import Blueprint, request, jsonify, current_app as app, render_template
from .business import *
from modules.tools.response import *
from flasgger import swag_from



@swag_from('./swagger/info.yaml')
def _info():
    try:
        data,message = info(request.get_json())
        return response(data=data,message=message)
    except Exception as e:
        return ERROR(e)
    

admin_bp = Blueprint('admin_bp', __name__)
admin_bp.add_url_rule('/admin/info',view_func=_info, methods=["POST"])