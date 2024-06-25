from config.extensions import db
from ..func.json import fromStringToJson

class Timer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.String(250))
    history = db.Column(db.String(1000))
    stat = db.Column(db.String(1000))

    

    def serialize(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'history': fromStringToJson(self.history),
            'stat':fromStringToJson(self.stat),
        }
    @classmethod
    def find_by_user(cls, userId):
        return cls.query.filter_by(userId=userId).first()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)