# from math import sqrt 


def perfect(max):
    a = 1
    while(a<=max):
        sum = 0

        for i in range(1,int(a/2)+1):        
            if(a%i==0):
                sum+=i                
        if(sum==a):
            print("Perfect: %s" % (a) )  
        a=a+1

def frend(max):
    dividers = {}
    for a in range(1,max):
        sum = 0
        for j in range(1,int(a/2)+1):        
            if(a%j==0):
                sum+=j
        if sum >0:                
            if a in dividers and dividers[a]== sum:
                print("Frends: %s %s" % (dividers[a],a))
            else:
                dividers[sum] = a  


perfect(10000)
frend(10000)
        
    
