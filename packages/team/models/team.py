from config.extensions import db

class TeamModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userOwnerId = db.Column(db.String(250))
    inviteKey = db.Column(db.String(250))
    title = db.Column(db.String(250))
    description = db.Column(db.String(250))
    columns = db.Column(db.String(250))




    def serialize(self):
        return {
            'id': self.id,
            'userOwnerId': self.userOwnerId,
            'inviteKey': self.inviteKey,
            'title': self.title,
            'description': self.description,
        }
   
