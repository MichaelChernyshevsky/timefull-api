import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "open sesame")
    BCRYPT_LOG_ROUNDS = 4

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SWAGGER_UI_DOC_EXPANSION = "list"
    RESTX_MASK_SWAGGER = False
    JSON_SORT_KEYS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost:6000/postgres'

class TestingConfig(Config):
    TESTING = True

class DevelopmentConfig(Config):
    BCRYPT_LOG_ROUNDS = 4

class ProductionConfig(Config):
    BCRYPT_LOG_ROUNDS = 13
    PRESERVE_CONTEXT_ON_EXCEPTION = True

ENV_CONFIG_DICT = dict(
    development=DevelopmentConfig, testing=TestingConfig, production=ProductionConfig
)

def get_config(config_name):
    return ENV_CONFIG_DICT.get(config_name, ProductionConfig)