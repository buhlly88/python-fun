import time 
import sys

print(sys.version)

startT = time.time()
for x in range(1,25):
	#print(x)
	sys.stdout.write(str(x))
	time.sleep(.001)

stopT = time.time()

print('')
total = stopT-startT
print (total)

print('===============')


kills=50
wins=10

myString = f"""
this is a 
multiline string and kills is {kills}
and wins is {wins}"""

print(myString)
