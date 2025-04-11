from flask import request
from flasgger import swag_from
from modules.tools.response import response, ERROR
from modules.packages.api.chack import checkPackage
from ..models.stat import TaskStat
from config.extensions import db

def _statEdit(data):
    try:
        stat = TaskStat.find_by_userId(data['userId'])
        if stat:
            if 'countDone' in data:
                stat.countDone += int(data['countDone'])
            if 'countUnDone' in data:
                stat.countUnDone += int(data['countUnDone'])
            db.session.commit()
            return {}, 'success'
        return {'Error': 'Stat not found'}, 'unsuccess'
    except Exception as e:
        return {'Error': str(e)}, 'unsuccess'

def statEdit():
    try:
        cont, message1 = checkPackage('task', request.get_json()['userId'])
        if cont:
            data, message = _statEdit(request.get_json())
            return response(data=data, message=message)
        else:
            return response(data={'state': 'not active package'}, message=message1)
    except Exception as e:
        return ERROR(e)