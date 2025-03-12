"""
a=input("enter your name:")
b=input("enter your department:")
c=input("enter your college name:")
d=input("enter your location:")
e=int(input("enter your mobile no:"))
choice=int(input("enter your choice:"))

if (choice==1):
    print(a)
elif(choice==2):
    print(b)
elif(choice==3):
    print(c)
elif(choice==4):
    print(d)
elif(choice==5):
    print(e)
else:
    print("no is not given")


"""

def print_hello():
    print("hello world")
print_hello()
print_hello()
print_hello()

def cal_o(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
cal_o(98,25,69)


def cal_o(a,b=2):
    print(a*b)

    return (a*b)
cal_o(5)


cities=["delhi","mumbai","chennai","mumbai"]
def prints_hlelo(cities):
    print(cities)
prints_hlelo(len(cities))

""" 
cities=["delhi","mumbai","chennai","mumbai"]
def print_list(list):
    for items in (list):
        print(items,end=" ")
print_list(cities)
"""





def cal_fun(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
cal_fun(5)








def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"usd",inr_val,"inr")

converter(1)




def show(n):
    if  (n==0):
         return
    print(n)

    show(n-1)
show(5)



def fun(n):
    if(n==1 or n==0):
       return 1
    return fun(n-1)*n
print(fun(5))


def sum_f(n):
    if(n==0):
        return 0
    return sum_f(n-1)+ n
print(sum_f(10))


def list_1(list, idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    list_1(list,idx+1)
fruits=["mango","banana","orange","pineapple"]
list_1(fruits)