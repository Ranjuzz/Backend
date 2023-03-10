import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def fireconnect(cred):
    cred=credentials.Certificate('secretkey.json')
    firebase_admin.initialize_app(cred,{
    'databaseURL':"https://studio-5f946-default-rtdb.asia-southeast1.firebasedatabase.app"

    })
    ref = db.reference('/images')
    print(ref.get())