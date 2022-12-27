# single level inheritance
# inheritance is used to inherit some data from a previous class
class person:              # here person is parent or base class
    def __init__(self, name, age):
        self.name= name
        self.age= age
    
    def print1(self):
        print("name is",self.name,"age is",self.age)

class student(person):        # here student is child or derived class
    def __init__(self,name,age, marks):
        person.__init__(self,name,age)
        self.marks=marks

    def print2(self):
        print("name is",self.name,"age is",self.age,"marks is",self.marks)

s1=student("satyam",19,30)
s1.print2()





# multi level class
class grandfather:
    def __init__(self,name):
        self.grandfathername= name


class father(grandfather):
    def __init__(self,name,grandfathername):
        self.fathername=name
        grandfather.__init__(self,grandfathername)

class daughter(father):
    def __init__(self,name,fathername,grandfathername):
        self.daughtername=name
        father.__init__(self,fathername,grandfathername)

    def print(self):
        print("grandfathername is",self.grandfathername)
        print("fathername is",self.fathername)
        print("daughtername is",self.daughtername)

s1=daughter("ram","mohan","shyam")
s1.print()


