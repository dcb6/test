import pyrebase

config = {
    "apiKey": "AIzaSyDaX9MehqYrxAp-doO7XFAAs_-2gquou5M",
    "authDomain": "friendlychat-f9712.firebaseapp.com",
    "databaseURL": "https://friendlychat-f9712.firebaseio.com",
    "projectId": "friendlychat-f9712",
    "storageBucket": "friendlychat-f9712.appspot.com",
    "messagingSenderId": "736276679722",
    "serviceAccount": "/Users/danielburke/Documents/Muvve/pyrebase-demo/src/dan_auth.json"
  }

firebase = pyrebase.initialize_app(config)

db = firebase.database()

auth = firebase.auth()
user = auth.sign_in_with_email_and_password("danielb14065@gmail.com","snoborder123")

# user['idToken'] used for a lot of things
# get returns pyreresponse object, val gets actual data

db.child("users").child("Morty")