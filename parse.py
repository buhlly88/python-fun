import sys
import requests
import json
from pprint import pprint

print(sys.version)

with open('stats.json') as f:
    data = json.load(f)

print("Duo Kills: " + str(data['stats']['kills_duo']))
print("=================")
pprint(data)


#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(myFile)
#print(str(myFile))