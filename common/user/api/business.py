from config.extensions import db
from ...packages.model.packages import Packages
from ..models import *

# stat
from packages import *


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

            return {'userId' : user.id},'success'
        return False, 'unsuccess'
    except Exception as e:
        
        return {
            "error" : e.GetMessage()
        },'unsuccess'
    
def edit(data):
    # try: 
        user = User.find_by_id(data['userId'])
        print(data)
        if(user):
            print(1)
            if ( data['phone']):
                print('p')
                
                user.phone = data['phone']
            if ( data['sex'] or  data['age'] or data['name'] or data['name2']):
                print('2')
                info = Info.find_by_userId(data['userId'])
                print(info.serialize())
                if ( data['sex']):
                    print(data['sex'])
                    info.sex = data['sex']
                # if ( data['age'] != 0):
                #     print(type(data['age']))
                #     info.age = data['age']
            #     if ( data['name']):
            #         print('n')

            #         info.name = data['name']
            #     if ( data['name2']):
            #         print('n2')
            #         info.name2 = data['name2']
            db.session.commit()
        return {} ,'success'
    
    # except Exception as e:
    #     return {} , "unsuccess"
        
    
def getId(data):
    try: 
        user = User.find_by_email(data['email'])
        if(user):
            if user.password ==data['password']:
                return {'userId' : user.id},'success'
            
            return False, 'wrong credentials'
            
        return False , "unsuccess" 
    except Exception as e:
        return False , "unsuccess"
    

    
def getById(data):
    try: 
        user = User.find_by_id(data['userId'])
        if(user):
            return user.serialize() , "success"
            
        return False , "unsuccess"
    except Exception as e:
        return False , "unsuccess"
    


def delete(data):
    try: 
        User.query.filter_by(id=data['userId']).delete()
        db.session.commit()
        return True ,'success'
      
    except Exception as e:
        return False , "unsuccess"
    
def stat(data):
    try: 
        stat = {"timer":"","economy":"","tasks":""}
        packages = Packages.find_by_id(data['userId'])
        if packages:
            if packages.timer:
                stat["timer"] = statInfoTimer(data)
            if packages.tasks:
                stat["economy"] = statInfoEconomy(data)
            if packages.economy:
                stat["tasks"] = statInfoTask(data)
            return stat ,'success'

        return False , "unsuccess"
      
    except Exception as e:
        return False , "unsuccess"

    