employeelist=[{
    "name":'subahjit',
    "emp_id": 324,
    'address':([
        {
            'home town':'ragpur',
            'post office':'ragpur',
            'dist':'paschim medinipur',
            'pin code': '721131'
        },
        {
            'home town':'haldia',
            'post office':'hatiberia',
            'dist':'purba medinipur',
            'pin code': '721563'
        }
    ])
},
{
    "name":'sudip',
    "emp_id": 327,
    'address':([
        {
            'home town':'baharampur',
            'post office':'baharampur',
            'dist':'murshidabad',
            'pin code': '723342'
        },
        {
            'home town':'new town',
            'post office':'dharmatala',
            'dist':'kolkata',
            'pin code': '760001'
        }
    ])
}
]
def function(list:employeelist, inputstring):
    MpincodeList=[]
    for i in range (len(employeelist)):
        pincodeList={}
        pincodelist=[]
        pincodeList['name']=(employeelist[i]['name'])
        for j in range (len(employeelist[i]['address'])):
            pincodelist.append(employeelist[i]['address'][j][inputstring])
        pincodeList[inputstring]=pincodelist
        MpincodeList.append(pincodeList)
    return (MpincodeList)
s=input('enter address key ')
output=function(employeelist,s)
print(output)