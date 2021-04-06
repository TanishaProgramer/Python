def myfunc(n):
    return lambda a :a*n*n

res = myfunc(4)

print(res(1))