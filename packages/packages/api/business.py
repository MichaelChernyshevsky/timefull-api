from config.extensions import db
from ..model.packages import Packages


def checkPakage(package,userId):
    try: 
        packages = Packages.find_by_user(userId)
        match package:
            case 'timer':
                return packages.timer,'success'
            case 'task':
                return packages.task,'success'
            case 'economy':
                return packages.economy,'success'
        return False,'error name'
    except Exception as e:
        return False,'error'
    
def changeState(data):
    try: 
        packages = Packages.find_by_user(data['userId'])
        match data['package']:
            case 'timer':
                if (packages.timer):
                    from packages.timer.api.business import deleteTimer
                    deleteTimer(data)
                else:
                    from packages.timer.api.business import createTimer
                    createTimer(data)
                packages.timer = not packages.timer 
            case 'task':
                if (packages.task):
                    from packages.task.api.business import deleteTask
                    deleteTask(data)
                packages.task = not packages.task 
            case 'economy':
                if (packages.economy):
                    from packages.economy.api.business import deleteEconomy
                    deleteEconomy(data)
                packages.economy = not packages.economy 
        print(3)

        db.session.commit()
        return {},'success'


    except Exception as e:
        
        return {
            'error':e
        },'unsuccess'

        
    

def get(data):
    try:
        package = Packages.find_by_user(data['userId'])
        return package.serialize(),'success'
    except Exception as e:
        return {},'unsuccess'

        
    

        