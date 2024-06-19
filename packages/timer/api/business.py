from config.extensions import db
from ..models.timer import Timer
from ..func.json import *
def create(data):
    try: 
        data = Timer(
            user_id = data['user_id'],
            history = '',
            stat = ''
        )
        db.session.add(data)
        db.session.commit()
        return True
    except Exception as e:
        return False
    
def editStat(data):
    try: 
        data = Timer.find_by_user(data['user_id'])
        data.stat = editStatFunc( data= data.stat)
        db.session.commit()
        return True
      
    except Exception as e:
        return False
    
def editHistory(data):
    try: 
        data = Timer.find_by_user(data['user_id'])
        data.history = editHistoryFunc( data= data.history)
        db.session.commit()
        return True
      
    except Exception as e:
        return False
def get(data,serialize):
    try: 
        data = Timer.find_by_user(data['user_id'])
        if serialize :
            return data.serialize()
        return data
    except Exception as e:
        return None
    
def delete(data):
    try: 
        db.session.delete(Timer.find_by_user(data['user_id']))
        return True
    except Exception as e:
        return False