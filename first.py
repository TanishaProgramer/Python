#python proigram to reove dublicaate element and sorting the given list.

list = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,-1,-1,-1]

print("the given list :",list)
set_from_list = set(list)

print(type(set_from_list))
print(set_from_list)

l = sorted(set_from_list)

print("the sorted list:")
print(l)