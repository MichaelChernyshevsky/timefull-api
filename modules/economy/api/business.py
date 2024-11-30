from config.extensions import db
from ..models.economy import Economy


def add(data):
    try: 
        economy = Economy(
            userId = data['userId'],
            income = data['income'],
            count = data['count'],
            date = data['date'],
            title = data['title'],
            description = data['description'],
        )
        db.session.add(economy)        
        db.session.commit()
        return {},'success'
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'

        
    
def get(data):
    try: 
        e = []
        _elements = Economy.find_by_userId_filtered(data['userId'],dateFrom=data['dateFrom'],dateTo=data['dateTo'],page=data['page'],countOnPage=data['countOnPage'])
        for element in _elements:
            e.append(element.serialize())
        return {'data':e},'success'
    except Exception as e:
        return {'error':e},'unsuccess'

        
    
def statInfoEconomy(data):
    try: 
        spending = 0
        income = 0
        _elements = Economy.find_by_user(data['userId'])
        for element in _elements:
            if (element.income):
                income += int(element.count)
            else:
                spending += int(element.count)
        return {
            'spending':spending,
            'income': income,
            'all' : income - spending
        },'success'
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'

        
    
def deleteEconomy(data):
    try: 
        Economy.query.filter_by(id=data['id']).delete()
        db.session.commit()
        return {},'success'
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'

        