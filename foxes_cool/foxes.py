import time
import math
from datetime import datetime
import requests
import random

times = {}

def __internal(tag, argument):
    day = math.floor(int(time.mktime(datetime.utcnow().timetuple()))/86400)
    if times.get(tag, {}).get("time", 0) != day:
        times[tag] = {
            "time":day,
            "count": int(requests.get("https://foxes.cool/counts/"+tag).content),
        }
    urlParams = []
    for key in argument:
        urlParams.append(key+"="+str(argument[key]))
    urlParamsString = ""
    if len(urlParams) > 0:
        urlParamsString = "?" + "&".join(urlParams)
    return "https://img.foxes.cool/"+tag+"/"+str(random.randint(0, times[tag]["count"]))+".jpg"+urlParamsString


def fox(argument):
    return __internal("fox", argument)

def curious(argument):
    return __internal("curious", argument)

def happy(argument):
    return __internal("happy", argument)

def scary(argument):
    return __internal("scary", argument)

def sleeping(argument):
    return __internal("sleeping", argument)
