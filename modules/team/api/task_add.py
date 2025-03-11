
from flask import Blueprint, request, jsonify, current_app as app, render_template
from http import HTTPStatus
from flasgger import swag_from
from modules.packages.api.chack import checkPackage
from  modules.tools.response import *


@swag_from('../swagger/task_add.yaml')
def addTask():
    try:
        cont,message1 = checkPackage('team',request.get_json()['userId'])
        if (cont):
            # data,message = deleteTask(request.get_json())
                       return ''

        else:
            return response(data={'state':'not active package'},message=message1)
        
    except Exception as e:
       return ERROR(e)
    
