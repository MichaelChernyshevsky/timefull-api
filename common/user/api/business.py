from ..models.user import User
from config.extensions import db
from ...packages.model.packages import Packages
from ..models.info import Info



def create(data):
    try: 
        if  User.find_by_email(data['email']) == None :
            # user
            user = User(
                    email= data['email'],
                    password = data['password'],
                )
            db.session.add(user)
            db.session.commit()
            # package
            package = Packages( userId = user.id)
            db.session.add(package)
            db.session.commit()
            user.packages = package.id
            db.session.commit()
             # info
            info = Info(userId = user.id)
            db.session.add(info)
            db.session.commit()
            user.info = info.id
            db.session.commit()

            return {'userId' : user.id}
        return {"user": 'already '}
    except Exception as e:
        
        return {
            "error" : e.GetMessage()
        }
    
def edit(data):
    try: 
        user = User.find_by_id(data['userId'])
        if(user):
            if ( data['phone']):
                user.phone = data['phone']
            if ( data['sex'] or  data['age'] or data['name'] or data['name2']):
                info = Info.find_by_userId(data['userId'])
                if ( data['sex']):
                    info.sex = data['sex']
                if ( data['age']):
                    info.age = data['age']
                if ( data['name']):
                    info.name = data['name']
                if ( data['name2']):
                    info.name2 = data['name2']
            
            db.session.commit()
        return True
    
    except Exception as e:
        return False
        
    
def getId(data):
    try: 
        user = User.find_by_email(data['email'])
        if(user):
            if user.password ==data['password']:
                return {'userId' : user.id}
            return 'wrong credentials'
            
        return False
    except Exception as e:
        return False
    
def get(data):
    try: 
        user = User.find_by_email(data['email'])
        if(user):
            if user.password ==data['password']:
                return user.serialize()
            return 'wrong credentials'
            
        return False
    except Exception as e:
        return False
    
def getById(data):
    try: 
        user = User.find_by_id(data['userId'])
        if(user):
            return user.serialize()
            
        return False
    except Exception as e:
        return False
    


def delete(data):
    try: 
        User.query.filter_by(id=data['userId']).delete()
        db.session.commit()
        return True
      
    except Exception as e:
        return False