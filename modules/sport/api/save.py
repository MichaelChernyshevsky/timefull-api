from flask import request
from flasgger import swag_from
from modules.tools.response import response, ERROR
from modules.packages.api.chack import checkPackage
from ..models.model import Sport
from config.extensions import db

def save(data):
    try: 
        countDeleted = 0
        countAded= 0
        countUpdated = 0

        user_id = data['userId']
        existing_sports = Sport.query.filter_by(userId=user_id).all()
        model_ids = data['models'].keys()
        for model in existing_sports:
            if str(model.id) not in model_ids:
                countDeleted +=1
                db.session.delete(model)
        for key in model_ids:

            _model = data['models'][key]
            existing_sport = Sport.query.filter_by(id= int(_model['id'])).all()
            added = False
            for sp in existing_sport:
                if sp.userId == user_id:
                    if sp:

                        sp.title = _model['title']
                        sp.date = _model['date']
                        sp.distant = _model['distant']
                        countUpdated += 1
                    added = True
            if added == False:
                new_sport = Sport(
                    id=_model['id'], 
                    userId=user_id,
                    title=_model['title'],
                    date=_model['date'],
                    distant=_model['distant'],
                )
                countAded +=1
                db.session.add(new_sport)
        db.session.commit()
        return {'Deleted':countDeleted,'Add':countAded,'Update':countUpdated}, 'success' 
    except Exception as e:
        return {'Error': str(e)}, 'unsuccess'

@swag_from('../swagger/save.yaml')
def _save():
    try:
        cont, message1 = checkPackage('sport', request.get_json()['userId'])
        if (cont):
            data, message = save(request.get_json())
            return response(data=data, message=message)
        else:
            return response(data={'state': 'not active package'}, message=message1)
    except Exception as e:
        return ERROR(e)