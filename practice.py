""" strings & conditional statements"""
from idlelib.pyshell import extended_linecache_checkcache

from ctypes.macholib.dyld import DEFAULT_LIBRARY_FALLBACK

#\n is used for next line

#string is  collection of sequence characters"""
#str1=("thsi is a string\n")
#str2=('apna college\n')
#str3=("""how are you man .\nthis is a python developer""")
#print(str1,str2,str3)

#print(str1+str3)

#len1=len(str1)
#print(len1
#)

#fina_str=(str1+"  "+str2)
#print(len(fina_str));
#print(fina_str);

#indexing
#we used to acces the no
#it starts with always 0 and its used in [] square brackets.

#str4=("apna college")
#ch=str4[5]
#print(ch);


#print(str4[6:len(str4)]);

#print(str4[-3:-8]);

clas=("apnajk")
ch=(clas)
print(clas[-3:-1]);


print(clas.endswith("jk"));
print(clas.capitalize());
print(clas.replace("k","m"));
print(clas.find("a"));
print(clas.count("na"));



#conditional statemts

light="yellow"

if(light=="yellow"):
    print("you can go");
elif(light=="red"):
   print("you can stop");
elif(light=="green"):
    print("you can move");


age=24

if(age>=24):
    print("you can vote");
elif(age<=24):
    print("you cant vote");
else:
    print("your name is not listed");



marks=int(input("enter student marks :"));
if(marks>=90):
    garde="a"
elif(marks>=80 and marks <=90):
    garde="b"
elif(marks>=70 and marks<=80):
    garde="c"
                                                 #elif(marks>=60 and marks<70):
                                                  #garde="d"
else:
    garde="d"

    print("grade of the student", garde);



# write a program for odd or even
num=int(input("enter your number:"));

if(num%2==0):
    print("even");
else:
    print("odd");


# write a program to find 3 among greater no
a=int(input("enter your first no:"))
b=int(input("enter your second no:"))
c=int(input("enter your third no:"))

if(a>=b and a<=c):
    print("a is lower");

elif(b>=c):
    print("b is second");

else:
    print("c is greater");

# wap a if the no is  multiple of 7 or not

x=int(input("enter your no:"))

if(x%7==0):
    print("multiply of 7");
else:
    print("not a multiply ");


