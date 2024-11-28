from .bp import packages_bp  

from flask import Blueprint, request, jsonify, current_app as app, render_template
from http import HTTPStatus
from flasgger import swag_from
from .chack import *
from ..list_packages import listPackages

from packages.tools.response import *


def changeState(data):
    try: 
        packages = Packages.find_by_user(data['userId'])
        match data['package']:
            case 'timer':
                if (packages.timer):
                    from packages.timer.api.business import deleteTimer
                    # deleteTimer(data)
                else:
                    from packages.timer.api.business import createTimer
                    createTimer(data)
                packages.timer = not packages.timer 
            case 'task':
                if (packages.tasks):
                    from packages.task.api.business import deleteTask
                    # deleteTask(data)
                packages.tasks = not packages.tasks
            case 'economy':
                if (packages.economy):
                    from packages.economy.api.business import deleteEconomy
                    # deleteEconomy(data)
                packages.economy = not packages.economy 
            case 'sport':
                # if (packages.sport):
                    # from packages.economy.api.business import deleteEconomy
                    # # deleteEconomy(data)
                packages.sport = not packages.sport 
            case 'note':
                # if (packages.economy):
                #     from packages.economy.api.business import deleteEconomy
                #     # deleteEconomy(data)
                packages.note = not packages.note 
        db.session.commit()
        return {},'success'


    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'


@swag_from('../swagger/change.yaml')
def _change():
    try:
        data,message = changeState(request.get_json())
        return response(data=data,message=message)
    except Exception as e:
        return ERROR(e)
    
packages_bp.add_url_rule('/packages/change',view_func=_change, methods=["POST"])
