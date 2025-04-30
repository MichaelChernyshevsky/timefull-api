from flask import request
from flasgger import swag_from
from modules.tools.response import response, ERROR
from ..models import User, Info
from config.extensions import db

@swag_from('../swagger/edit.yaml')
def _edit():
    try:
        data, message = edit(request.get_json())
        return response(data=data, message=message)
    except Exception as e:
        return ERROR(e)

def edit(data):
    try:
        user = User.find_by_id(data['userId'])
        if user:
            if 'phone' in data:
                user.phone = data['phone']
            if 'sex' in data or 'age' in data or 'name' in data or 'name2' in data:
                info = Info.find_by_userId(data['userId'])
                if info:
                    if 'sex' in data:
                        info.sex = data['sex']
                    if 'age' in data and data['age'] != 0:
                        info.age = data['age']
                    if 'name' in data:
                        info.name = data['name']
                    if 'name2' in data:
                        info.name2 = data['name2']
                    db.session.commit()
            return {}, 'success'
        return {}, 'unsuccess'
    except Exception as e:
        return {}, 'unsuccess'