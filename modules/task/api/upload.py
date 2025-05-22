from flask import request
from flasgger import swag_from
from modules.tools.response import response, ERROR
from modules.packages.api.chack import checkPackage
from ..models.task import Task
from config.extensions import db

def _upload(data):
    try: 
        countDeleted = 0
        countAded= 0
        countUpdated = 0
        user_id = data['userId']
        existing = Task.query.filter_by(userId=user_id).all()
        model_ids = data['tasks'].keys()
        for model in existing:
            if str(model.id) not in model_ids:
                countDeleted +=1
                db.session.delete(model)
        for key in model_ids:
            _model = data['tasks'][key]
            currentModel = Task.query.filter_by(id= _model['id'], userId=user_id).first()
            added = False
            if currentModel:
                currentModel.title = _model['title']
                currentModel.date = _model['date']
                currentModel.description = _model['description']
                currentModel.countOnTask = _model['countOnTask']
                currentModel.countOnDay = _model['countOnTask']
                countUpdated += 1
                added = True
            if added == False:
                new_sport = Task(
                    id=_model['id'], 
                    userId=user_id,
                    title=_model['title'],
                    date=_model['date'],
                    description=_model['description'],
                    countOnDay=_model['countOnTask'],
                    countOnTask=_model['countOnTask'],
                )
                countAded +=1
                db.session.add(new_sport)
        db.session.commit()
        return {'Deleted':countDeleted,'Add':countAded,'Update':countUpdated}, 'success' 
    except Exception as e:
        return {'Error': str(e)}, 'unsuccess'

# @swag_from('../swagger/upload.yaml')
def upload():
    try:
        cont, message1 = checkPackage('task', request.get_json()['userId'])
        if cont:
            data, message = _upload(request.get_json())
            return response(data=data, message=message)
        else:
            return response(data={'state': 'not active package'}, message=message1)
    except Exception as e:
        return ERROR(e)