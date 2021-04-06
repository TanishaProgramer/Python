str = input("enter a string")

str = str.split(' ')
print(type(str))
for i in str:
    if len(i)%2==0:
        print(i)
    else:
        continue