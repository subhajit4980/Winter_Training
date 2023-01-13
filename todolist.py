import json
from datetime import date

emptyDoc=False
newDay=False

task={}
while True:
    with open("todoDB.json","r") as f:
        todoData=json.load(f)

    currentDATE=date.today()
    if len(todoData)>=0:
        emptyDoc=True

        username=input('Hi  ! welcome to todo app \n please enter your username :')
        todoData['name']=username
        todoData['date']=str(currentDATE)

        todoData['today']=[]
        while True:
            print("\n create a task by writing <create task> or <add task> :")
            cmd=input(">>>")
            if cmd=='create task' or cmd=='add task':
                task_description=input("\n enter description")
                task_schedule_time=input('\n enter the time to schedule the task')

                task={
                    "description":task_description,
                    "schedule_time":task_schedule_time
                }
                todoData['today'].append(task)

                with open('todoDB.json','w') as f:
                    json.dump(todoData,f,indent=4)
            if cmd =='new user':
                break
            if cmd=='exit':
                exit()
                