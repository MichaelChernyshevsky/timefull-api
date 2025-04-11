from flask import request
from flasgger import swag_from
from modules.tools.response import response, ERROR
from ..models import User

@swag_from('../swagger/get.yaml')
def _info():
    try:
        data, message = info(request.get_json())
        return response(data=data, message=message)
    except Exception as e:
        return ERROR(e)

def info(data):
    try:
        user = User.find_by_id(data['userId'])
        if user:
            return user.serialize(), 'success'
        return {'state':'can not find user'}, 'unsuccess'
    except Exception as e:
        print(e)
        return {'error':''}, 'unsuccess'