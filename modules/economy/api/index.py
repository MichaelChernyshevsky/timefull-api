


from flask import Blueprint, request, jsonify, current_app as app, render_template
from http import HTTPStatus
from flasgger import swag_from
from .business import *
from modules.tools.response import *
from modules.packages.api.chack import checkPackage



# # @swag_from('../swagger/add.yaml')
def _add():
    try:
        cont,message1 = checkPackage('economy',request.get_json()['userId'])
        if (cont):
            data,message = add(request.get_json())
            return response(data=data,message=message)
        else:
            return response(data={},message=message1)
    

        
    except Exception as e:
        return ERROR(e)
    
# # @swag_from('../swagger/delete.yaml')
def _delete():
    try:
        print(1)

        cont,message1 = checkPackage('economy',request.get_json()['userId'])
        if (cont):
            data,message = deleteEconomy(request.get_json())
            return response(data=data,message=message)
        else:
            return response(data={},message=message1)
    
        
    except Exception as e:
        return ERROR(e)


# # @swag_from('../swagger/get.yaml')
def _get():
    try: 
        cont,message1 = checkPackage('economy',request.get_json()['userId'])

        if (cont):
            data,message = get(request.get_json())
            print(data)
            return response(data=data,message=message)
        else:

            return response(data={},message=message1)
    
        
       
    except Exception as e:
       return ERROR(e)

# # @swag_from('../swagger/stat.yaml')
def _stat():
    try:
        cont,message1 = checkPackage('economy',request.get_json()['userId'])
        if (cont):
            data,message = statInfoEconomy(request.get_json())
            return response(data=data,message=message)
        else:
            return response(data={},message=message1)
    
        
    except Exception as e:
        return ERROR(e)
    
economy_bp = Blueprint('economy_bp', __name__)
economy_bp.add_url_rule('/economy/add',view_func=_add, methods=["POST"])
economy_bp.add_url_rule('/economy/delete',view_func=_delete, methods=["DELETE"])
economy_bp.add_url_rule('/economy/get',view_func=_get, methods=["POST"])
economy_bp.add_url_rule('/economy/stat',view_func=_stat, methods=["POST"])




