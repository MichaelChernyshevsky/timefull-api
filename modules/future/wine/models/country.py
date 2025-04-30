from config.extensions import db

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    code = db.Column(db.String(20))
  

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
        }