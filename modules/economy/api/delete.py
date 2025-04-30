from flask import request
from flasgger import swag_from
from modules.tools.response import response, ERROR
from modules.packages.api.chack import checkPackage
from ..models.model import Economy
from config.extensions import db

def deleteEconomy(data):
    try:
        Economy.query.filter_by(id=data['id']).delete()
        db.session.commit()
        return {}, 'success'
    except Exception as e:
        return {'Error': str(e)}, 'unsuccess'
    
@swag_from('../swagger/delete.yaml')
def _delete():
    try:
        cont, message1 = checkPackage('economy', request.get_json()['userId'])
        if cont:
            data, message = deleteEconomy(request.get_json())
            return response(data=data, message=message)
        else:
            return response(data={'state': 'not active package'}, message=message1)
    except Exception as e:
        return ERROR(e)