from config.extensions import db
from ..model.packages import Packages

def add(data):
    try: 
        packages = Packages.find_by_user(data['user_id'])
        db.session.commit()
        return True


    except Exception as e:
        return False
    

def get(data):
    try: 
        print(data['user_id'])

        package = Packages.find_by_user(data['user_id'])
        print(package)
        return package.serialize()
    except Exception as e:
        return False
    
def delete(data):
    try: 
        packages = Packages.find_by_user(data['user_id'])
        
        pass
    except Exception as e:
        return False