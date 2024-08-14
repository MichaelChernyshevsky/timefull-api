from config.extensions import db


class Sport(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.String(250))
    title = db.Column(db.String(250))
    distant = db.Column(db.Integer)
    date = db.Column(db.String(2500))
  

    def serialize(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'title': self.title,
            'distant': self.distant,
            'date': self.date,
        }
   
    @classmethod
    def find_by_userId(cls, userId):
        return cls.query.filter_by(userId=userId).all()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id)