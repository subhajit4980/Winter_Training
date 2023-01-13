# array=[['subhajit',55],['sudip',56],['sayan',44]]
# print(array)
# for i in range (len(array)):
#     print(array[i][0]," ",array[i][1])
# employee={
#     "name":'subahjit',
#     "emp_id": 324,
#     'address':([
#         {
#             'village':'ragpur',
#             'post office':'ragpur',
#             'dist':'paschim medinipur',
#             'pin code': '721131'
#         },
#         {
#             'village':'haldia',
#             'post office':'hatiberia',
#             'dist':'purba medinipur',
#             'pin code': '721563'
#         }
#     ])
# }
# for i in range (len(employee['address'])):
#     print("pin code of the no.",i,"address" ,employee['address'][i]['pin code'])
# employeelist=[{
#     "name":'subahjit',
#     "emp_id": 324,
#     'address':([
#         {
#             'home town':'ragpur',
#             'post office':'ragpur',
#             'dist':'paschim medinipur',
#             'pin code': '721131'
#         },
#         {
#             'village':'haldia',
#             'post office':'hatiberia',
#             'dist':'purba medinipur',
#             'pin code': '721563'
#         }
#     ])
# },
# {
#     "name":'sudip',
#     "emp_id": 327,
#     'address':([
#         {
#             'home town':'baharampur',
#             'post office':'baharampur',
#             'dist':'murshidabad',
#             'pin code': '723342'
#         },
#         {
#             'home town':'new town',
#             'post office':'dharmatala',
#             'dist':'kolkata',
#             'pin code': '760001'
#         }
#     ])
# }
# ]
# def function(list:employeelist):
#     MpincodeList=[]
#     for i in range (len(employeelist)):
#         pincodeList={}
#         pincodelist=[]
#         pincodeList['name']=(employeelist[i]['name'])
#         for j in range (len(employeelist[i]['address'])):
#             pincodelist.append(employeelist[i]['address'][j]['pin code'])
#         pincodeList['pin code']=pincodelist
#         MpincodeList.append(pincodeList)
#     return (MpincodeList)
# up_list=function(employeelist)
# print(up_list)
# def sum(a,b):
#     return a*b
# print(sum(3,5))
# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(0,len(arr)-i-1):
#             if arr[j]>arr[j+1]:
#                 a=arr[j]
#                 arr[j]=arr[j+1]
#                 arr[j+1]=a

# arr=[1,4,3,5,2,7]
# bubble_sort(arr)
# print(arr)

