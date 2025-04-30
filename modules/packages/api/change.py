
from flask import Blueprint, request, jsonify, current_app as app, render_template
from flasgger import swag_from
from .chack import *
from modules.tools.response import *


def _changeState(data):
    try: 
        state = 'Not changed'
        count = 0
        packages = Packages.find_by_user(data['userId'])
        for package in data['packages']:
            match package['package']:
                case 'timer':
                    packages.timer =  package['state']
                    state = 'changed'
                    count += 1
                case 'task':
                    packages.tasks =  package['state']
                    state = 'changed'
                    count += 1
                case 'team':
                    packages.team =  package['state']
                    state = 'changed'
                    count += 1
                case 'economy':
                    packages.economy =  package['state']
                    state = 'changed'
                    count += 1
                case 'sport':
                    packages.sport =  package['state']
                    state = 'changed'
                    count += 1
                case 'note':
                    packages.note =  package['state']
                    state = 'changed'
                    count += 1
        db.session.commit()
        return {'state':state,'count':count},'success'
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'

@swag_from('../swagger/change.yaml')
def change():
    try:
        data,message = _changeState(request.get_json())
        return response(data=data,message=message)
    except Exception as e:
        return ERROR(e)
    
