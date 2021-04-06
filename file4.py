studet_data ={"name":"","class":"","roll_number":""}

## now we will read the input from user

studet_data["name"] = input("Enter name:")
studet_data["class"] = input("Enter class:")
studet_data["roll_number"]=input("enter roll number:")

print("student data:\n",studet_data)

#now we will open file

studet_file = open("student_data.txt","a+")
## now to write student data in file we need to open file in append(a+) mode


studet_file.write("-----------------------------------\n")
## it will written for making file readable

studet_file.write("name:"+studet_data["name"]+"\n") 
## this will  write name of student in file

studet_file.write("class:"+studet_data["class"]+"\n") 
## this will write class of student

studet_file.write("roll number:"+studet_data["roll_number"]+"\n")
 ## this will write roll number of student in file

studet_file.write("-----------------------------------\n")
## it will written for making file readable

studet_file.close()
## closing the file

studet_file=open("student_data.txt","r")
## now to read file we need to open it in reading mode

data =studet_file.read()
# reading file 

print(data)
##printing the file data