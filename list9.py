# def func(a=0,b=0,c=0,d=0):
#     print(a,b,c,d)

# mylist=[1,2,4,5]

# func(*mylist)

# print(*mylist)
# print(mylist)

def func(*mytuple):
    sum=0
    for i in mytuple:
        sum=sum+i

    return sum

print(func(1,2,3,4,5))  ## 1+2+3+4+5=15
print(func(1,2,5,6,7,8,9)) ## 38

mynewtuple = 1,2,4,4,5,6

# mynewtuple=list(mynewtuple)

print(mynewtuple)



