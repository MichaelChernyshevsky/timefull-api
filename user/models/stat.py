from config.extensions import db

class Stat(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer)
    

 
    

    def serialize(self):
        return {
            'id': self.id,
            'userId': self.userId,
            
        }
   

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.get(user_id)
    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)