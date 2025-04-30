from flask import Blueprint
from .get import _get
from .add import _add
from .save import _save
from .delete import _delete

sport_bp = Blueprint('sport_bp', __name__)

sport_bp.add_url_rule('/sport/get', view_func=_get, methods=["POST"])
sport_bp.add_url_rule('/sport/add', view_func=_add, methods=["POST"])
sport_bp.add_url_rule('/sport/save', view_func=_save, methods=["POST"])
sport_bp.add_url_rule('/sport/delete', view_func=_delete, methods=["DELETE"])