from flask import Blueprint, request, jsonify, current_app as app, render_template
from http import HTTPStatus
from flasgger import swag_from
from packages.packages.api.chack import checkPackage
from packages.tools.response import *
from .func import getActive
from ..models.team import TeamModel
from config.extensions import db


@swag_from('../swagger/delete.yaml')
def delete():
    try:
        data = request.get_json()
        cont,message1 = checkPackage('task',data['userId'])
        teams = getActive(userId=data['userId'])
        if (len(teams)==0):
            return response(data= {'Error':'you dont  have active team'},message='unsuccess')
        elif (cont):
            for team in teams:
                if (team.id == data['id']):
                    team.isActive = False
            db.session.commit()
            return response(data= {},message='success')
        else:
            return response(data={},message=message1)
      
    except Exception as e:
        return ERROR(e)
    

