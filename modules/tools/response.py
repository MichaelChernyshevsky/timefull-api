from flask import jsonify
from http import HTTPStatus
from flask import  current_app as app

SUCCESS = 'success'
UNSUCCESS = 'unsuccess'

def response(data,message):
    return jsonify(    
            message = message,
            data = data,
        ), HTTPStatus.OK


def ERROR (e):
    app.logger.error(str(e))
    return jsonify(    
                message = {
                    "error":str(e)
                },
                data = {},
            ), HTTPStatus.INTERNAL_SERVER_ERROR