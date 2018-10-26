from random import  randrange
r = randrange(100)
u = int(input("podaj liczbe od 1 do 100"))

while(r!=u):
    if(u>r):
        print("za duzo")
    else:
        print("za malo")
    i = input("sprobuj")
    if(i=="q"):
        break
    u = int(i)            
if(r==u):            
    print("zgadles")
