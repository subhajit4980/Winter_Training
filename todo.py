import json
from datetime import date
import streamlit as st

emptyDoc=False
newDay=False

task={}
while True:
    with open("todoDB.json","r") as f:
        todoData=json.load(f)
    # print(todoData,type(todoData))

    currentDATE=date.today()
    if len(todoData)==0:
        emptyDoc=True

        username=st.input('Hi  ! welcome to todo app \n please enter your username :')
        todoData['name']=username
        todoData['date']=str(currentDATE)

        st.success(" create a task by writing <create task> or <add task> :")
        cmd=input(">>>")
        todoData['today']=[]

        if cmd=='create task' or cmd=='add task':
            task_description=input("\n enter description : ")
            task_schedule_time=input('\n enter the time to schedule the task : ')

            task={
                "description":task_description,
                "schedule_time":task_schedule_time
            }
            todoData['today'].append(task)

            with open('todoDB.json','w') as f:
                json.dump(todoData,f,indent=4)
    elif "today" in list(todoData.keys()):
        tasks=todoData['today']
        username=todoData['name']
        print(f"hey {username}, here are the tasks for your day\n ")

        for task in tasks:
            print(f"task number {tasks.index(task)+1}")
            print("task description ",task['description'])            
            print("task schedule time ",task['schedule_time'])            
        print("create another task")
        cmd=input(">>>")
        if cmd=='create task' or cmd=='add task':
            task_description=input("\n enter description : ")
            task_schedule_time=input('\n enter the time to schedule the task : ')

            task={
                "description":task_description,
                "schedule_time":task_schedule_time
            }
            todoData['today'].append(task)

            with open ("todoDB.json","r+") as f:
                f.seek(0)
                json.dump(todoData,f,indent=4)
            print('Your task created sucessfully !!!!!!!!!!!!')
            print('if you want to add task type <create task> or <add task>')
            print('if you are done type done')
            continue
        if cmd=="delete user":
            with open("todoDB.json","w") as f:
                json.dump({},f,indent=4)
            print("all data deleted successfully!!!")
        if cmd=='done' or cmd=='exit':
            print('have a great day')
            exit()
        if cmd=="delete task":
            if  "today" in list(todoData.keys()):
                todoData['today']=[]
                todoData['name']=username
                todoData['date']=str(currentDATE)
                with open("todoDB.json","w") as f:
                    json.dump(todoData,f,indent=4)