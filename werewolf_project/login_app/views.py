from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    if 'userID' not in request.session or request.session['userID'] == None:
        return render(request, 'login_registration.html')
    else:
        return redirect('/home')

def register(request):
    errors = User.objects.new_user_validator(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, errors[error])
        return redirect('/')
    passwordHash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    currUser = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], username=request.POST['username'], email=request.POST['email'], password=passwordHash)
    request.session['userID'] = currUser.id
    return redirect('/home')
    
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, errors[error])
        return redirect('/')
    currUser = User.objects.filter(email=request.POST['email'])[0]
    request.session['userID'] = currUser.id
    return redirect('/home')

def logout(request):
    request.session.clear()
    return redirect('/')

def checkEmail(request):
    context = {
        'found': (len(User.objects.filter(email=request.POST['email'])) > 0),
    }
    return render(request, 'partials/emailCheck.html', context)
