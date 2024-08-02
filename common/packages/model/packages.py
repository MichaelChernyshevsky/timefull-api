from config.extensions import db

class Packages(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    timer = db.Column(db.Boolean)
    task = db.Column(db.Boolean)
    economy = db.Column(db.Boolean)
    

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'timer': self.timer,
            'task': self.task,
            'economy': self.economy,
        
        }
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_by_user(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()
