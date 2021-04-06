## i am using list in this program not sets

vowel = ['a','e','i','o','u','A','E','I','O','U']

string =input("Enter any string")

result =0
for character in string:
    if character in vowel:
        result+=1
    else:
        continue

print("number ov vowels in ",string,"are: ",result)

