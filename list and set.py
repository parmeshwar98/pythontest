"""" ""
list9=[1,2,1]

list10=[1,2,3]

copy_list=list9.copy()
copy_list.reverse()
print(copy_list)

if(copy_list==list9):
    print("its a palindrome")
else:
    print("not a palindrome")
"""""
""" ""
 #dictionaries and set
info={
    "name":"parm",
    "divison":"a",
    "learning":"coding",
    "age":85
}
print(info["name"])
print(info["divison"])
print(info["learning"])
print(info["age"])

info["name"]="parmeshwar"
info["surname"]="pawar"
print(info)

student={
    "name":"rahul kumar",
    "subjects" : {
    "phy":98,
    "chem":97,
    "sci":87,
    "eng":89
     }


}
print(list(student.keys()))
print(student["subjects"])
print(student.items())
pairs=list(student.items())
print(pairs[1])
print(student["name"])
print(student.get("name"))
#print(student["name2"])
#print(student.get("name2"))


student.update({"city":"delhi"})
print(student)
"""""

# set concepts
#set are not allowed in dict and list
# set are allowed in boolean ,float ,int, str,tuple

collections={
    1,2,34,5,"hello","hello"
}
print(collections)
print(type(collections))
print(len(collections))

collect=set()
collect.add(1)
collect.add(2)
print(collect)
print(type(collect))

collect1={
    "hello","world",1,"parm"
}
print(collect1.pop())
print(collect1.pop())
print(collect1.pop())

set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))


parm2={
    "table":" a piece of furniture",
             " list of facts and figures  "
     "cat":"a small animal"
}
print(parm2)

parm3={
    "python","java","c++","python","javascript","java",
    "python","java","C++","c"
}

print(parm3)

marks={}
x=int(input("enter your phy :"))
marks.update(
    {"phy" :x})

x=int(input("enter your chem :"))
marks.update({"chem ":x})

x=int(input("enter your sci :"))
marks.update(
    {"sci" :x})

print(marks)


parm4={
    ("float",9.0),
    ("int",9)
}
print(parm4)