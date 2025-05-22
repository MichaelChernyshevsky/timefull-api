
from config.extensions import db
from ..model.note import Note
from flask import Blueprint, request, jsonify, current_app as app, render_template
from flasgger import swag_from
from modules.tools.response import *




def _clean(data):
    try:
        user_id = data['userId']
        notes_ids = data['notesId']  
        countDeleted = 0
        countUpdateOrAdd = 0

    
        
        all_notes = Note.query.filter_by(userId=user_id).all()
       
        for note in all_notes:
            if note.id not in notes_ids:
                countDeleted += 1
                db.session.delete(note)
            else:
                countUpdateOrAdd += 1


       
        db.session.commit()

        return {'Delet' : countDeleted,'UpdateOrAdd' : countUpdateOrAdd}, 'success'
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'


@swag_from('../swagger/clean.yaml')
def clean():
    try:
        data,message = _clean(request.get_json())
        return response(data=data,message=message)
    except Exception as e:
        return ERROR(e)