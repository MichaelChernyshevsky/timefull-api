from config.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250))
    password = db.Column(db.String(250))
    phone = db.Column(db.String(250))
    sex = db.Column(db.String(250))
    # packages = db.relationship('Packages')
    

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'phone': self.phone,
            'sex': self.sex,
        }
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)