from ..models.user import User
from config.extensions import db


def create(data):
    try: 
        user = User(
                email= data['email'],
                password = data['password'],
             
            )
        db.session.add(user)
        db.session.commit()
        return {"user": 'user.serialize()'}
      
    except Exception as e:
        return {
            "error" : e.GetMessage()
        }
    
def edit(data):
    try: 
        user = User.find_by_id(data = data['id'])
        if(user):
            if ( user.phone):
                user.phone = data['phone']
            if ( user.sex):
                user.sex = data['sex']
            db.session.commit()
        return True
      
    except Exception as e:
        return False
    
def delete(data):
    try: 
        User.find_by_id(id = data['id']).delete()
        db.session.commit()
        return True
      
    except Exception as e:
        return False