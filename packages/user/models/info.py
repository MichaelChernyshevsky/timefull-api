from config.extensions import db

class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer)
    sex = db.Column(db.String(250))
    name = db.Column(db.String(250))
    name2 = db.Column(db.String(250))
    age = db.Column(db.Integer)
    

    def serialize(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'sex': self.sex,
            'name': self.name,
            'name2': self.name2,
            'age': self.age,
        }
   
    @classmethod
    def find_by_userId(cls, userId):
        return cls.query.filter_by(userId=userId).first()
    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)
    

    