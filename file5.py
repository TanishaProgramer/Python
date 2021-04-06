def open_and_read(filename):
    f = open(filename,"r")

    content= f.read()

    list1=content.split("\n")
    print(list1)
    print("number of words are: ",len(list1))

open_and_read("demo.txt")