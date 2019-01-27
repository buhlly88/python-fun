import random

i=0
a=0
x=0
y=0
z=1
b=300
while True: 
  if x==y==z==a:
    break
  x=random.randint(1,b)
  y=random.randint(1,b)
  z=random.randint(1,b)
  a=random.randint(1,b)
  #print(str(x)+str(y)+str(z)+str(a))
  i=i+1
print('ittook ' + "{:,}".format(i) )  




