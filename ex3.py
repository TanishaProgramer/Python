def pattern1(number):

    for i in range(1,number+1):
        for j in range(1,i+1):
            print("*",end="")
        print()

def pattern2(number):
    for i in range(number,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print()

num_rows = int(input("enter number of rows"))

type_pattern = int(input("type 0 or 1"))
if type_pattern != 0 and type_pattern != 1:
    print("please enter valid input")
else:
    if type_pattern == 0:
        pattern1(num_rows)
    
    if type_pattern ==1:
        pattern2(num_rows)