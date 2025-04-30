from flask import request
from flasgger import swag_from
from modules.tools.response import response, ERROR
from modules.packages.api.chack import checkPackage
from ..models.timer import Timer
from ..models.timer import Timer
from ..models.timer import emptyHistory, emptyStat
from config.extensions import db

def createTimer(data):
    try:
            data = Timer(
                userId = data['userId'],
                history = emptyHistory(),
                stat = emptyStat()
            )
            db.session.add(data)
            db.session.commit()
            return True
    except Exception as e:
        return False
