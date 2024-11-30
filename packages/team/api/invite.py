from flask import Blueprint, request, jsonify, current_app as app, render_template
from http import HTTPStatus
from flasgger import swag_from
from packages.packages.api.chack import checkPackage
from packages.tools.response import *



@swag_from('../swagger/invite.yaml')
def invite():
    try:
        cont,message1 = checkPackage('task',request.get_json()['userId'])
        if (cont):
            # data,message = deleteTask(request.get_json())
                        return ''

        else:
            return response(data={},message=message1)
        
        
    except Exception as e:
       return ERROR(e)
    