
report =[]
report_demo ={"name":"","age":"","class":"","percentage":""}

def add(dict):
    return list

def remove(dict):
    return list

while(True):

    print("1: Add student")
    print("2: remove student")
    print("3: view report")

    choice = int(input("enter your choice"))
    switcher={
        1: add(report_demo),
        2: remove(report_demo)
    }
    print (switcher.get(choice,"invalid input"))
