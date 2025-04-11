from flask import request
from flasgger import swag_from
from modules.tools.response import response, ERROR
from modules.packages.api.chack import checkPackage
from ..models.model import Economy

def statInfoEconomy(data):
    try:
        spending = 0
        income = 0
        elements = Economy.find_by_user(data['userId'])
        for element in elements:
            if element.income:
                income += int(element.count)
            else:
                spending += int(element.count)
        return {
            'spending': spending,
            'income': income,
            'all': income - spending
        }, 'success'
    except Exception as e:
        return {'Error': str(e)}, 'unsuccess'

def _stat():
    try:
        cont, message1 = checkPackage('economy', request.get_json()['userId'])
        if cont:
            data, message = statInfoEconomy(request.get_json())
            return response(data=data, message=message)
        else:
            return response(data={'state': 'not active package'}, message=message1)
    except Exception as e:
        return ERROR(e)