mystr = input("Enter any string")

if len(mystr) < 5:
    print("null")
else:
    for i in range(0,5):
        print(mystr[i],end="")