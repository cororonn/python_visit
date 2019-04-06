import requests
import json
import pprint
import hashlib
from Misskey import Misskey
from websocket import create_connection

api_Token="!wLno8dw52KYCvyn20VUQqRVJKYbiDRKi"
app_secret = "NxM8T3Oyl6KhUImauM9ndQhp7klPixAR"

h = "https://misskey.m544.net/api/auth/session/generate?i=NxM8T3Oyl6KhUImauM9ndQhp7klPixAR"

item_data = {
    "appsecret":"NxM8T3Oyl6KhUImauM9ndQhp7klPixAR",
    "Content-Type": "/auth/session/generate"

}


r_post = requests.post(h,json=item_data)

print(r_post.status_code)
print(r_post)

j = hashlib.sha256(api_Token.encode()).hexdigest()
l = hashlib.sha256(app_secret.encode()).hexdigest()
i = j+l

misskey = Misskey("misskey.m544.net", apiToken="!wLno8dw52KYCvyn20VUQqRVJKYbiDRKi")

h = "https://misskey.m544.net/api/auth/session/generate/?i=NxM8T3Oyl6KhUImauM9ndQhp7klPixAR"
host_url = h.encode("unicode-escape")

print(host_url)