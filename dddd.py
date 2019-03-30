from Misskey import Misskey
import json, os, sys


misskey = Misskey("misskey.m544.net", apiToken="!wLno8dw52KYCvyn20VUQqRVJKYbiDRKi")

print(misskey)

class CREATE_BOT():
    def __init__(self):
        pass
    def K(self):
        print("one_status")
a = CREATE_BOT()
a.K()



g = "C:/Users/sakuw/OneDrive/デスクトップ/TEST/python_visit"


dirname,basename = os.path.split("")
print(dirname)
print(basename)


from websocket import create_connection

h = "https://misskey.m544.net/?i=!wLno8dw52KYCvyn20VUQqRVJKYbiDRKi"
host_url = h.encode("unicode-escape")

print(host_url)

aaa = create_connection(host_url)
aaa.send(json.dumps({
    "type":"api",
    "id":"cororonnxx",
    "endpoint":"cororonnxx",
    "data": {
        "text":"ok_dash"
    }
}))
