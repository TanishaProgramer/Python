k =int(input("Enter value of k"))

str1 = "Tanisha khandelwal is a good girl"

if k < 0 :
    print("Please enter value of k greater than -1")
else:
    str2 = str1.split(' ')
    for i in str2:
        if len(i)>k:
            print(i)
            

