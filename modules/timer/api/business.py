from config.extensions import db
from ..models.timer import Timer
from ..func.json import *
from  ...tools.helper.json import *


        
    
def update(data):
    try: 
        timer = Timer.find_by_user(data['userId'])
        timer.stat = json.dumps({
            'timeRelax': int(data['stat']['timeRelax']),
            'timeWork': int(data['stat']['timeWork'])
        })
        timer.history =json.dumps( {
            'work': int(data['history']['work']),
            'relax': int(data['history']['relax'])
        })
        

        db.session.commit()
        return {},'success'
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'

        
        
def get(data):
    try: 
        return Timer.find_by_user(data['userId']).serialize(),'success'
    except Exception as e:
       
        return {
            'Error':str(e)
        },'unsuccess'
    
def statInfoTimer(data):
    try: 
        return fromStringToJson(Timer.find_by_user(data['userId']).history),'success'
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'

    
    
def deleteTimer(data):
    try: 
        db.session.delete(Timer.find_by_user(data['userId']))
        db.session.commit()
        return True
    except Exception as e:
        return False

        
def createTimer(data):
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
