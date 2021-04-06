 


#this is bunch of dataset
user_data =[]


def getdata():

    ## this is demo data
    dataset = {"name":"","age":"","classs":""}
    #taking input from user
    name = input("Enter name: ")
    
    age = input("enter age: ")
    classs = input("enter class: ")
    print("\n")
    
    # assigning value to dataset
    dataset["name"]=name
    dataset["age"]=age
    dataset["classs"]=classs

    #returning dataset
    return dataset

## making list of data given by user.
for i in range(0,4):
    data = getdata()
    user_data.append(data)
    print(data)
    print(user_data)
# prining title for data
print("  name  age  class")

#printing the data
for i in user_data:
    print("  ",i["name"],"  ",i["age"],"  ",i["classs"])