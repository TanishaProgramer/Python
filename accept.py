str = input("enter any string")

vowels =['a','e','i','o','u']

result = True

for i in vowels:
    if i in str:
        continue
    else:
        result=False
        break

if result == False:
    print("string not accepted")
if result == True:
    print("string accepted")