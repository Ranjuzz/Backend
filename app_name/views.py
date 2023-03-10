from django.shortcuts import render, redirect
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import default_storage
from django.contrib import messages
import pyrebase
import os
config = {

  "apiKey": "AIzaSyAJ-wgnz5P7pyg2reCZaSivG17nfIs7Xm8",

  "authDomain": "studio-5f946.firebaseapp.com",

  "databaseURL": "https://studio-5f946-default-rtdb.asia-southeast1.firebasedatabase.app",

  "projectId": "studio-5f946",

  "storageBucket": "studio-5f946.appspot.com",

  "messagingSenderId": "671673613388",

  "appId": "1:671673613388:web:aef21312c6d0725a7288e9",

  "measurementId": "G-9L43N0LP2T"

};


firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

def main(request):
    if request.method == 'POST':
        file = request.FILES['file']
        file_save = default_storage.save(file.name, file)
        storage.child("files/" + file.name).put("media/" + file.name)
        delete = default_storage.delete(file.name)
        messages.success(request, "File upload in Firebase Storage successful")
        return redirect('main')
    else:
        return render(request, 'login.html')