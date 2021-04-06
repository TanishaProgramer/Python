class User:
    def __init__(self,name,rank):
        self.name=name
        self.rank = rank

    def printdata(self):
        print("name of student:"+self.name)
        print("rank of student:",self.rank)
    
u = User("ashish",1000)

u.printdata()