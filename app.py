from flask import *  
import pyrebase

config = {
    ## Your DB DATA HERE
}

'''B DATA LOOKS LIKE 
"apiKey": "",
  "authDomain": "",
  "projectId": "",
  "storageBucket": "",
  "messagingSenderId": "",
  "appId": "",
  "databaseURL" : ""   
'''

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__) 


@app.route('/add', methods=['POST'])  
def addusers():
    if request.method == "POST":
        email = request.json['email']
        password = request.json['password']
        name = request.json['name']
        try:
            user = auth.create_user_with_email_and_password(email,password)
            data = {
                "name":name
            }
            results = db.child("users").child(user['localId']).set(data)
            return {"auth" : True, "msg":name+', thanks for registering with us.'}
        except Exception as e:
            return {"auth" : False, "msg":"Email ID already registered or passowrd is less than 6 characters"}
    else:
        return {"auth":False, "msg":"Something is wrong"}

@app.route('/find', methods=["POST"])
def finduser():
    if request.method == "POST":
        email = request.json['email']
        password = request.json['password']
        try:
            user = auth.sign_in_with_email_and_password(email,password)
            user = db.child("users").child(user['localId']).get()
            name = user.val()["name"]
            return{"auth":True, "msg":"Welcome back, "+name}
        except:
            return {"auth" : False, "msg":"Invalid Credentials"}
    else:
        return {"auth":False, "msg":"Something is wrong"}


@app.route('/update', methods=["POST"])
def updateuser():
    if request.method == "POST":
        email = request.json['email']
        password = request.json['password']
        name = request.json['name']
        try:
            user = auth.sign_in_with_email_and_password(email,password)
            print(user)
            data = {
                "name":name
            }
            user = db.child("users").child(user['localId']).update(data)
            return{"auth":True, "msg":"Data updated"}
        except:
            return {"auth" : False, "msg":"Invalid Credentials"}
    else:
        return {"auth":False, "msg":"Something is wrong"}

@app.route('/delete', methods=["POST"])
def deleteuser():
    if request.method == "POST":
        email = request.json['email']
        password = request.json['password']
        try:
            user = auth.sign_in_with_email_and_password(email,password)
            deleteuser = db.child("users").child(user['localId']).remove()
            auth.delete_user_account(user['idToken'])
            return{"auth":True, "msg":"Data deleted"}
        except:
            return {"auth" : False, "msg":"Invalid Credentials"}
    else:
        return {"auth":False, "msg":"Something is wrong"}

if __name__ == '__main__':  
   app.run(debug = True)  
