from ...helper.json import *


def emptyHistory():
    return '{"work":0,"relax":0}'

def emptyStat():
    return '{"timeWork":0,"timeStat":0}'

def editStatFunc(data,timeWork,timeRelax):
    json = fromStringToJson(data=data)
    json["timeWork"] += int(timeWork)
    json["timeStat"] += int(timeRelax)
    return fromJsonToString(json)

def editHistoryFunc(data,work,relax):
    json = fromStringToJson(data=data)
    json['work'] +=  int(work)
    json['relax'] += int(relax)
    return fromJsonToString(json)
