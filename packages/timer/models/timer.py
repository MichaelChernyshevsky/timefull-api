from config.extensions import db

class Timer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(250))
    history = db.Column(db.String(1000))
    stat = db.Column(db.String(1000))

    

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'history': self.history,
            'stat': self.stat,
        }
    @classmethod
    def find_by_user(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)