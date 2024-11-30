from config.extensions import db
from ..model.packages import Packages



def inection(userId):
    packages = Packages.find_by_user(userId)
    if packages.timer == None:
        packages.timer = False
    if packages.tasks == None:
        packages.tasks = False
    if packages.economy == None:
        packages.economy = False
    if packages.sport == None:
        packages.sport = False
    if packages.note == None:
        packages.note = False
    if packages.team == None:
        packages.team = False
    db.session.commit()
    