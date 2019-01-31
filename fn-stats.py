'''
Get a list of usernames 
Call fortnite api with each username
Create HTML template in order to put data retrieved from api call
Save file

Do this:

myList = "spellcheck,ninja"
for i in myList:
	response = callFunctionToAPI(i)
	kills = getKills(response)
	wins = getWins(response)


totalWins=50
totalKills=10

myString = f"""

<tr>
	<td>Name</td>
	<td>Kills</td>
	<td>Wins</td>
</tr>

<tr>
	<td>{username}</td>
	<td>{totalWins}</td>
	<td>{totalKills}</td>
</tr>
"""

print(myString)


'''



import sys
from pprint import pprint
import requests
import json

print(sys.version)

def getStats(username):
    url ="https://api.fortnitetracker.com/v1/profile/pc/" + username
    headers = {'TRN-Api-Key': 'e79ac99b-1033-43a8-833a-c2733ace72f6'}
    
    r = requests.get(url, headers=headers)
    data = r.content.decode("utf-8")
    parsedData = json.loads(data)
    
    print(username)

    stats={}
    stats['Username']=username
    try:
        stats['solokd']=parsedData['stats']['p2']['kd']['value']
    except:
        stats['solokd']=0

    try:
        stats['duokd']=parsedData['stats']['p9']['kd']['value']
    except:
        stats['duokd']=0

    try:
        stats['squadkd']=parsedData['stats']['p10']['kd']['value']
    except:
        stats['squadkd']=0

    try:
        stats['totalwins']=parsedData['lifeTimeStats'][8]['value']
    except:
        stats['totalwins']=0

    try:
        stats['totalkills']=parsedData['lifeTimeStats'][10]['value']
    except:
        stats['totalkills']=0

    return stats

def getHTML(stats):
    myHMTL=f"""
        <tr>
            <td><font color='blue'>{username}</td></font>        
            <td>{stats['solokd']}</td>
            <td>{stats['duokd']}</td>
            <td>{stats['squadkd']}</td>
            <td>{stats['totalkills']}</td>
            <td>{stats['totalwins']}</td>
        </tr>"""        

    return myHMTL



#Define variables
usernames=['v7_fatigue','UNIcorn-XD','thecurryboy','Sad Pika','Obamayang420','extrabaconplz','MilkyBiscuits YT','Spelchekk','Ninja','HighDistortion','Lilsquad_YT','MaxMoomin']
uesrnames=usernames.sort(key=str.lower) 
topSection = '''
<!doctype html>
<html>
  <head>
    <title>Fortnite stats</title>
    <meta name="description" content="Fortnite stats">
    <meta name="keywords" content="fortnite stats">
  </head>

  <body>
    <p>This is a table show fortnite stats</p>
    <table border="1" width="75%">
      <tr>
        <td><b><font color="red">Name</b></td></font>
        <td><b><font color='red'>Solo KD</b></td></font>
        <td><b><font color='red'>Duo KD</b></td></font>
        <td><b><font color='red'>Squad KD</b></td></font>
        <td><b><font color='red'>Total Kills</b></td></font>
        <td><b><font color='red'>Total Wins</b></td></font>
      </tr>
'''

bottomSection='''
    </table>
  </body>
</html>
'''

middleSection = ''


for username in usernames:
    currentStat=getStats(username)
    myHTML = getHTML(currentStat)
    middleSection = middleSection + myHTML 


#put the piece together
myPage = topSection + middleSection + bottomSection


f = open("fn-stats.html", "w")
f.write(myPage)


#pprint(myBigVariable)
#print(s.get('solokd'))
#sys.exit()


#print(r.content.decode("utf-8"))
#sys.exit('bam')


#print(parsed_json['accountId'])


























