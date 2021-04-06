num1 = float(input("enter first number"))
num2 = float(input("enter second number"))

print("1 for addition")
print("2 for substraction")
print("3 for multiplication")
print("4 for divison")

choice = int(input("enter your choice"))

if choice==1:
    print("addtion:" , num1 + num2)

elif choice == 2:
       print("substration :" , num1 - num2)

elif choice == 3:
    print("multipilcation :" , num1 * num2)

elif choice == 4:
    print("divison :" , num1 / num2)

else:
    print("enter right option pkease")

print(".........")