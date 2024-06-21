from config.extensions import db
from .info import Info

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(250))
    password = db.Column(db.String(250))
    phone = db.Column(db.String(250))
    packages = db.Column(db.Integer)
    info = db.Column(db.Integer)
    admin = db.Column(db.Boolean)
    creator = db.Column(db.Boolean)
    subscribed = db.Column(db.Boolean)


    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'phone': self.phone,
            'packagesId': self.packages,
            'info' : Info.find_by_id(self.info).serialize(),
            'admin': self.admin,
            'creator': self.creator,
            'subscribed' : self.subscribed,
        }
 
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()