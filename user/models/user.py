from config.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(250))
    password = db.Column(db.String(250))
    phone = db.Column(db.String(250))
    sex = db.Column(db.String(250))
    name = db.Column(db.String(250))
    name2 = db.Column(db.String(250))
    age = db.Column(db.Integer)
    

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'phone': self.phone,
            'sex': self.sex,
            'name': self.name,
            'name2': self.name2,
            'age': self.age,
        }
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)