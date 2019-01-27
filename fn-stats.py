import sys
from pprint import pprint
import requests
import json

print(sys.version)

username="spelchekk"

url ="https://api.fortnitetracker.com/v1/profile/pc/" + username
headers = {'TRN-Api-Key': 'e79ac99b-1033-43a8-833a-c2733ace72f6'}


r = requests.get(url, headers=headers)
data = r.content.decode("utf-8")

#print(r.content.decode("utf-8"))
#sys.exit('bam')

parsedData = json.loads(data)

kdP2=parsedData['stats']['p2']['kd']['value']
kdP9=parsedData['stats']['p9']['kd']['value']
kdP10=parsedData['stats']['p10']['kd']['value']
totalWins=parsedData['lifeTimeStats'][8]['value']
totalKills=parsedData['lifeTimeStats'][10]['value']


print(kdP2)
print(kdP9)
print(kdP10)
print(totalWins)
print(totalKills)

#print(parsed_json['accountId'])

