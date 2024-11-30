from flasgger import Swagger

from  modules.exports import *



def register_blueprints(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(packages_bp)
    app.register_blueprint(admin_bp)
    # packages
    app.register_blueprint(task_bp)
    app.register_blueprint(timer_bp)
    app.register_blueprint(economy_bp)
    app.register_blueprint(sport_bp)
    app.register_blueprint(team_bp)


    

    





    





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