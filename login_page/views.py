from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from .models
def view_name(request):
    return render(request, 'login.html', {})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username, password=pa)
    context={}
    return render(request, 'login.html', context)