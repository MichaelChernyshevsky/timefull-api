from config.extensions import db

class TaskStat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.String(250))
    countDone = db.Column(db.Integer)
    countUnDone = db.Column(db.Integer)


    def serialize(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'countDone': self.countDone,
            'countUnDone': self.countUnDone,
        }
   
    @classmethod
    def find_by_userId(cls, userId):
        return cls.query.filter_by(userId=userId).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
