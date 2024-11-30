from config.extensions import db
from ..models import *

# stat
from ...packages.model.packages import Packages

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
          

            # info
            info = Info(userId = user.id)
            db.session.add(info)
            db.session.commit()
            user.info = info.id
            db.session.commit()
            # # package
            package = Packages( userId = user.id)
            db.session.add(package)
            db.session.commit()
            user.packages = package.id
            db.session.commit()

            return {'userId' : user.id},'success'
        return {}, 'success'
    except Exception as e:
        return {},'unsuccess'
    
def edit(data):
    try: 
        user = User.find_by_id(data['userId'])
        if(user):
            if ( data['phone']):
                user.phone = data['phone']
            # if ( data['admin']):
            #     user.admin =  data['admin']
            if ( data['sex'] or  data['age'] or data['name'] or data['name2']):
                info = Info.find_by_userId(data['userId'])
                if (info):
                    if ( data['sex']):
                        info.sex =  data['sex']
                    if ( data['age'] != 0):
                        info.age =  data['age']
                    if ( data['name']):
                        info.name =  data['name']
                    if ( data['name2']):
                        info.name2 =  data['name2']
                    
                    db.session.commit()
            return {} ,'success'
        return {} ,'unsuccess'
    except Exception as e:
        return {} , "unsuccess"
        
    
def getId(data):
    try: 
        user = User.find_by_email(data['email'])
        if(user):
            if user.password ==data['password']:
                return {'userId' : user.id},'success'
            
            return {}, 'wrong credentials'
            
        return {} , "unsuccess" 
    except Exception as e:
        return {} , "unsuccess"
    

    
def info(data):
    try: 
        user = User.find_by_id(data['userId'])
        if(user):
            return user.serialize() , "success"
        return {} , "unsuccess"
    except Exception as e:
        print(e)
        return {} , "unsuccess"
    


def delete(data):
    try: 
        User.query.filter_by(id=data['userId']).delete()
        db.session.commit()
        return {} ,'success'
      
    except Exception as e:
        return {} , "unsuccess"
    
def stat(data):
    try: 
        stat = {"timer":"","economy":"","task":""}
        packages = Packages.find_by_id(data['userId'])
        # if packages:
        #     if packages.timer:
        #         stat["timer"] = statInfoTimer(data)
        #     if packages.tasks:
        #         stat["economy"] = statInfoEconomy(data)
        #     if packages.economy:
        #         stat["tasks"] = statInfoTask(data)
        #     return stat ,'success'

        return {} , "unsuccess"
      
    except Exception as e:
        return {} , "unsuccess"

    