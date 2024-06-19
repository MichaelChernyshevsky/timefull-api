import json

def fromStringToJson(data):
    return json.loads(data)

def fromJsonToString(data):
    return json.loads(data)

def emptyHistory():
    return '{"work":0,"relax":0}'

def emptyStat():
    return '{"timeWork":0,"timeStat":0}'

def editStatFunc(data,timeWork,timeStat):
    json = fromStringToJson(data=data)
    json["timeWork"] += timeWork
    json["timeStat"] += timeStat

    return fromJsonToString(json)

def editHistoryFunc(data,work,relax):
    json = fromStringToJson(data=data)
    json["work"] += work
    json["relax"] += relax
    return fromJsonToString(json)
