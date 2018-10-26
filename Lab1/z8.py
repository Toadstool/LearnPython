import random

data = []

for i in range(1,5): 
    data.append(random.randint(1,6))

print(data)
tryCount = 10
while(tryCount>0):
    tryCount = tryCount-1
    userData = input("Provide 4 number")
    if userData == "q":
        break
    output = "" 
    for i in range(0,4):
        print(userData[i])
        if int(userData[i])== data[i]:
            output = output +"2"
        elif int(userData[i]) in data:
            output = output +"1"
        else:
            output = output +"0"                
    if output== "2222":
        print("Win")
    else:
        print(output)
