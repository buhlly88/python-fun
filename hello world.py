
#print('hello world')
myList = ['John', 'Lena' , 'Alex', 'Simon', 'Anna']
#print(myList[3])
myList.append('buhl')
#print(myList)
myList.pop(3)
#print(myList)

myVar = "jOhn"

if myList[3] == 'Bogus': 
  print('no go senor')
  print ('continuation line')
elif myList[2]=='Lena':
  print('ok')
elif myList[0].lower()== myVar.lower():
  print('john cena')



#else: 
 # print('this is the third item: ' + myList[2])

for i in range(0,4):
  print(myList[i])
  print('some string %s' % i)

coins= 5
for week in range(1,5):
  coins = coins + 10
  print('week %s = %s' % (week,coins))

step = 0
x = ''
while step < 1000:
  x = x + str(step)
  step = step + 1

print(x)

x=10
i =10
while i>1:
  x=x*(i-1)
  i=i-1
print(x)