list1=[1,2,3,4,5,6,7,8,9,0,11,13,15,18,20]

search_element = int(input("Enter number to be searched"))

if search_element in list1:
    index = list1.index(search_element)
    print("number found at:",index)
    

    newlist=[]
    for i in range(index+1,len(list1)):
        newlist.append(list1[i])

    print("the next n element are:")
    for i in newlist:
        print(i)    
else:
    print("number not found")
