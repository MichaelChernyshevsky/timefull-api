from flask import request
from flasgger import swag_from
from modules.tools.response import response, ERROR
from modules.packages.api.chack import checkPackage
from ..models.stat import TaskStat

def _statInfo(data):
    try:
        return TaskStat.find_by_userId(data['userId']).serialize(), 'success'
    except Exception as e:
        return {'Error': str(e)}, 'unsuccess'

def statInfo():
    try:
        cont, message1 = checkPackage('task', request.get_json()['userId'])
        if cont:
            data, message = _statInfo(request.get_json())
            return response(data=data, message=message)
        else:
            return response(data={'state': 'not active package'}, message=message1)
    except Exception as e:
        return ERROR(e)