

from config.extensions import db

class Note(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    userId = db.Column(db.String(250))
    title = db.Column(db.String())
    note = db.Column(db.String())


    def serialize(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'title': self.title,
            'note': self.note,
        }
    
    @classmethod
    def find_by_id(cls, id, userId):
        return cls.query.filter_by(id=id, userId=userId).first()
    
    @classmethod
    def find_by_user(cls, userId):
        return cls.query.filter_by(userId=userId).first()
    
    @classmethod
    def find_by_user_notes_notfull(cls, userId):
        return cls.query.with_entities(cls.id, cls.title).filter_by(userId=userId).all()

