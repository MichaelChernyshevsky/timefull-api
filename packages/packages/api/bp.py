
from flask import Blueprint
from .get import get
from .change import change
from .info import info


    


packages_bp = Blueprint('packages_bp', __name__)
packages_bp.add_url_rule('/packages/get',view_func=get, methods=["POST"])
packages_bp.add_url_rule('/packages/change',view_func=change, methods=["POST"])
packages_bp.add_url_rule('/packages/info',view_func=info, methods=["POST"])







