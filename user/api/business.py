from ..models.user import User
from config.extensions import db


def create(data):
    print('start')
    try: 
        if  User.find_by_email(data['email']) == None :
            print('1');
            user = User(
                    email= data['email'],
                    password = data['password'],
                )
            print('2');
            
            db.session.add(user)
            db.session.commit()
            print('s')
            return {"user": user.serialize()}
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
        user = User.find_by_id(data['user_id'])
        if(user):
            return user.serialize()
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