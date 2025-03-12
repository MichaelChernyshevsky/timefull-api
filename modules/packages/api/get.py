from flask import  request
from flasgger import swag_from
from .chack import *
from .inection import inection
from modules.tools.response import *

def _get(data):
    try:
        inection(data['userId']);
        package = Packages.find_by_user(data['userId'])
        return package.serialize(),'success'
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'

        
@swag_from('../swagger/get.yaml')
def get():
    try:
        data,message = _get(request.get_json())
        return response(data=data,message=message)
    except Exception as e:
        return ERROR(e)
    

