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
            case 'team':
                return packages.team,'success'
            case 'economy':
                return packages.economy,'success'
            case 'note':
                return packages.note,'success'
            case 'sport':
                return packages.sport,'success'
        return False,'error name'
    except Exception as e:
        return False,'Error is:' +str(e)
    

        
    



        