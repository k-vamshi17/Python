#Program for Demonstrating Need of Static Method
#StaticMethodEx6.py
class Employee:
    def readempdata(self):
        print('-'*50)
        self.eno=int(input("\tEnter Employee Number:"))
        self.ename=input("\tEnter Employee Name:")
        self.sal=float(input("\tEnter Employee Salary:"))
class Student:
    def readstudata(self):
        print('-'*50)
        self.sno = int(input("\tEnter Student Number:"))
        self.sname = input("\tEnter Student Name:")
class Teacher:
    def readteacherdata(self):
        print('-'*50)
        self.tno = int(input("\tEnter Teacher Number:"))
        self.tname = input("\tEnter Teacher Name:")
        self.subject = input("\tEnter Teacher Subject:")
        self.exp=float(input("\tEnter Teacher Experience:"))
class Hyd:
    def recvobject(self,obj,objinfo): # Instance Method
        self.dispobjinfo(obj,objinfo) # calling Static Method from Insatnce Method w.r.t self
    @staticmethod
    def dispobjinfo(obj,objinfo):
        print("*"*50)
        print("{} Information".format(objinfo))
        print("*"*50)
        for k,v in obj.__dict__.items():
            print("\t{}--->{}".format(k,v))
        print("*" * 50)
#Main Program
eo=Employee()
so=Student()
to=Teacher()
#read the data for Different Objects
eo.readempdata()
so.readstudata()
to.readteacherdata()
#Display the Data of Different Objects of Different Classes
#By using Single Method called Static Method
Hyd().recvobject(eo,"Employee") # calling Instance method by Name-Less object
Hyd().dispobjinfo(so,"Student") # calling Class Level method Name-Less Object
Hyd().dispobjinfo(to,"Teacher") # calling Class Level method by Name-less object
