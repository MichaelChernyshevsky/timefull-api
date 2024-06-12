from dotenv import load_dotenv
from flask import Flask
import os

from flask_cors import CORS
from flask_migrate import Migrate
from config.func.register import *

from config.config import get_config

from config.extensions import (
    db,
    bcrypt,
    migrate
)


load_dotenv()

def create_app(config_name=os.getenv("FLASK_ENV", "development"))-> Flask:
    app = Flask(__name__)
    CORS(app, max_age=6000)
    app.config.from_object(get_config(config_name))
    
    init_app(app)
    register_blueprints(app=app)
    register_swagger(app=app)
    return app


def init_app(app):
    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

