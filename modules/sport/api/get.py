from flask import request
from flasgger import swag_from
from modules.tools.response import response, ERROR
from modules.packages.api.chack import checkPackage
from ..models.model import Sport

def get(data):
    try: 
        if ( data['dateFrom'] != 0 and data['dateTo'] != 0):
            elements = Sport.find_by_userId_filtered(data['userId'], dateFrom=data['dateFrom'], dateTo=data['dateTo'], page=data['page'], countOnPage=data['countOnPage'])
        else:
            elements = Sport.find_by_userId(userId=data['userId'])
        map = {}
        for element in elements:
            map[element.id] = element.serialize() 
        return {'sport': map}, 'success'        
    except Exception as e:
        print(str(e))
        return {'Error': str(e)}, 'unsuccess'

@swag_from('../swagger/get.yaml')
def _get():
    try:
        cont, message1 = checkPackage('sport', request.get_json()['userId'])
        if (cont):
            data, message = get(request.get_json())
            return response(data=data, message=message)
        else:
            return response(data={'state': 'not active package'}, message=message1)
    except Exception as e:
        return ERROR(e)