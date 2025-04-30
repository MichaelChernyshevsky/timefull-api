from flask import request
from flasgger import swag_from
from modules.tools.response import response, ERROR
from modules.packages.api.chack import checkPackage
from ..models.model import Economy

def get(data):
    try:
        elements = Economy.find_by_user(userId=data['userId'])
        models = {}
        for model in elements:
            models[model.id] = model.serialize()
        return {'economy': models}, 'success'
    except Exception as e:
        return {'error': str(e)}, 'unsuccess'
    
@swag_from('../swagger/get.yaml')
def _get():
    try:
        cont, message1 = checkPackage('economy', request.get_json()['userId'])
        if cont:
            data, message = get(request.get_json())
            return response(data=data, message=message)
        else:
            return response(data={'state': 'not active package'}, message=message1)
    except Exception as e:
        return ERROR(e)