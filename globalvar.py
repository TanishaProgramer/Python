a=1
def a1():
    a=2
    print(a)

def a2():
    a=3
    print(a)

def a3():
    global a
    a=4
    print(a)

print(a)
a1()
print(a)
a2()
print(a)
a3()
print(a)