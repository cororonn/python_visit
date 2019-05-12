import pprint
import json
import requests

def main():
    response = requests.post(
        'https://misskey.m544.net/api/auth/session/generate',
        json.dumps({'appsecret':'NxM8T3Oyl6KhUImauM9ndQhp7klPixAR'}),
        headers={'Content-Type': 'application/json'})

    print(response)
    print(response.json())


if __name__=='__main__':
    main()