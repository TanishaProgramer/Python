dictionary = {"name":"chirag","age":20,"class":"7th sem","salary":"0","job":"no"}

print("1 name \n 2 age \n 3 class \n 4 salary \n 5 job")
print("select one of them")

choice = int(input())

if choice ==1:
    print(dictionary["name"])
elif choice==2:
    print(dictionary["age"])
    