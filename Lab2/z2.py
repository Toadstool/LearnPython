import random

def losuj(a,b):
   bemben = []
   for i in range(1,a+1):
      bemben.append(i)
         
   for i in range(1,a-b):
      bemben.pop(random.randint(0,len(bemben)-1))
      
   return bemben


moje = losuj(20,6)
count = 0
while set(moje) != set(losuj(20,6)):
   count = count+1
   
print(count)
   
