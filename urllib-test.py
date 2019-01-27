import urllib.request
with urllib.request.urlopen('https://packagecontrol.io/channel_v3.json') as response:
   html = response.read()
   print(html)
