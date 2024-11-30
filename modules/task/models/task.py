from config.extensions import db
from .stat import TaskStat
from sqlalchemy import cast, Integer

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.String(250))
    title = db.Column(db.String(250))
    description = db.Column(db.String(2500))
    date = db.Column(db.String(2500))
    countOnDay = db.Column(db.Integer)
    countOnTask = db.Column(db.Integer)

    def serialize(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'title': self.title,
            'description': self.description,
            'date': self.date,
            'countOnDay': self.countOnDay,
            'countOnTask': self.countOnTask,
        }
   
    @classmethod
    def find_by_userId_filtered(cls, userId,dateFrom, dateTo, page, countOnPage):
        query =  cls.query.filter_by(userId=userId).filter(cls.date >= str(dateFrom), cls.date <= str(dateTo))
        paginated_results = query.paginate(page=page, per_page=countOnPage, error_out=False)
        return paginated_results.items
    
    @classmethod
    def find_by_userId(cls, userId):
        return cls.query.filter_by(userId=userId)

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id)