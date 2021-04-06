f = open("demo.txt","w")

f.write("hello this is new content written by tanisha khandelwal")

f.close()

f=open("demo.txt","r")
print("new content is:")
content = f.read()

print(content)