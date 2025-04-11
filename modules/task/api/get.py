from flask import request
from flasgger import swag_from
from modules.tools.response import response, ERROR
from modules.packages.api.chack import checkPackage
from ..models.task import Task

def _get(data):
    try:
        tasks = {}
        elements = Task.find_by_userId(userId=data['userId'])
        for element in elements:
            tasks[element.id] = element.serialize()
        return {'tasks': tasks}, 'success'
    except Exception as e:
        return {'Error': str(e)}, 'unsuccess'

@swag_from('../swagger/get.yaml')
def get():
    try:
        cont, message1 = checkPackage('task', request.get_json()['userId'])
        if cont:
            data, message = _get(request.get_json())
            return response(data=data, message=message)
        else:
            return response(data={'state': 'not active package'}, message=message1)
    except Exception as e:
        return ERROR(e)