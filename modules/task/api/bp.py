from flask import Blueprint
from .add import add
from .delete import delete
from .edit import edit
from .get import get
from .stat_info import statInfo
from .stat_edit import statEdit
from .upload import upload


# Создаем Blueprint для задач
task_bp = Blueprint('task_bp', __name__)

# Регистрируем маршруты
task_bp.add_url_rule('/task/get', view_func=get, methods=["POST"])
task_bp.add_url_rule('/task/delete', view_func=delete, methods=["DELETE"])
task_bp.add_url_rule('/task/add', view_func=add, methods=["POST"])
task_bp.add_url_rule('/task/edit', view_func=edit, methods=["PATCH"])
task_bp.add_url_rule('/task/stat/info', view_func=statInfo, methods=["POST"])
task_bp.add_url_rule('/task/stat/edit', view_func=statEdit, methods=["PATCH"])
task_bp.add_url_rule('/task/upload', view_func=upload, methods=["POST"])
