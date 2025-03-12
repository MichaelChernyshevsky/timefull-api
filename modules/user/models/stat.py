from config.extensions import db

class Stat(db.Model):
    
    id = db.Column(db.BigInteger, primary_key=True)
    userId = db.Column(db.Integer)
    

    def serialize(self):
        return {
            'id': self.id,
            'userId': self.userId,
            
        }
   
    @classmethod
    def find_by_userId(cls, userId):
        return cls.query.get(userId)
    @classmethod
    def find_by_id(cls, id, userId):
        return cls.query.filter_by(id=id, userId=userId).first()