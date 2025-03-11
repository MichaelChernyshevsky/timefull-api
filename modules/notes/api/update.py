
from config.extensions import db
from ..model.note import Note
from flask import Blueprint, request, jsonify, current_app as app, render_template
from flasgger import swag_from
from modules.tools.response import *

def _update(data):
    try:
        added = 0
        updated = 0
        deleted = 0

        user_id = data['note'][list(data['note'].keys())[0]]['userId']  
        existing_note_ids = {note.id for note in Note.query.filter_by(userId=user_id).all()}

        passed_note_ids = set()

        for key in data['note']:
            note_data = data['note'][key]
            note_id = int(note_data['id'])
            passed_note_ids.add(note_id)

            note = Note.find_by_id(note_id, user_id)
            if note is not None:
                note.title = note_data['title']
                note.note = note_data['note']
                updated += 1
            else:
                new_note = Note(
                    id=note_id,
                    userId=user_id,
                    title=note_data['title'],
                    note=note_data['note'],
                )
                db.session.add(new_note)
                added += 1

        ids_to_delete = existing_note_ids - passed_note_ids
        for note_id in ids_to_delete:
            note_to_delete = Note.find_by_id(note_id, user_id)
            if note_to_delete:
                db.session.delete(note_to_delete)
                deleted += 1

        db.session.commit()

        return {'Added': added, 'Updated': updated, 'Deleted': deleted}, 'success'
    except Exception as e:
        db.session.rollback()  
        return {'Error': str(e)}, 'unsuccess'



@swag_from('../swagger/update.yaml')
def update():
    try:
        data,message = _update(request.get_json())
        return response(data=data,message=message)
    except Exception as e:
        return ERROR(e)