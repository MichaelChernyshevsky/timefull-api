from config.extensions import db
from ..models.timer import Timer
from ..func.json import *
from ...helper.json import *

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
        timer = Timer.find_by_user(data['userId'])
        timer.stat = editStatFunc(data=timer.stat,timeWork=data['timeWork'],timeRelax=data['timeRelax'])
        db.session.commit()
        return True
      
    except Exception as e:
        return False

        
    
def editHistory(data):
    try: 
        timer = Timer.find_by_user(data['userId'])
        timer.history = editHistoryFunc(data=timer.history,work=data['work'],relax=data['relax'])
        db.session.commit()
        return True
      
    except Exception as e:
        return False

        
def get(data):
    try: 
        return Timer.find_by_user(data['userId']).serialize()
    except Exception as e:
        return False
    
def statInfoTimer(data):
    try: 
        return fromStringToJson(Timer.find_by_user(data['userId']).history)
    except Exception as e:
        return False

    
    
def delete(data):
    try: 
        db.session.delete(Timer.find_by_user(data['userId']))
        db.session.commit()
        return True
    except Exception as e:
        return False

        