
#taking number input and casting it to the integer and assigning in the variable 'number'.
number = int(input("Enter Any number"))

fact =1

if number==1 or number==0:
    fact=1
else:
    for i in range(1,number+1):
        fact=fact*i


print(fact)

