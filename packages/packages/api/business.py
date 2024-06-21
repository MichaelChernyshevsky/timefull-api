from config.extensions import db
from ..model.packages import Packages

def add(data):
    try: 
        packages = Packages.find_by_user(data['userId'])
        db.session.commit()
        return True


    except Exception as e:
        return False

        
    

def get(data):
    try: 
        package = Packages.find_by_user(data['userId'])
        return package.serialize()
    except Exception as e:
        return False

        
    
def delete(data):
    try: 
        packages = Packages.find_by_user(data['userId'])
        
        pass
    except Exception as e:
        return False

        