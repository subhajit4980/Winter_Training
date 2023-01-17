from flask import Flask,request
from uuid import uuid1,uuid4
import os,json,pytz
from datetime import datetime

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
        if len(db["users"])==0 or userDict not in db["users"]:
            db["users"].append(userDict)
            with open(db_filename,"r+") as f:
                f.seek(0)
                json.dump(db,f,indent=4)
                return "success"
        else:
            return "user already exists"
    return "method not allowed"
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)