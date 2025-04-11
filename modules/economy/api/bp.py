from flask import Blueprint
from .add import _add
from .delete import _delete
from .get import _get
from .stat import _stat
from .upload import upload


# Создаем Blueprint для экономики
economy_bp = Blueprint('economy_bp', __name__)

# Регистрируем маршруты
economy_bp.add_url_rule('/economy/add', view_func=_add, methods=["POST"])
economy_bp.add_url_rule('/economy/delete', view_func=_delete, methods=["DELETE"])
economy_bp.add_url_rule('/economy/get', view_func=_get, methods=["POST"])
economy_bp.add_url_rule('/economy/stat', view_func=_stat, methods=["POST"])
economy_bp.add_url_rule('/economy/upload', view_func=upload, methods=["POST"])
