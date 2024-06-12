from flask_caching import Cache
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
cache = Cache(config={'CACHE_TYPE': 'simple'})
