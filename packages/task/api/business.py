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

        return {},'success'
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'

    
def edit(data):
    try: 
        task = Task.find_by_id(id=data['taskId']).first()
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

        return {},'success'
      
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'


def get(data):
    try: 
        tasks = []
        elements = Task.find_by_userId_filtered(data['userId'],dateFrom=data['dateFrom'],dateTo=data['dateTo'],page=data['page'],countOnPage=data['countOnPage'])
        for elenemt in elements:
            tasks.append(elenemt.serialize())
        return {'data':tasks},'success'
    except Exception as e:
        
        print(e)
        return {
            'Error':str(e)
        },'unsuccess'

    
def deleteTask(data):
    try: 
        Task.query.filter_by(id=data['taskId']).delete()
        db.session.commit()
        return {},'success'
      
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'

def createTasks(data):
    try: 
        Task.query.filter_by(id=data['taskId']).delete()
        db.session.commit()
        return {},'success'
      
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'
    
def statCreate(data):
    try: 
        stat = TaskStat(
                userId= data['userId'],
            )
        db.session.add(stat)
        db.session.commit()
        return {},'success'
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'

    
def statInfoTask(data):
    try: 
        return TaskStat.find_by_userId(data['userId']).serialize(),'success'
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'


        
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
            return {},'success'
        return {
            'Error':str(e)
        },'unsuccess'

    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'


def statDelete(data):
    try: 
        TaskStat.query.filter_by(id=data['taskId']).delete()
        return {},'success'
    except Exception as e:
        return {
            'Error':str(e)
        },'unsuccess'

    

        