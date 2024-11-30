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
    def find_by_userId_filtered(cls, userId,dateFrom, dateTo, page, countOnPage):
        query = cls.query.filter_by(userId=userId).filter(cls.date >= str(dateFrom), cls.date <= str(dateTo))
        paginated_results = query.paginate(page=page, per_page=countOnPage, error_out=False)
        return paginated_results.items
    
    @classmethod
    def find_by_userId(cls, userId):
        return cls.query.filter_by(userId=userId)
    
    @classmethod
    def find_by_id(cls, id,dateFrom, dateTo, page, countOnPage):
        query = cls.query.filter_by(id=id).filter(cls.date >= dateFrom, cls.date <= dateTo)
        paginated_results = query.paginate(page=page, per_page=countOnPage, error_out=False)
        return paginated_results.items