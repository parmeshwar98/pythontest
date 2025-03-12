def task():
    tasks=[]
    print("____________welcome to task management app_________")
    total_task=int(input("how may task you want to add:"))

    for i in range(1,total_task+1):
     task_name=input(f"enter your task{i}=")
    tasks.append(task_name)
    print(f"today tasks are\n(tasks)")
while True:
    operation=int(input("enter 1-add\n2-update\n3-delete\n4-view\n5- stop\exit"))