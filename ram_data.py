def open_and_read(filename):

    f= open(filename,"r")
    content = f.read()

    print("\n\n\ncontent of file:\n",content)

    f.close()

def open_and_append(filename,data):
    f=open(filename,"a+")

    f.write(data+" ")
    f.close()

def manipulate_data(dictionary):

    list_data=[]

    for i in dictionary:
        string = i+":"+str(dictionary[i])
        list_data.append(string)

    return list_data


dictionary={}
key = input("enter the name of the value ")

value = input("Enter the value")

dictionary[key]=value

data = manipulate_data(dictionary)

for  i in data:
    string = i
    open_and_append("ramdata.txt",string)

open_and_read("ramdata.txt")



