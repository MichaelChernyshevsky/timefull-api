
from config.extensions import db

class Wine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer,db.ForeignKey('WineCategory.id'))
    country_id = db.Column(db.Integer,db.ForeignKey('Country.code'))
    year = db.Column(db.Integer)
    title = db.Column(db.String(250))
    text =  db.Column(db.String(10000))

    def serialize(self):
        return {
            'id': self.id,
            'category_id': self.category_id,
            'year' : self.year,
            'country_code' : self.country_code,
            'title' : self.title,
            'text':self.text, 
        }