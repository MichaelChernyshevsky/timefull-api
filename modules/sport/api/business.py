from config.extensions import db
from ..models.model import Sport

# stat
from ...packages.model.packages import Packages


def get(data):
    try: 
        elements = Sport.find_by_userId_filtered(data['userId'],dateFrom=data['dateFrom'],dateTo=data['dateTo'],page=data['page'],countOnPage=data['countOnPage'])
        array = []
        for element in elements:
            array.append(element.serialize())
        return {'sport' : array},'success'        
    except Exception as e:
        print(str(e))
        return {'error':str(e)} , "unsuccess"
    
def delete(data):
    try: 
        Sport.query.filter_by(id=data['id']).delete()
        db.session.commit()
        return {},'success' 
    except Exception as e:
        return {'error':str(e)} , "unsuccess"
    

    
def add(data):
    try: 
        sp = Sport(
            userId = data['userId'],
            title = data['title'],
            date = data['date'],
            distant = data['distant'],
        )
        db.session.add(sp)        
        db.session.commit()
        elements = Sport.find_by_userId(data['userId'])
        print(len(elements))
        return {},'success'
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'