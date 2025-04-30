from flask import Blueprint
from .update import update
from .get import get

timer_bp = Blueprint('timer_bp', __name__)

timer_bp.add_url_rule('/timer/update', view_func=update, methods=["PATCH"])
timer_bp.add_url_rule('/timer/get', view_func=get, methods=["POST"])