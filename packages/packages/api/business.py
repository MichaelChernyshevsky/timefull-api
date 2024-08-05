from config.extensions import db
from ..model.packages import Packages


def checkPackage(package,userId):
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
        print(e)
        return False,'error'
    
def changeState(data):
    try: 
        packages = Packages.find_by_user(data['userId'])
        match data['package']:
            case 'timer':
                if (packages.timer):
                    from packages.timer.api.business import deleteTimer
                    # deleteTimer(data)
                else:
                    from packages.timer.api.business import createTimer
                    createTimer(data)
                packages.timer = not packages.timer 
            case 'task':
                if (packages.tasks):
                    from packages.task.api.business import deleteTask
                    # deleteTask(data)
                packages.tasks = not packages.tasks
            case 'economy':
                if (packages.economy):
                    from packages.economy.api.business import deleteEconomy
                    # deleteEconomy(data)
                packages.economy = not packages.economy 
        db.session.commit()
        return {},'success'


    except Exception as e:
        print(1)
        print(e)
        return {
            'error':e
        },'unsuccess'

        
    

def get(data):
    try:
        print(1)

        package = Packages.find_by_user(data['userId'])
        print(1)

        return package.serialize(),'success'
    except Exception as e:
        print(e)
        return {},'unsuccess'

        
    

        