data =input("podaj list")
list = eval(data)
print(list)
for item in list:
    name = item.split(" ")[0]
    surname = item.split(" ")[1]
    print(name[0:3]+surname[0:2]+"@student.agh.edu.pl")

