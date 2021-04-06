# from random import shuffle
# li = [3,6,7,8]
# shuffle(li)
# print (li)

import random as r
list1=[1,2,3,4,5,6,7]

# with this code we can choose random number from list
# i = r.choice(list1)

list2=[]
for i in range(1,len(list1)+1):
    i = r.choice(list1)
    list2.append(i)
    list1.remove(i)

print(list2)





