from config.extensions import db

class TaskOfTeamModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userForId = db.Column(db.String(250))
    userCratedId = db.Column(db.String(250))
    title = db.Column(db.String(250))
    description = db.Column(db.String(250))
    column = db.Column(db.String(250))





    def serialize(self):
        return {
            'id': self.id,
            'userForId': self.userForId,
            'userCratedId': self.userCratedId,
            'title': self.title,
            'description': self.description,
            'column': self.column,
        }
   
