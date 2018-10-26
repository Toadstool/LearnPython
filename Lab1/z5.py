import math
from random import  randrange
list  = range(2,40,1)



def calProb(groupCount):
    counts = 0
    simulation =100000
    for x in range(simulation):
        list = [randrange(365) for n in range(1,groupCount)]        
        if(len(list)!=len(set(list))):            
            counts+=1        
    return counts/simulation
    
    

for x in list:
    prop = 1-math.factorial(365)/math.factorial(365-x)/365**x
    print("{0} :{1}".format(x,prop),calProb(x))
