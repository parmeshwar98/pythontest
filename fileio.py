f=open("demo.txt","r")
data=f.read(5)
line=f.readline()
print(line)

line1=f.readline()
print(line1)
print(data)
print(type(data))
f.close()
8149024645

f=open("demo.txt","w")
f.write("i want to larn javascript")
f.close()

f=open("demo.txt","a")
f.write("\ni want to larn javascript")
f.close()




f=open("deva.txt","w")
f.write("i want to larn javascript")
f.close()


f=open("demo.txt","r+")
f.write("abc")
print(f.read())
f.close()

f=open("demo.txt","w+")

print(f.read())
f.close()


f=open("demo.txt","a+")
f.write("i want to larn javascript")
f.close()



with open("demo.txt","r") as f:
    data=f.read()

with open("demo.txt","w")as f:

    data=f.write("news data")
    print(data)


with open("pratice.txt","w")as f:
    f.write("hi everyone\nwe are learning file  i/o\n")
    f.write("using java\ni like programmimg in java")

with open("pratice.txt","r")as f:
    data=f.read()

new_data=data.replace("java","python")
print(new_data)

with open("pratice.txt","w") as f:
    data=f.write(new_data)


def check_word():
    word="learning"
    with open("pratice.txt","r") as f:
         data=f.read()
    if(data.find(word)!=-1):
        print("found")
    else:
        print("not found")
check_word()


def check_word():
    word="xlearning"
    with open("pratice.txt","r") as f:
         data=f.read()
    if(data.find(word)!=-1):
        print("found")
    else:
        print("not found")
check_word()



def check_word12():
    word="learning"
    data=True
    line_no=1
    with open("pratice.txt","r")as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1

check_word12()


with open("don.txt","r")as f:
    data=f.read()
    print(data)
    num=""
    for i in range(len(data)):
         if(data[i]==","):
             print(int(num))
             num=""
         else:
             num+=data[i]
count=0
with open("don.txt","r")as f:
    data=f.read()
    print(data)
    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count+=1

    print(count)

















