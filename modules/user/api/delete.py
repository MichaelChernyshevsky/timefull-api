from flask import request
from flasgger import swag_from
from modules.tools.response import response, ERROR
from ..models import User
from config.extensions import db

@swag_from('../swagger/delete.yaml')
def _delete():
    try:
        data, message = delete(request.get_json())
        return response(data=data, message=message)
    except Exception as e:
        return ERROR(e)

def delete(data):
    try:
        User.query.filter_by(id=data['userId']).delete()
        db.session.commit()
        return {}, 'success'
    except Exception as e:
        return {}, 'unsuccess'