from config.extensions import db
from ..models.economy import Economy


def add(data):
    try: 
        economy = Economy(
            user_id = data['user_id'],
            income = data['income'],
            count = data['count'],
            date = data['date'],
            title = data['title'],
            description = data['description'],
        )
        db.session.add(economy)
        db.session.commit()
        return True
    except Exception as e:
        return False
    
def edit(data):
    try: 
        return True
    except Exception as e:
        return False
    
def get(data):
    try: 
        e = []
        _elements = Economy.find_by_user(data['user_id'])
        for element in _elements:
            e.append(element.serialize())
        
        return e
    except Exception as e:
        return False
    
def delete(data):
    try: 
        Economy.query.filter_by(id=data['id']).delete()
        db.session.commit()
        return True
    except Exception as e:
        return False