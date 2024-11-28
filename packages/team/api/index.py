from flask import Blueprint, request, jsonify, current_app as app, render_template
from http import HTTPStatus
from flasgger import swag_from
from packages.packages.api.chack import checkPackage
from packages.tools.response import *



# @swag_from('../swagger/add.yaml')
def _add():
    try:
        cont,message1 = checkPackage('task',request.get_json()['userId'])
        if (cont):
            # data,message = add(request.get_json())
            return response(data=data,message=message)
        else:
            return response(data={},message=message1)
    

        
    except Exception as e:
        return ERROR(e)
    
# @swag_from('../swagger/delete.yaml')
def _delete():
    try:
        cont,message1 = checkPackage('task',request.get_json()['userId'])
        if (cont):
            # data,message = deleteTask(request.get_json())
            return response(data=data,message=message)
        else:
            return response(data={},message=message1)
        
        
    except Exception as e:
       return ERROR(e)
    

# @swag_from('../swagger/delete.yaml')
def _keyGenerate():
    try:
        cont,message1 = checkPackage('task',request.get_json()['userId'])
        if (cont):
            # data,message = deleteTask(request.get_json())
            return response(data=data,message=message)
        else:
            return response(data={},message=message1)
        
        
    except Exception as e:
       return ERROR(e)
    

# @swag_from('../swagger/delete.yaml')
def _invite():
    try:
        cont,message1 = checkPackage('task',request.get_json()['userId'])
        if (cont):
            # data,message = deleteTask(request.get_json())
            return response(data=data,message=message)
        else:
            return response(data={},message=message1)
        
        
    except Exception as e:
       return ERROR(e)
    
# @swag_from('../swagger/delete.yaml')
def _uninvite():
    try:
        cont,message1 = checkPackage('task',request.get_json()['userId'])
        if (cont):
            # data,message = deleteTask(request.get_json())
            return response(data=data,message=message)
        else:
            return response(data={},message=message1)
        
    except Exception as e:
       return ERROR(e)

# @swag_from('../swagger/delete.yaml')
def _addTask():
    try:
        cont,message1 = checkPackage('task',request.get_json()['userId'])
        if (cont):
            # data,message = deleteTask(request.get_json())
            return response(data=data,message=message)
        else:
            return response(data={},message=message1)
        
    except Exception as e:
       return ERROR(e)
    

# @swag_from('../swagger/delete.yaml')
def _deleteTask():
    try:
        cont,message1 = checkPackage('task',request.get_json()['userId'])
        if (cont):
            # data,message = deleteTask(request.get_json())
            return response(data=data,message=message)
        else:
            return response(data={},message=message1)
        
    except Exception as e:
       return ERROR(e)
team_bp = Blueprint('team_bp', __name__)
team_bp.add_url_rule('/team/create',view_func=_add, methods=["POST"])
team_bp.add_url_rule('/team/delete',view_func=_delete, methods=["DELETE"])
team_bp.add_url_rule('/team/invite',view_func=_invite, methods=["POST"])
team_bp.add_url_rule('/team/key/generate',view_func=_keyGenerate, methods=["POST"])

team_bp.add_url_rule('/task/uninvite',view_func=_uninvite, methods=["POST"])
team_bp.add_url_rule('/task/task/add',view_func=_addTask, methods=["POST"])
team_bp.add_url_rule('/task/task/delete',view_func=_deleteTask, methods=["DELETE"])




