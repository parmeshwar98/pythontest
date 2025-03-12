class  Student:

    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math


    @property
    def calcpercentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1=Student(98, 82 ,96)
print(stu1.calcpercentage)

stu1.phy=85
print(stu1.calcpercentage)


class complex:

    def __init__(self,real,imag):
         self.real=real
         self.imag=imag
    def shownumber(self):
         print(self.real,"i+",self.imag,"j")

    def __add__(self,num1):
        newreal=self.real+num1.real
        newiamg=self.imag+num1.imag
        return complex(newreal,newiamg)


num=complex(1,3)
num.shownumber()

num1=complex(2,5)
num1.shownumber()


num3=num+num1
num3.shownumber()


class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (22/7)*self.radius ** 2
    def paramete(self):
        return 2*(22/7)*self.radius ** 2

ci=circle(22)
print(ci.area())
print(ci.paramete())


class employeee:
    def __init__(self,role,depat,salary):
        self.role=role
        self.depat=depat
        self.salary=salary

    def showdetails(self):
        print("role =",self.role)
        print("depat =",self.depat)
        print("salary =",self.salary)

class engineeer(employeee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("acc",  "it", "85,000")

d1=engineeer("rahul kumar",45)
d1.showdetails()



class order:
    def __init__(self,items,price):
        self.items=items
        self.price=price
    def __gt__(self, ord2):
        return self.price>ord2.price
ord1=order("chipes",25)
ord2=order("cold",12)
print(ord1>ord2)
