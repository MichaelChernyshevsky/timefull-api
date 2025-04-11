from flask import request
from flasgger import swag_from
from modules.tools.response import response, ERROR
from modules.packages.api.chack import checkPackage
from ..models.model import Economy
from config.extensions import db

def _upload(data):
    try: 
        countDeleted = 0
        countAded= 0
        countUpdated = 0

        user_id = data['userId']
        existing = Economy.query.filter_by(userId=user_id).all()
        model_ids = data['economy'].keys()
        for model in existing:
            if str(model.id) not in model_ids:
                countDeleted +=1
                db.session.delete(model)
        for key in model_ids:
            _model = data['economy'][key]
            currentModel = Economy.query.filter_by(id= _model['id'], userId=user_id).first()
            added = False
            if currentModel:
                currentModel.title = _model['title']
                currentModel.date = _model['date']
                currentModel.description = _model['description']
                currentModel.count = _model['count']
                currentModel.income = _model['income']
                countUpdated += 1
                added = True
            if added == False:
                new_sport = Economy(
                    id=_model['id'], 
                    userId=user_id,
                    title=_model['title'],
                    date=_model['date'],
                    description=_model['description'],
                    count=_model['count'],
                    income=_model['income'],
                )
                countAded +=1
                db.session.add(new_sport)
        db.session.commit()
        return {'Deleted':countDeleted,'Add':countAded,'Update':countUpdated}, 'success' 
    except Exception as e:
        return {'Error': str(e)}, 'unsuccess'

@swag_from('../swagger/upload.yaml')
def upload():
    try:
        cont, message1 = checkPackage('economy', request.get_json()['userId'])
        if (cont):
            data, message = _upload(request.get_json())
            return response(data=data, message=message)
        else:
            return response(data={'state': 'not active package'}, message=message1)
    except Exception as e:
        return ERROR(e)