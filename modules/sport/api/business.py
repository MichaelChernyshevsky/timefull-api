from config.extensions import db
from ..models.model import Sport

# stat
from ...packages.model.packages import Packages


def get(data):
    
    try: 
        if ( data['dateFrom']!= 0 and data['dateTo'] != 0):
            elements = Sport.find_by_userId_filtered(data['userId'],dateFrom=data['dateFrom'],dateTo=data['dateTo'],page=data['page'],countOnPage=data['countOnPage'])
        else:
            elements = Sport.find_by_userId(userId=data['userId'])
        map = {}
        for element in elements:
            map[element.id] = element.serialize() 
        return {'sport' : map},'success'        
    except Exception as e:
        print(str(e))
        return {'Error':str(e)} , "unsuccess"
    
def delete(data):
    try: 
        Sport.query.filter_by(id=data['id']).delete()
        db.session.commit()
        return {},'success' 
    except Exception as e:
        return {'Error':str(e)} , "unsuccess"
    
def save(data):
    try: 
        Sport.query.delete()
        db.session.commit() 
       
        models = data['models']
        for model in models:
            sp = Sport(
                userId = model['userId'],
                title = model['title'],
                date = model['date'],
                distant = model['distant'],
            )
            db.session.add(sp) 
        db.session.commit()
        return {},'success' 
    except Exception as e:
        return {'Error':str(e)} , "unsuccess"
    

    
def add(data):
    try: 
        sp = Sport(
            id = data['id'],
            userId = data['userId'],
            title = data['title'],
            date = data['date'],
            distant = data['distant'],
        )
        db.session.add(sp)        
        db.session.commit() 
        
        return {},'success'
    except Exception as e:
        
        return {
            'Error':str(e)
        },'unsuccess'