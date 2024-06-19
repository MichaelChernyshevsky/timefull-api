
from config.extensions import db

class WineCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    description = db.Column(db.String(500))
  

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)