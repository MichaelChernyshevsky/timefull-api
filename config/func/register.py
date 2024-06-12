from packages.exports import *
from flasgger import Swagger



def register_blueprints(app):
    app.register_blueprint(news_bp)




def register_swagger(app):
    SWAGGER_TEMPLATE = {
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "\JWT access token"
            }
        }
    }
    swag = Swagger(app, template=SWAGGER_TEMPLATE)
    app.config["SWAGGER"] = {
        "openapi": "3.0.0",
        "title": "Daytime api",
        "description": ""
    }