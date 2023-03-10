import firebase_admin
from firebase_admin import auth
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = auth.get_user_by_email(email)
            auth.sign_in_with_email_and_password(email, password)
            return redirect('home')
        except auth.AuthError:
            error_message = 'Invalid email or password'
    else:
        error_message = ''
    return render(request, 'login.html', {'error_message': error_message})
