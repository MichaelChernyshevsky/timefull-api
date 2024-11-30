from flask import Blueprint, request, jsonify, current_app as app, render_template
from http import HTTPStatus
from flasgger import swag_from
from modules.packages.api.chack import checkPackage
from  modules.tools.response import *
from .func import getActive
from ..models.team import TeamModel
from config.extensions import db


@swag_from('../swagger/delete.yaml')
def delete():
    try:
        data = request.get_json()
        cont,message1 = checkPackage('team',data['userId'])
        teams = getActive(userId=data['userId'])

        if (len(teams)==0):
            print('2');

            return response(data= {'Error':'you dont  have active team'},message='unsuccess')
        elif (cont):

            for team in teams:
                print(team.serialize())
                if (team.id == int(data['id'])):
                    team.isActive = False
            db.session.commit()
            return response(data= {},message='success')
        else:
            return response(data={},message=message1)
      
    except Exception as e:
        return ERROR(e)
    

