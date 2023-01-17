from flask import Flask

app=Flask(__name__)
# @app.route("/hello")
# def hello():  
#     print("hello!")
#     return "hello world"
users=[
    {
    "user_id":"user1",
    "user_name":"subhajit"
    },
    {
    "user_id":"user2",
    "user_name":"sudip"
    },
    {
    "user_id":"user3",
    "user_name":"sayan"
    }
]
@app.route("/get_user_id")

def get_user_id():
    us={'idlist':[]}
    for i in users:
        us["idlist"].append(i["user_id"])
    return us
@app.route("/get_user_name")

def get_user_name():
    us={'username_list':[]}
    for i in users:
        us["username_list"].append(i["user_name"])
    return us
if __name__ == '__main__':
    app.run(host='127.0.0.1',port='5000',debug=True)