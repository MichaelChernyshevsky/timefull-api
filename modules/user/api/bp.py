from flask import Blueprint
from .signin import _signin
from .signup import _signup
from .edit import _edit
from .info import _info
from .delete import _delete

user_bp = Blueprint('user_bp', __name__)

user_bp.add_url_rule('/signin', view_func=_signin, methods=["POST"])
user_bp.add_url_rule('/signup', view_func=_signup, methods=["POST"])
user_bp.add_url_rule('/user/edit', view_func=_edit, methods=["PATCH"])
user_bp.add_url_rule('/user/delete', view_func=_delete, methods=["DELETE"])
user_bp.add_url_rule('/user/info', view_func=_info, methods=["POST"])