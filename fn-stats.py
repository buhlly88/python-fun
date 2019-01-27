import sys
from pprint import pprint
import requests
import json

print(sys.version)

username="spelchekk"

url ="https://api.fortnitetracker.com/v1/profile/pc/" + username
headers = {'TRN-Api-Key': 'e79ac99b-1033-43a8-833a-c2733ace72f6'}


r = requests.get(url, headers=headers)

parsed_json = json.loads(r)

print(parsed_json['accountId'])

