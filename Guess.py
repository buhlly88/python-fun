import random 
import sys
a=random.randint(1,100)
print (a)

def getValue(verbiage):
  return(input(verbiage))

y = 0
count = 0

while a != y:
  count= count+1
  y = getValue('Guess a value? ')

  if a==y:
    print('good job. It took you ' + str(count) + ' tries.')
    if count>=10: print('stoopid')
    elif count>=6: print('a okay')
    elif count>=2: print ('preety smart')
    elif count==1: print('lucky guess fool')
  elif a>y:
    print('too low fool')
  elif a<y:
    print('too high fool')


