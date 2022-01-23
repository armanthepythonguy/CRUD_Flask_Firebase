# CRUD_Flask_Firebase

In this API, I have used Flask and connected it to the Firebase database using pyrebase module.

Inside the code you will find 4 endpoints namely /add, /find, /update, /delete.

Firstly go to firebase website and create a new app, inside the app again chose web app and then you will get a list of data. Copy it and paste it in dict format in the code where it is written Your DB data.
Then go to the realtime database page, in firebase and create a db. Then just add your db link like this "databaseURL" : "YOUR DB LINK" to the DB data you got.


To run this code in your environment, 
simply run the following commands in CMD or terminal :-

pip install flask
pip install pyrebase (If this command gives error try pip install pyrebase4)

Then simply run this app.py file in your environment.

Locate to localhost:5000 and use the endpoints.
