from flask import request
from flasgger import swag_from
from modules.tools.response import response, ERROR
from ..models import User

@swag_from('../swagger/signin.yaml')
def _signin():
    try:
        data, message = getId(request.get_json())
        return response(data=data, message=message)
    except Exception as e:
        return ERROR(e)

def getId(data):
    try:
        user = User.find_by_email(data['email'])
        if user:
            if user.password == data['password']:
                return {'userId': user.id}, 'success'
            return {}, 'wrong credentials'
        return {}, 'unsuccess'
    except Exception as e:
        return {}, 'unsuccess'