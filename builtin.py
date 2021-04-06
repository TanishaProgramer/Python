# in this program we are going to learn about built in functions of python

print(abs(12.234))

print(bin(2))

print(bool("hello"))

#func is callable function.
def func():
    return
print(callable(func))

code_py = 'i=10\nj=10\nprint(i+j)'

code = compile(code_py,"sumpy.py",'exec')

print(type(code))

exec(code)

i = 10
j='i+1+10*56/23+12'

print(eval(j))

class User:
    name = "ajay nagar"
    age = 23

details = User()

print(getattr(details,"name"))




