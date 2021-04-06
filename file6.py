def open_and_read(filename):
    f = open(filename,"r")
     
    content = f.read()

    print(content)

    f.close()


def open_and_append(filename,data):

    f = open(filename,"a+")


    # here write will work as append
    f.write(data)

    f.close()

open_and_read("demo.txt")
open_and_append("demo.txt",)

open_and_read("demo.txt")