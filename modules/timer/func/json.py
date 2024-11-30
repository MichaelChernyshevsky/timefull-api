from  ...tools.helper.json import *


def emptyHistory():
    return '{"work":0,"relax":0}'

def emptyStat():
    return '{"timeWork":0,"timeRelax":0}'

def editStatFunc(data,timeWork,timeRelax):
    json = fromStringToJson(data=data)
    if (timeWork):
        json["timeWork"] += int(timeWork)
    if(timeRelax):
        json["timeRelax"] += int(timeRelax)

    return fromJsonToString(json)

def editHistoryFunc(data,work,relax):
    json = fromStringToJson(data=data)
    json['work'] +=  int(work)
    json['relax'] += int(relax)
    return fromJsonToString(json)
