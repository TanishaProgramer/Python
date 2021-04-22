## Sign Up : 
## name , number , email , password .

## login
## email , password.

## dictionary - to store a single user data.
## list - to store multiple user's data in a single list.

import os

data = {}
users = []

# this function will clear the screen 
def clearScreen():
    clear = lambda:os.system('cls')
    clear()

# this function will create a new Student and add in list
def signUpStudent():
    data['name'] = input("ENTER NAME : ")
    data['phone'] = int(input("ENTER PHONE NUMBER : "))
    data['email'] = input("ENTER EMAIL ADDRESS :")
    data['password'] = input("ENTER PASSWORD : ")

    userName = len(users)
    users.append(data)
    print("SIGNUP SUCCESS....","\nYour User Name is : ",userName)   
    input("ENTER TO CONTINUE.......")
    clearScreen()

## this function will login the student.
def loginStudent():

    if len(users) == 0:
        print("NO USERS..")
        pass
    else:
        username = int(input("ENTER THE USERNAME : "))
        password = ""

        if username < len(users) and username >= 0 :
            data = users[username]
            password = input("ENTER YOUR PASSWORD.")

            if password == data['password']:
                print("Login Success....")
                print("welcome ", data['name'] , "username :",username)
            else:
                print("INVALID PASSWORD...")
        else:
            print("INVALID USERNAME...")
    
    input("\nENTER TO CONTINUE...")
    clearScreen()

def main():
    while True:
        clearScreen()
        print("-------- STUDENT LOGIN PORTAL --------")
        print("1. ADD NEW STUDENT")
        print("2. LOGIN WITH DETAILS")
        print("3. EXIT")

        choice = int(input("ENTER YOUR CHOICE : "))

        if choice == 1:
            signUpStudent()
        elif choice == 2:
            loginStudent()
        elif choice == 3:
            exit(0)
        else:
            print("BAD TRY....")

if __name__ == '__main__':
    ## starting of Execution of the program..
    main()
