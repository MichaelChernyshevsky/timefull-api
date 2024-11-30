


from flask import Blueprint, request, jsonify, current_app as app, render_template
from http import HTTPStatus
from flasgger import swag_from
from .business import *
from  modules.tools.response import *
from modules.packages.api.chack import checkPackage



@swag_from('../swagger/add.yaml')
def _add():
    try:
        cont,message1 = checkPackage('task',request.get_json()['userId'])
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
        cont,message1 = checkPackage('task',request.get_json()['userId'])
        if (cont):
            data,message = deleteTask(request.get_json())
            return response(data=data,message=message)
        else:
            return response(data={},message=message1)
        
        
    except Exception as e:
       return ERROR(e)
    
@swag_from('../swagger/edit.yaml')
def _edit():
    try:
        cont,message1 = checkPackage('task',request.get_json()['userId'])
        if (cont):
            data,message = edit(request.get_json())
            return response(data=data,message=message)
        else:
            return response(data={},message=message1)
        
       
    except Exception as e:
        return ERROR(e)

@swag_from('../swagger/get.yaml')
def _get():
    try:
        cont,message1 = checkPackage('task',request.get_json()['userId'])
        if (cont):

            data,message = get(request.get_json())
            return response(data=data,message=message)
        else:
            
            return response(data={},message=message1)
        
        
        
    except Exception as e:
        return ERROR(e)

# @swag_from('../swagger/statInfo.yaml')
def _statInfo():
    try:
        cont,message1 = checkPackage('task',request.get_json()['userId'])
        if (cont):
            data,message = statInfoTask(request.get_json())
            return response(data=data,message=message)
        else:
            return response(data={},message=message1)
    
        
        
    except Exception as e:
        return ERROR(e)
    

# @swag_from('../swagger/statEdit.yaml')
def _statEdit():
    try:
        cont,message1 = checkPackage('task',request.get_json()['userId'])
        if (cont):
            data,message = statEdit(request.get_json())
            return response(data=data,message=message)
        else:
            return response(data={},message=message1)
        
        
        
    except Exception as e:
        return ERROR(e)
    


task_bp = Blueprint('task_bp', __name__)
task_bp.add_url_rule('/task/add',view_func=_add, methods=["POST"])
task_bp.add_url_rule('/task/delete',view_func=_delete, methods=["DELETE"])
task_bp.add_url_rule('/task/edit',view_func=_edit, methods=["PATCH"])
task_bp.add_url_rule('/task/get',view_func=_get, methods=["POST"])
task_bp.add_url_rule('/task/stat/info',view_func=_statInfo, methods=["POST"])
task_bp.add_url_rule('/task/stat/edit',view_func=_statEdit, methods=["PATCH"])





