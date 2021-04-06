def open_and_read(filename):
    f= open(filename,"r")

    content = f.read()

    print(content)

def open_and_write(filename):
    f=open(filename,"w")

    content = input("Enter the content to write")

    f.write(content)



## calling the function

open_and_read("demo.txt")

## writing user data

open_and_write("demo.txt")

## then printing  new content

open_and_read("demo.txt")