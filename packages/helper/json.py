import json

def fromStringToJson(data):
    return json.loads(data)

def fromJsonToString(data):
    return json.dumps(data)
