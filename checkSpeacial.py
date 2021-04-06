str = input("Enter your full name")

special_char = input("Enter the special character")

result = special_char in str

if result == True:
    print("charcter is present in the string")

else:
    print("character is not present in the string")