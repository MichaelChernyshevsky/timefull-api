from ..models.task import Task
from config.extensions import db


def add(data):
    try: 
        if  User.find_by_email(data['email']) == None :
            user = User(
                    email= data['email'],
                    password = data['password'],
                )
            
            db.session.add(user)
            db.session.commit()
            return {'user_id' : user.id}
        return {"user": 'already '}
    except Exception as e:
        print('e')

        return {
            "error" : e.GetMessage()
        }
    
def edit(data):
    try: 
        print('edit' *100)
        print(data)
        user = User.find_by_id(data['user_id'])
        print(user.serialize())
        if(user):
            if ( data['phone']):
                user.phone = data['phone']
            if ( data['sex']):
                user.sex = data['sex']
            if ( data['age']):
                user.age = data['age']
            if ( data['name']):
                user.name = data['name']
            if ( data['name2']):
                user.name2 = data['name2']
            
            db.session.commit()
            print(user.serialize())
        return True
      
    except Exception as e:
        return False
    
def get(data):
    try: 
        user = User.find_by_email(data['email'])
        if(user):
            if user.password ==data['password']:
                return user.serialize()
            return 'wrong credentials'
            
        return None
    except Exception as e:
        return None
    
def delete(data):
    try: 
        User.query.filter_by(id=data['user_id']).delete()
        db.session.commit()
        return True
      
    except Exception as e:
        return False