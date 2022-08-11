import json

def dumpIt(obj):
    return json.dumps(obj,indent=4,sort_keys=True,default=str)