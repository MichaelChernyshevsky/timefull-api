from config.extensions import db

class Packages(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.String(250))
    timer = db.Column(db.Boolean)
    task = db.Column(db.Boolean)
    economy = db.Column(db.Boolean)
    

    def serialize(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'timer': self.timer,
            'task': self.task,
            'economy': self.economy,
            'note':  self.economy,
        
        }
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_by_user(cls, userId):
        return cls.query.filter_by(userId=userId).first()
