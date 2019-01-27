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