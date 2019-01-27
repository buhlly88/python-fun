'''


for i in range(2,10):
  prime = 1
  for j in range(2,i):
    #print('i:%s j:%s' % (i,j))
    if i>1 and i!=j and i%j==0:
      #print('not prime %s' % i) 
      prime = 0
      break
  if prime == 1:
    print(i)
'''

''' 
1%1

2%1 0
2%2 0

3%1 0
3%2 1
3%3 0

4%1 0
4%2 0
4%3 1
4%4 0
'''


for i in reversed(range(2,10000000)):
  prime = 1
  for j in range(2,i):
    #print('i:%s j:%s' % (i,j))
    if i>1 and i!=j and i%j==0:
      #print('not prime %s' % i) 
      prime = 0
      break
  if prime == 1:
    print(i)
    break