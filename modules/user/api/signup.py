from flask import request
from flasgger import swag_from
from modules.tools.response import response, ERROR
from ..models import User, Info, Stat
from ...packages.model.packages import Packages
from config.extensions import db

@swag_from('../swagger/signup.yaml')
def _signup():
    try:
        data, message = create(request.get_json())
        return response(data=data, message=message)
    except Exception as e:
        print(e)
        return ERROR(e)

def create(data):
    try:
        if User.find_by_email(data['email']) is None:
            # Создаем пользователя
            user = User(
                email=data['email'],
                password=data['password'],
            )
            db.session.add(user)
            db.session.commit()

            # Создаем информацию о пользователе
            info = Info(userId=user.id)
            db.session.add(info)
            db.session.commit()
            user.info = info.id
            db.session.commit()

            # Создаем пакет для пользователя
            package = Packages(userId=user.id)
            db.session.add(package)
            db.session.commit()
            user.packages = package.id
            db.session.commit()

            return {'userId': user.id}, 'success'
        return {}, 'success'
    except Exception as e:
        return {}, 'unsuccess'