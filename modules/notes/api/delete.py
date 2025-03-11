
from config.extensions import db
from ..model.note import Note
from flask import Blueprint, request, jsonify, current_app as app, render_template
from flasgger import swag_from
from modules.tools.response import *




def _delete(data):
    try:
        Note.query.filter_by(id=data['id']).delete()
        db.session.commit()
        return {},'success'
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'


@swag_from('../swagger/delete.yaml')
def delete():
    try:
        data,message = _delete(request.get_json())
        return response(data=data,message=message)
    except Exception as e:
        return ERROR(e)