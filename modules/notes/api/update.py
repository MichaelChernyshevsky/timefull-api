
from config.extensions import db
from ..model.note import Note
from flask import Blueprint, request, jsonify, current_app as app, render_template
from flasgger import swag_from
from modules.tools.response import *


def _update(data):
    try:
        added = 0
        updated = 0

        for key in data['note']:
            print(data['note'][key])
            note = Note.find_by_id(int(data['note'][key]['id']),data['note'][key]['userId'])
            if note != None:
                note.title = data['note'][key]['title']
                note.note = data['note'][key]['note']
                updated += 1
            else:
                newNote = Note(
                    id = int(data['note'][key]['id']),
                    userId = data['note'][key]['userId'],
                    title = data['note'][key]['title'],
                    note = data['note'][key]['note'],
                )
                added += 1
                db.session.add(newNote)
            db.session.commit()
            

        return {'Added':added,'Updated':updated},'success'
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'



@swag_from('../swagger/update.yaml')
def update():
    try:
        data,message = _update(request.get_json())
        return response(data=data,message=message)
    except Exception as e:
        return ERROR(e)