class student:
    name="karan kumar"
s1= student()
print(s1.name)

class college:
    depart="it","comp","auto","mech"
    div="a","b","c","d"
    floor='1','2','3',4
s2=college()
print(s2.depart)
print(s2.div)
print(s2.floor)


class learner:
#default constructor
#def __init__(self, fullname):
#print("adding new database:")


#only one constructor is used for one class
#parametrized constructor

    def __init__(self,fullname):
      self.name=fullname
    print("adding new database:")
s3=learner("karan")
print(s3)


class pager:
    college_name="abc college"
                                             #class attributes
    def __init__(self,fullname ,marks):       #constructor
      self.name=fullname                      # object attributes
      self.marks=marks

    @staticmethod
    def welcome():
        print("welcome to pager")

    def getmarks(self):
        return self.marks



s3=pager("karan",97)           #object instances
s3.welcome()
print(s3.getmarks())
print(s3.college_name)


#method overloading
class area:
    def find_area(self,a=None,b=None):
        if a!=None and b!= None:
            print("area of rectangele:",(a*b))
        elif a!=None:
            print("area of square:",a*a)
        else:
            print("nothing to find")
obj1=area()
obj1.find_area()
obj1.find_area(10)
obj1.find_area(10,20)

#method overriding
class a:
    def showdata(self):
        print("i in a class" )
class b(a):
    def showdata(self):
        b.showdata(self)       #this syntax is used for class object to display
        print("iam in b class")

class c(b):
    def showdata(self):
        a.showdata(self)  # this syntax is used for class object to display
        print("iam in c class")
obj=c()
obj.showdata()


class deva:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def getaverage(self):
        sum=0
        for val in self.marks:
         sum += val
        print("hi",self.name ,"your score average is:",sum/3)

s5=deva("parm",[98,99,97])
s5.getaverage()



class bank:
    def __init__(self,acc ,bal):
        self.acc=acc
        self.bal=bal


    #debit method
    def debit(self,amount):
        self.bal-= amount
        print("rs.",amount ,"was debited")
        print("total balance:",self.getbalance())

    def credit(self,amount):
        self.bal += amount
        print("rs.",amount, "was credit")
        print("total balance:",self.getbalance())

    def getbalance(self):
        return self.bal




b1=bank(10000,1324000)
b1.debit(5000)
b1.credit(500)


class bank:
    def __init__(self,acc_no,acc_pswd):
        self.acc_no=acc_no
        self.acc_pswd=acc_pswd
