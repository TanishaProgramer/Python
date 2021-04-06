dict_user = {"name":"","age":"","salary":""}

list_li = [dict_user]

name = age = salary = ""

name = input("Enter user name.")
age= input("Enter user name")
salary = input("Enter user salary")

dict_user[name]= name
dict_user[age]= age
dict_user[salary]= salary

list_li.append(dict_user)

dict_user_2 = list_li[1]

print("name: "+dict_user_2[name])
print("age: "+dict_user_2[age])
print("salary: "+dict_user_2[salary])