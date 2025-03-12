from ..models.team import TeamModel
from config.extensions import db



def getActive(userId):
    userTeams = []
    teams = TeamModel.find_by_user(userOwnerId=userId)
    for team in teams:
        if(team.isActive):
            
            
            userTeams.append(team)
    return userTeams

def getNotActive(userId):
    userTeams = []
    teams = TeamModel.find_by_user(userOwnerId=userId)
    for team in teams:
        if(team.isActive != True ):
            userTeams.append(team)
    return userTeams