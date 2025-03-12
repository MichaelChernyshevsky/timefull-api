
from config.extensions import db
from ..model.note import Note
from flask import Blueprint, request, jsonify, current_app as app, render_template
from flasgger import swag_from
from modules.tools.response import *


def _get(data):
    try:
        notes = Note.find_by_user_notes_notfull(data['userId'])
        notesList = {}
        for note in notes:
            notesList[note[0]] = {
                'id' : note[0],
                'title' : note[1],
            }
      

        print(notesList)
        return {'notes': notesList},'success'
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'


@swag_from('../swagger/getNotes.yaml')
def getNotes():
    try:
        data,message = _get(request.get_json())
        return response(data=data,message=message)
    except Exception as e:
        return ERROR(e)