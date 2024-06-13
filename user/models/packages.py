from config.extensions import db

class Packages(db.Model):
    back_populates= db.Column(db.Integer, db.ForeignKey('User.id'))
    pass