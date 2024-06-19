import json

def fromStringToJson(data):
    return json.loads(data)

def fromJsonToString(data):
    return json.dumps(data)

def emptyHistory():
    return '{"work":0,"relax":0}'

def emptyStat():
    return '{"timeWork":0,"timeStat":0}'

def editStatFunc(data,timeWork,timeRelax):
    print(data)
    json = fromStringToJson(data=data)
    print(json)
    json["timeWork"] += int(timeWork)
    print(json)
    
    json["timeStat"] += int(timeRelax)
    print(json)

    return fromJsonToString(json)

def editHistoryFunc(data,work,relax):
    json = fromStringToJson(data=data)
    json['work'] +=  int(work)
    json['relax'] += int(relax)
    return fromJsonToString(json)
