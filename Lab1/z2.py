import math
import cmath

a = float(input("a "))
b = float(input("b "))
c = float(input("c "))
delta = b*b-4*a*c

if(delta >0):
    print((-b+sqrt(delta))/(2*a))
    print((-b-sqrt(delta))/(2*a))
elif (delta ==0):
    print((-b)/(2*a))
else:
    print("complex !!!!")
    print((-b+cmath.sqrt(delta))/(2*a))
    print((-b-cmath.sqrt(delta))/(2*a))
    
    


    
