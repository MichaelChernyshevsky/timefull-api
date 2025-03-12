from config.extensions import db

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer)
    title = db.Column(db.String(250))
    text =  db.Column(db.String(10000))

    def serialize(self):
        return {
            'id': self.id,
            'category_id': self.category_id,
            'title' : self.title,
            'text':self.text, 
        }