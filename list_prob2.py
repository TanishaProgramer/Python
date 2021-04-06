list1=[1,2,3,4,56,78,90,23,35,65,74,42,31,89,0,-43]

largest = list1[0]

for i in range(0,len(list1)):
    if list1[i] > largest:
        largest=list1[i]

print(largest)

## largest = 1
## 2
## 3
## 4
## 56
## 78
## 90
## 90
## 90
## 90
## 90
## 90
## 90

list1.remove(largest)

print(list1)

largest = list1[0]

for i in range(0,len(list1)):
    if list1[i] > largest:
        largest=list1[i]

print(largest)
