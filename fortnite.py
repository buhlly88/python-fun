import sys
from pprint import pprint

print(sys.version)

from fortnite_python import Fortnite

fortnite = Fortnite('e79ac99b-1033-43a8-833a-c2733ace72f6')
player = fortnite.player('spelchekk')
stats = player.get_stats()

print(player.id)
#pprint(vars(stats))

