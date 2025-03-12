from flask import Blueprint


from .create import create
from .delete import delete
from .generate import keyGenerate
from .invite import invite
from .task_add import addTask
from .task_delete import deleteTask
from .uninvite import uninvite







team_bp = Blueprint('team_bp', __name__)
team_bp.add_url_rule('/team/create',view_func=create, methods=["POST"])
team_bp.add_url_rule('/team/delete',view_func=delete, methods=["DELETE"])
team_bp.add_url_rule('/team/invite',view_func=invite, methods=["POST"])
team_bp.add_url_rule('/team/key/generate',view_func=keyGenerate, methods=["POST"])
team_bp.add_url_rule('/task/uninvite',view_func=uninvite, methods=["POST"])
team_bp.add_url_rule('/task/task/add',view_func=addTask, methods=["POST"])
team_bp.add_url_rule('/task/task/delete',view_func=deleteTask, methods=["DELETE"])




