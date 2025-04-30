

from flask import Blueprint, request, jsonify, current_app as app, render_template
from modules.tools.response import *
from flasgger import swag_from

from .info import _info



admin_bp = Blueprint('admin_bp', __name__)
admin_bp.add_url_rule('/admin/info',view_func=_info, methods=["POST"])