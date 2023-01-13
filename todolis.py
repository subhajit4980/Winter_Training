import json
from datetime import date
import streamlit as st

task={}
while True:
    with open("todoDB.json","r") as f:
        todoData=json.load(f)
    currentDATE=date.today()
    if len(todoData)==0:
        username=input('Hi  ! welcome to todo app \n please enter your username :')
        todoData['name']=username
        todoData['date']=str(currentDATE)
        print("\n create a task by writing <create task> or <add task> :")
        cmd=input(">>>")
        todoData['today']=[]
        if cmd=='create task' or cmd=='add task':
            task_description=input("\n enter description : ")
            task_schedule_time=input('\n enter the time to schedule the task : ')
            task={
                "description":task_description,
                "schedule_time":task_schedule_time,
                "task_id":0,
                "status":"To Be Done⛔"
            }
            todoData['today'].append(task)
            with open('todoDB.json','w') as f:
                json.dump(todoData,f,indent=4)
    elif "today" in list(todoData.keys()):
        tasks=todoData['today']
        username=todoData['name']
        print(f"\nhey {username}, here are the tasks for your day\n ")
        for task in tasks:
            print(f"\ntask_id is ",task["task_id"])
            print(f"task number {tasks.index(task)+1}")
            print("task description ",task['description'])            
            print("task schedule time ",task['schedule_time'])            
            print("your task ",task['status'])            
        print("\n1.create another task by writing <create task> or <add task> :")
        print("2.delete user by writing \"delete user\" :")
        print("3.update status of the task by writing \"update status\" :")
        print("4.delete task by writing \"delete task\" :")
        print("5.Exit from the app type \"exit\" :\n")
        cmd=input(">>>")
        if cmd=='create task' or cmd=='add task':
            task_description=input("\n enter description : ")
            task_schedule_time=input('\n enter the time to schedule the task : ')
            task={
                "description":task_description,
                "schedule_time":task_schedule_time,
                 "task_id":len(todoData['today'])+1,
                "status":"To Be Done"
            }
            todoData['today'].append(task)

            with open ("todoDB.json","r+") as f:
                f.seek(0)
                json.dump(todoData,f,indent=4)
            print('\nYour task created sucessfully !!!!!!!!!!!!')
            print('if you want to add task type <create task> or <add task>')
            print('if you are done type done\n')
            continue
        if cmd=="delete user":
            with open("todoDB.json","w") as f:
                json.dump({},f,indent=4)
            print("all data deleted successfully!!!")
        if  cmd=='exit':
            print('\nhave a great day\n')
            exit()
        if cmd=="delete task":
            if  "today" in list(todoData.keys()):
                todoData['today']=[]
                todoData['name']=username
                todoData['date']=str(currentDATE)
                with open("todoDB.json","w") as f:
                    json.dump(todoData,f,indent=4)
        if cmd =="update status":
            tid=int(input("enter your task_id : "))
            mark=input("type status :")
            for task in tasks:
                if task['task_id']==tid:
                    todoData['today'][tasks.index(task)]['status']=mark
                else:
                    continue
            with open("todoDB.json","r+") as f:
                        json.dump(todoData,f,indent=4)
                        
