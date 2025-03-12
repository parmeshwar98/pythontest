#code of calculator in conditional statments
from itertools import count
""" 
a=int(input("enter your no:"))
b=int(input("enter your second no:"))
choice=int(input())
if(choice==1):
     print("add",a+b);
elif(choice==2):
     print("sub",a-b);
elif(choice==3):
     print("multiply",a*b);
elif(choice==4):
     print("divison",a/b);
else:
     print("no is not given");

#print(sum);

#code for user input for student details
d=input("enter your name:")
e=input("enter your div:")
f=input("enter your school name: ")
choice=int(input())
if(choice==1):
    print(d);
elif(choice==2):
    print(e);
elif(choice==3):
    print(f);
else:
    print("data is not listed");



#x=int(input("enter your no:"))
#y=int(input("enter your second no:"))

"""
""" ""
#for loop increment value
 count=1
while count<=5:
    print("hello world",count)

    count += 1

#for loop decrement value
i=5
while i>=1:
    print(i)

    i -= 1
print("loop ended")

#for loop print 100 to 1

z=1
while z<=100:
    print(z)
    z +=1

#for loop print 1 to 100

z=100
while z>=1:
    print(z)
    z-=1
# for loop print multiply of n

x=int(input("enter your no"))
i=1
while i<=10:
    print(x*i)
    i+=1
"""
""" ""
# calucalting length of index
nums=[1,4,5,6,78,89,102,214,236,300]
idx=0
while idx<len(nums):
    print(nums[idx])
    idx+=1
"""

""" ""
##finding elements at index
nums=[1,4,5,6,78,89,102,214,236,300]
X=236
idx=0
while idx<len(nums):
    if(nums[idx]==X):
        print("found at index",idx)
    else:
        print("finding value..")
    idx +=1

#wap to use break statment in loop
nums=[1,4,5,6,78,89,102,214,236,300]
X=300
idx=0
while idx<len(nums):
    if(nums[idx]==X):
        print("found at index",idx)
        break
    else:
        print("finding value..")
    idx +=1
print("end of the loop")




#wap program for continue statement
# we have used for continue keyword
# it is uesd for skip the condition and to be execute further condition
i=0
while i<=10:
    if(i==3):
       i+=1
       continue
    print(i)
    i+=1

#wap program for for loop finding elements in list
#we have used break statements
#it stop the loop
nums=[1,4,5,6,78,89,102,214,236,300]
x=214
ix=0
for val in nums:
    if(val==x):
       print("no found at ix",ix)
       break
    ix+=1


# wap program for range print 10
seq=range(10)
for i in seq:
    print(i)

#wap program for range with step of 3
seq=range(2,10,3)
for i in seq:
    print(i)

#wap program for range print 1 to 100
for i in range(1,100):
    print(i)

#wap program for range print 100 to 1
for i in range(100,0,-1):
    print(i)

l1=[10,20,30,40]
l2=[1,2,3,4]

for a in l1:
    for b in l2:
        print(a,b)
"""


#wap for calculate any table
n=int(input("enter your no:"))
for i in range(1, 11):
    print(n*i)

""" ""
#wap program for pass statements
    seq = range(10)
    for i in seq:
        pass

        print(i)
"""" "



n=10
sum=0

for i in range (n+1):
    sum +=i
print("total sum:",sum)


n=14
sum=0
i=5
while i<=n:
    sum +=i
    i+=1
print("total sum:",sum)

n=5
fact=1
i=1
while i<=n:
    fact *=i
    i+=1
print("total factorial :",fact)




n=5
fact=1

for i in range (1,n+1):
    fact *=i
print("total factorial:",fact)