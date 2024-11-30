
from flask import Blueprint, request, jsonify, current_app as app, render_template
from flasgger import swag_from
from modules.packages.api.chack import checkPackage
from  modules.tools.response import *
from ..models.team import TeamModel
from config.extensions import db
from .func import getActive


@swag_from('../swagger/create.yaml')
def create():
    try:
        data = request.get_json()
        cont,message1 = checkPackage('team',data['userId'])
        teams = getActive(userId=data['userId'])
        if (len(teams)>0):
            return response(data= {'Error':'you already have active team'},message='unsuccess')
        elif (cont):
            team = TeamModel(
                userOwnerId = data['userId'],
                title = data['title'],
                description = data['description'],
                columns = data['columns'],
                isActive = True,
                users = '',
            )
            db.session.add(team)        
            db.session.commit()
            return response(data= {},message='success')
        else:
            return response(data={},message=message1)
      
    except Exception as e:
        return ERROR(e)
    

