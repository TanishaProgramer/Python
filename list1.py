list = ["chirag",2,3,4.5,"juneja"]
newlist =[]

for i in list:
    if isinstance(i,str):
        newlist.append(i)

print(newlist)