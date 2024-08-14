from config.extensions import db
from ..model.packages import Packages


def checkPackage(package,userId):
    try: 

        packages = Packages.find_by_user(userId)
        match package:
            case 'timer':
                return packages.timer,'success'
            case 'task':
                return packages.tasks,'success'
            case 'economy':
                return packages.economy,'success'
            case 'note':
                return packages.note,'success'
            case 'sport':
                return packages.sport,'success'
        return False,'error name'
    except Exception as e:
        return False,'Error is:' +str(e)
    
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
            case 'sport':
                # if (packages.sport):
                    # from packages.economy.api.business import deleteEconomy
                    # # deleteEconomy(data)
                packages.sport = not packages.sport 
            case 'note':
                # if (packages.economy):
                #     from packages.economy.api.business import deleteEconomy
                #     # deleteEconomy(data)
                packages.note = not packages.note 
        db.session.commit()
        return {},'success'


    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'

        
    

def get(data):
    try:
        package = Packages.find_by_user(data['userId'])
        return package.serialize(),'success'
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'

        
    

        