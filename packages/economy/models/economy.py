from config.extensions import db

class Economy(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.String(250))
    income = db.Column(db.Boolean)
    count = db.Column(db.String(1000))
    date = db.Column(db.String(1000))
    title = db.Column(db.String(250))
    description =  db.Column(db.String(1000))


    def serialize(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'income': self.income,
            'count': self.count,
            'date': self.date,
            'title': self.title,
            'description': self.description,
        }
    @classmethod
    def find_by_user(cls, userId):
        return cls.query.filter_by(userId=userId)
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)