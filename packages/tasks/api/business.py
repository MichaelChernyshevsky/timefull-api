from ..models.task import Task
from ..models.stat import TaskStat

from config.extensions import db




def add(data):
    try: 
        task = Task(
                userId= data['userId'],
                title = data['title'],
                description = data['description'],
                date = data['date'],
                countOnDay = data['countOnDay'],
                countOnTask = data['countOnTask'],
            )
        db.session.add(task)
        db.session.commit()
        return True
    except Exception as e:
        return False
    
def edit(data):
    try: 
        task = Task.find_by_id(data['taskId'])
        if(task):
            if ( data['title']):
                task.title = data['title']
            if ( data['description']):
                task.description = data['description']
            if ( data['date']):
                task.date = data['date']
            if ( data['countOnDay']):
                task.countOnDay = data['countOnDay']
            if ( data['countOnTask']):
                task.countOnTask = data['countOnTask']
            db.session.commit()
        return True
      
    except Exception as e:
        return False

        
    
def get(data):
    try: 
        tasks = []
        elements = Task.find_by_userId(data['userId'])
        for elenemt in elements:
            tasks.append(elenemt.serialize())
        return tasks
    except Exception as e:
        return False
    

    
def delete(data):
    try: 
        Task.query.filter_by(id=data['taskId']).delete()
        db.session.commit()
        return True
      
    except Exception as e:
        return False
    
def statCreate(data):
    try: 
        stat = TaskStat(
                userId= data['userId'],
            )
        db.session.add(stat)
        db.session.commit()
        return True
    except Exception as e:
        return False
    
def statInfo(data):
    try: 
        return TaskStat.find_by_userId(data['userId']).serialize()
    except Exception as e:
        return False
        
def statEdit(data):
    try: 
        stat = TaskStat.find_by_userId(data['userId'])
        if stat:
           
            if stat.countDone:
                stat.countDone += int(data['countDone'])
            else:
                stat.countDone = int(data['countDone'])
            if stat.countUnDone:
                stat.countUnDone += int(data['countUnDone'])
            else:
                stat.countUnDone = int(data['countUnDone'])
            db.session.commit()
            return True
        return False
    except Exception as e:
        return False

def statDelete(data):
    try: 
        tasks = []
        elements = Task.find_by_userId(data['userId'])
        for elenemt in elements:
            tasks.append(elenemt.serialize())
        Task.query.filter_by(id=data['taskId']).delete()

        return True
    except Exception as e:
        return False
    

        