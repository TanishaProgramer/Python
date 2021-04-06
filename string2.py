'''
write a python program to print string characters to dictionary
where character is the key and number of percentage is the value
'''



mystr = input("Enter any string")

#now we will convert the string to list where list contains word in string seprated by spaces
# chirag is a good boy
# list contains--->>> ["chirag","is","good","boy"]

newmystr = mystr.split(' ')
print(newmystr)

name_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for j in newmystr:
    for i in j:
        index = name_char.index(i)
        count[index]+=1

percentage ={}


total_length = 0

for i in range(0,len(newmystr)):
    total_length = total_length+len(newmystr[i])

total=0

print(count)
k=0
for i in count:
    per = (i/total_length)*100
    percentage[name_char[k]] = per
    k+=1
    total=total+per

print(percentage)
print("percentage of occuring of every character in given string")
for i in percentage:
    print(i," :",percentage[i],"%")
    

print(total)

