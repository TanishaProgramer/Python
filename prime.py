# prime number is a number 
# which can only be divided by 1 and self
#for ex:- 2 2 can only divided by 2 and 1 
# also 3, 5 and 7 etc.

num = int(input("Enter any number"))

isprime = True
if num==1:
    print("number is prime")

       ## because every number can be divided by one and n so we will check wheather it is divisible by 2 to n-1 or not

else:
    for i in range(2,num-1): 
        if num%2==0:
            isprime=False
            break
if isprime==True:
    print("number is  prime")
else:
    print("number is not Prime")