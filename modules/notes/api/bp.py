from flask import Blueprint
from .delete import delete
from .update import update
from .get_notes import getNotes
from .get_note import getNote



notes_bp = Blueprint('notes_bp', __name__)
notes_bp.add_url_rule('/notes/note/update',view_func=update, methods=["POST"])
notes_bp.add_url_rule('/notes/note/delete',view_func=delete, methods=["DELETE"])
notes_bp.add_url_rule('/notes/note',view_func=getNote, methods=["POST"])
notes_bp.add_url_rule('/notes',view_func=getNotes, methods=["POST"])




