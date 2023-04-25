from flask import Flask,request,jsonify
from uuid import uuid1,uuid4
import os,json,pytz
from datetime import datetime,date
import pandas as pd

db={}
db_filename='db.json'

if os.path.exists(db_filename):
    print('db exists')
    with open(db_filename,'r') as f:
        db=json.load(f)
else:
    print("db not found")
    accesskey=str(uuid1())
    secretkey=str(uuid4())
    item_types=["food","Brevarage","clothing","stationaries","electronics devices","wearables"]
    db={
        "accesskey":accesskey,
        "secretkey":secretkey,
        "item_types":item_types,
        "users":[]
    }
    with open(db_filename,"w") as f:
        json.dump(db,f,indent=4)


app=Flask(__name__)
@app.route("/signup",methods=["POST"])

def signup():
    if request.method=="POST":
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        username=request.form['username']
        userDict={
            "name":name,
            "email":email,
            "password":password,
            "username":username,
            "purchase":{}
        }
        emailList=[]
        for user in db["users"]:
            emailList.append(user["email"])
        if len(db["users"])==0  or userDict["email"] not in emailList:
            db["users"].append(userDict)
            with open(db_filename,"r+") as f:
                f.seek(0)
                json.dump(db,f,indent=4)
                return "success"
        else:
            return "user already exists"
    return "method not allowed"
@app.route("/signin",methods=["POST"])

def signin():
    if request.method=="POST":
        email=request.form['email']
        password=request.form['password']
        for user in db["users"]:
            if user["email"]==email and user["password"]==password:
                user_idx=db["users"].index(user)
                response={
                    "massage":"Login successful",
                    "user_idx": user_idx
                }
                return response
            else:
                 continue
    return "user doesn't exists"
@app.route("/add_purchase",methods=["POST"])

def add_purchase():
    if request.method =="POST":
        user_idx=int(request.form["user_index"])
        item_name=request.form["item_name"]
        item_types=request.form["item_types"]
        item_price=request.form["item_price"]
        curr_date=str(date.today())
        # curr_date="2023-01-17"
        curr_time=str(datetime.now(pytz.timezone("Asia/Kolkata")))
        itemDict={
            "item_name": item_name,
            "item_type": item_types,
            "item_price": item_price,
            "purchase_time": curr_time,
        }
    #     if curr_date in db["users"][user_idx]["purchase"]:
    #         db["users"][user_idx]["purchase"][curr_date].append(itemDict)
    #         with open(db_filename,"r+") as f:
    #             f.seek(0)
    #             json.dump(db,f,indent=4)
            
    #     else:
    #         db["users"][user_idx]["purchase"][curr_date]=[]
    #         db["users"][user_idx]["purchase"][curr_date].append(itemDict)
    #         with open(db_filename,"r+") as f:
    #             f.seek(0)
    #             json.dump(db,f,indent=4)
    # return "item added successfully"
        existing_dates = list(db["users"][user_idx]["purchase"].keys())
        print(existing_dates)

        if len(db["users"][user_idx]["purchase"]) == 0 or curr_date not in existing_dates:
            db["users"][user_idx]["purchase"][curr_date] = []
            db["users"][user_idx]["purchase"][curr_date].append(itemDict)
            with open(db_filename, "r+") as f:
                f.seek(0)
                json.dump(db, f, indent=4)
            return "Item added successfully"
        else:
            db["users"][user_idx]["purchase"][curr_date].append(itemDict)
            with open(db_filename, "r+") as f:
                f.seek(0)
                json.dump(db, f, indent=4)
            return "Item added successfully"
@app.route("/get_purchases_today",methods=['GET'])
def get_purchases_today():
    # if request.method =="GET":
        # curr_date= str(date.today())
    #     user_idx=int(request.form["user_index"])
    #     if curr_date in db["users"][user_idx]["purchase"]:
    #         return db["users"][user_idx]["purchase"][curr_date]
    #     else:
    #         return "you have no purchase"
    user_idx = int(request.args["user_index"])
    curr_date = str(date.today())
    purchases_today = db["users"][user_idx]["purchase"][curr_date]
    if len(purchases_today) == 0:
        return jsonify(msg="No items purchased today.")
    return jsonify(purchases_for_today=purchases_today)
@app.route("/get_purchases", methods=["GET"])
def get_purchases():
    data=request.json
    user_idx=data["user_index"]
    start_date=data["start_date"]
    end_date=data["end_date"]
    date_range=pd.date_range(start_date,end_date)
    db_dates=db["users"][user_idx]["purchase"].keys()
    purchase_list={}
    for dt in db_dates:
        if dt in date_range:
            purchase_list[dt]=db["users"][user_idx]["purchase"][dt]
        else:
            continue
    return purchase_list
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)