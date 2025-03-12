# user
from modules.user.models.user import User
from modules.user.models.info import Info
from modules.user.models.stat import Stat
# economy
from modules.economy.models.economy import Economy
# timer
from modules.timer.models.timer import Timer
# task 
from modules.task.models.task import Task
from modules.task.models.stat import TaskStat
# packages
from modules.packages.model.packages import Packages


def info(data):
    try: 
        users = User.query.all()
        info = Info.query.all()
        stat = Stat.query.all()
        packages = Packages.query.all()
        task = Task.query.all()
        taskStat = TaskStat.query.all()
        economy = Economy.query.all()
        timer = Timer.query.all()
        return {
            "user" : {
                "users": len(users),
                "info": len(info),
                "stat": len(stat),
            },
            "economy": {
                "economy": len(economy)
            },
             "timer": {
                "timer" : len(timer)
            },
             "task": {
                "task": len(task),
                "stat": len(taskStat)
            },
           
        },'success'
    except Exception as e:
        return {} , "unsuccess"
    

    
def wipe(data):
    try:
        def user():
            pass
        def economy():
            pass
        def timer():
            pass
        def task():
            pass
        def packages():
            pass
        if (data['user']):
            user()
            packages()
        if (data['economy']):
            economy()
        if (data['timer']):
            timer()
        if (data['task']):
            task()
        if (data['all']):
            user()
            packages()
            economy()
            timer()
            task()
        return {} , "success"

    except Exception as e:
        return {} , "unsuccess"