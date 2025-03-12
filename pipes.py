class institute:
    def __init__(self,section,subject,marks):
        self.section=section
        self.subject=subject
        self.marks=marks


d=institute("a","maths","98")
print(d.section)
print(d.subject)
print(d.marks)


x=input("enter your name:")
y=input("enter your college:")
z=int(input("enter your percentage:"))
choice=int(input("enter your choice:"))



if (choice==1):

      print("data is found")

else:
    print("your data is not saved")
