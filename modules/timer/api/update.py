from flask import request
from flasgger import swag_from
from modules.tools.response import response, ERROR
from modules.packages.api.chack import checkPackage
from config.extensions import db
from ..models.timer import Timer
import json

def _update(data):
    try:
        timer = Timer.find_by_user(data['userId'])
        print(data)
        if timer:
            timer.stat = json.dumps({
                'relax': int(data['historyForTimer']['relax']),
                'work': int(data['historyForTimer']['work'])
            })
            timer.history = json.dumps({
                'work': int(data['history']['work']),
                'relax': int(data['history']['relax'])
            })
            db.session.commit()
            return {}, 'success'
        else:
            return {'Error': 'Timer not found'}, 'unsuccess'
    except Exception as e:
        db.session.rollback()  
        return {'Error': str(e)}, 'unsuccess'

@swag_from('../swagger/update.yaml')
def update():
    try:
        print('upd')
        print(request.get_json())
        cont, message1 = checkPackage('timer', request.get_json()['userId'])
        if cont:
            data, message = _update(request.get_json())
            return response(data=data, message=message)
        else:
            return response(data={'state': 'not active package'}, message=message1)
    except Exception as e:
        return ERROR(e)