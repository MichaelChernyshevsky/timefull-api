from ..models.user import User
from config.extensions import db


def create(data):
    try: 
        print('create '*100)
        user = User(
                email= data['email'],
                password = data['password'],
                phone = '',
                sex = '',
            )
        print('created '*100)
        
        db.session.add(user)
        db.session.commit()

        print('success ' *100)
        return {"user": user.serialize()}
      
    except Exception as e:
        return {
            "error" : e.GetMessage()
        }
    