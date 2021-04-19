# def printData(name , degree , passingYear , numberStudents , numberExams):
#     print("NAME : ",name)
#     print("DEGREE : ",degree)
#     print("PASSING YEAR : ",passingYear)
#     print("NUMBER OF STUDENTS : ",numberStudents)
#     print("NUMBER OF EXAMS : ",numberExams)
 
# ## calling the function :
# name = input("ENTER USER NAME ")
# degree = input("ENTER DEGREE NAME ")
# passingYear  = input("ENTER PASSING YEAR ")
# numberStudents = input("ENTER NUMBER OF STUDENTS ")
# numberExams = input("ENTER NUMBER OF EXAMS ")

# printData(name , degree , passingYear , numberStudents , numberExams)


## there are two types of functions :

## syntax to create a function

## dynamic..
students = {1:"Chirag" , 2:"Jitesh" , 3:"Tanisha" ,4:"Riya" , 5:"manish"}

def getStudentName(key):
    result = students[key] 
    return result

def addNewStudent():
    name = input("please enter your name")
    numKey = len(students)
    key= numKey+1
    students[key] = str(name)
    return key

def start():
    while True:
        print("1. Add new Student")     
        print("2. get Student Data")
        print("3. EXIT...")
        d = int(input("please enter your choice..."))

        if d == 1:
            addNewStudent()
        elif d == 2:
            key = int(input("please enter a key"))
            if key<=len(students) and key>0:
                print(getStudentName(key))  
            else:
                print(" please enter valid key....")
        elif d==3:
            break
        else:
            print("invalid choice...")
            break

# start()

# def reverseArray(a):
#     size = len(a)
#     result = []
#     for i in range(0,size):
#         result.append(a[ size-i-1 ])
#     return result

a = [1,2,3,4]

print(a[::-1])


