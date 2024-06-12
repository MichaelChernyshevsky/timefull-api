from config.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250))
    phone = db.Column(db.String(250))
    sex = db.Column(db.String(250))

    