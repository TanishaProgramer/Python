stack=[]
while True:
    print("stack:")
    print("1. add")
    print("2. pop")
    print("3. traverse")
    print("4. Exit..")

    choice = int(input("enter your choice"))
    if(choice==1):
        num = input("enter number")
        stack.append(num)
    if(choice==2):
        stack.pop()
    if(choice==3):
        for i in stack:
            print(i)
    if(choice==4): 
        break