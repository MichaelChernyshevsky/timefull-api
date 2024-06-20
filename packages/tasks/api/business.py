from ..models.task import Task
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
        