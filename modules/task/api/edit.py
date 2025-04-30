from flask import request
from flasgger import swag_from
from modules.tools.response import response, ERROR
from modules.packages.api.chack import checkPackage
from ..models.task import Task
from config.extensions import db

def _edit(data):
    try:
        task = Task.find_by_id(id=data['taskId'], userId=data['userId']).first()
        if task:
            if 'title' in data:
                task.title = data['title']
            if 'description' in data:
                task.description = data['description']
            if 'date' in data:
                task.date = data['date']
            if 'countOnDay' in data:
                task.countOnDay = data['countOnDay']
            if 'countOnTask' in data:
                task.countOnTask = data['countOnTask']
            db.session.commit()
        return {}, 'success'
    except Exception as e:
        return {'Error': str(e)}, 'unsuccess'

@swag_from('../swagger/edit.yaml')
def edit():
    try:
        cont, message1 = checkPackage('task', request.get_json()['userId'])
        if cont:
            data, message = _edit(request.get_json())
            return response(data=data, message=message)
        else:
            return response(data={'state': 'not active package'}, message=message1)
    except Exception as e:
        return ERROR(e)