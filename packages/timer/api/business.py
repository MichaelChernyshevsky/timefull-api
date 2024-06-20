from config.extensions import db
from ..models.timer import Timer
from ..func.json import *

def contain(data):
    return  Timer.find_by_user(data['userId']) != None 

def create(data):
    try:
            data = Timer(
                userId = data['userId'],
                history = emptyHistory(),
                stat = emptyStat()
            )
            db.session.add(data)
            db.session.commit()

            return True
    except Exception as e:
        return False

        
    
def editStat(data):
    try: 
        if contain(data) == False:
            create(data)
        timer = Timer.find_by_user(data['userId'])
        timer.stat = editStatFunc(data=timer.stat,timeWork=data['timeWork'],timeRelax=data['timeRelax'])
        db.session.commit()
        return True
      
    except Exception as e:
        return False

        
    
def editHistory(data):
    try: 
        if contain(data) == False:
            create(data)
        timer = Timer.find_by_user(data['userId'])
        timer.history = editHistoryFunc(data=timer.history,work=data['work'],relax=data['relax'])
        db.session.commit()
        return True
      
    except Exception as e:
        return False

        
def get(data,serialize):
    try: 
        if contain(data) == False:
            create(data)
        data = Timer.find_by_user(data['userId'])
        if serialize :
            return data.serialize()
        return data
    except Exception as e:
        return False
    
def delete(data):
    try: 
        if contain(data) == False:
            return True
        db.session.delete(Timer.find_by_user(data['userId']))
        db.session.commit()

        return True
    except Exception as e:
        return False

        