
from config.extensions import db
from ..model.note import Note
from flask import Blueprint, request, jsonify, current_app as app, render_template
from flasgger import swag_from
from modules.tools.response import *


def _get(data):
    try:
        note = Note.find_by_id(int(data['id']),data['userId'])
        if note != None:
            return note.serialize(),'success'
        else:
            return {
            'Can not find'
        },'unsuccess'
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'


@swag_from('../swagger/getNote.yaml')
def getNote():
    try:
        data,message = _get(request.get_json())
        return response(data=data,message=message)
    except Exception as e:
        return ERROR(e)