class A:
    varA="wlecome to a"

class B(A):
    varB="wlecome to b"
CAT=B()
print(CAT.varB)
print(CAT.varA)


#multi level inheritance
class car:
    def __init__(self,type):
        self.type=type
    color="blue"
    @staticmethod
    def start():
        print("car started....")
    @staticmethod
    def stop():
        print("car stoped....")
class toyatacar(car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        super().start()
car1=toyatacar("toyata","electric")
car2=toyatacar("parus","diesel")
print(car1.start())
print(car1.type)

class fortuner(toyatacar):
    def __init__(self,brand):
        self.brand=brand

model=fortuner("diesel")
print(model.stop())



#multiple inheritance
class A:
    varA="wlecome to a"

class B:
    varB="wlecome to b"

class C(A,B):
    varC="welcome to c"

BOOT=C()
print(BOOT.varC)
print(BOOT.varB)
print(BOOT.varA)


class person:
    name="anonymus"

    def changename(self,name):
        self.name=name
p1=person()
p1.changename("rahul kumar")
print(p1.name)
print(person.name)

class person:
    name="anonymus"

    #def changename(self,name):

       # self.__class__.name="rahul"

    @classmethod
    def changename(cls,name):
        cls.name="rahul"
p1=person()
p1.changename("rahul kumar")
print(p1.name)
print(person.name)






