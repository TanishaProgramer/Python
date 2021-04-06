

mystr = input("Enter any string")
newmystr = mystr.split(' ')
name_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for j in newmystr:
    for i in j:
        index = name_char.index(i)
        count[index]+=1

percentage =[]

total_length = 0

for i in range(0,len(newmystr)):
    total_length = total_length+len(newmystr[i])


total=0
for i in count:
    per = (i/total_length)*100
    percentage.append(per)
    total=total+per


print("percentage of occuring of every character in given string")
for i in range(0,26):
    print(name_char[i]," :" ,percentage[i],"%")
    

print(total)