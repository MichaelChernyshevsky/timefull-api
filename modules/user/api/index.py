


from flask import Blueprint, request, jsonify, current_app as app, render_template
from flasgger import swag_from
from .business import *
from  modules.tools.response import *



@swag_from('../swagger/signin.yaml')
def _signin():
    try:
        data,message = getId(request.get_json())
        return response(data=data,message=message)
    except Exception as e:
        return ERROR(e)
    
@swag_from('../swagger/signup.yaml')
def _signup():
    try:
        data,message = create(request.get_json())
        return response(data=data,message=message)
    except Exception as e:
        print(e)

        return ERROR(e)
    
@swag_from('../swagger/edit.yaml')
def _edit():
    try:
        data,message = edit(request.get_json())
        return response(data=data,message=message)
    except Exception as e:
        return ERROR(e)



@swag_from('../swagger/get.yaml')
def _info():
    try:     
        data,message = info(request.get_json())
        return response(data=data,message=message)
    except Exception as e:
        
        return ERROR(e)
    

@swag_from('../swagger/delete.yaml')
def _delete():
    try:
        data,message = delete(request.get_json())
        return response(data=data,message=message)
    except Exception as e:
        return ERROR(e)


    
user_bp = Blueprint('user_bp', __name__)
user_bp.add_url_rule('/signin',view_func=_signin, methods=["POST"])
user_bp.add_url_rule('/signup',view_func=_signup, methods=["POST"])
user_bp.add_url_rule('/user/edit',view_func=_edit, methods=["PATCH"])
user_bp.add_url_rule('/user/delete',view_func=_delete, methods=["DELETE"])
user_bp.add_url_rule('/user/info',view_func=_info, methods=["POST"])




