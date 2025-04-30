from flask import request
from flasgger import swag_from
from modules.tools.response import response, ERROR
from modules.packages.api.chack import checkPackage
from ..models.timer import Timer

def _get(data):
    try:
        timer = Timer.find_by_user(data['userId'])
        if timer:
            return timer.serialize(), 'success'
        else:
            return {'Error': 'Timer not found'}, 'unsuccess'
    except Exception as e:
        return {'Error': str(e)}, 'unsuccess'

@swag_from('../swagger/get.yaml')
def get():
    try:
        cont, message1 = checkPackage('timer', request.get_json()['userId'])
        if cont:
            data, message = _get(request.get_json())
            return response(data=data, message=message)
        else:
            return response(data={'state': 'not active package'}, message=message1)
    except Exception as e:
        return ERROR(e)