
from flask import Blueprint, request, jsonify, current_app as app, render_template
from flasgger import swag_from
from .chack import *
from modules.tools.response import *


def _changeState(data):
    try: 
        state = 'Not changed'
        packages = Packages.find_by_user(data['userId'])
        match data['package']:
            case 'timer':
                if (packages.timer):
                  pass
                else:
                    from modules.timer.api.business import createTimer
                    createTimer(data)
                packages.timer = not packages.timer 
                state = 'changed'
            case 'task':
                packages.tasks = not packages.tasks
                state = 'changed'
            case 'team':
                packages.team = not packages.team
                state = 'changed'
            case 'economy':
                packages.economy = not packages.economy 
                state = 'changed'
            case 'sport':
                packages.sport = not packages.sport 
                state = 'changed'
            case 'note':
                packages.note = not packages.note 
                state = 'changed'
        db.session.commit()
        return {'state':state},'success'
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
    
