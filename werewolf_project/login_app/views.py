from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    return render(request, 'login_registration.html')

def register(request):
    errors = User.objects.new_user_validator(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, errors[error])
        return redirect('/')
    passwordHash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    print("hashed password:", passwordHash)
    currUser = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=passwordHash)
    print("created user")
    request.session['currUserID'] = currUser.id
    return redirect('/trips')
    
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, errors[error])
        return redirect('/')
    currUser = User.objects.filter(email=request.POST['email'])[0]
    request.session['currUserID'] = currUser.id
    return redirect('/trips')

def success(request):
    if not request.session['currUserID'] or request.session['currUserID'] == None:
        messages.error(request, "You must first login!")
        return redirect('/')
    return render(request, 'success.html')

def logout(request):
    request.session['currUserID'] = None
    return redirect('/')

def checkEmail(request):
    found = False
    if len(User.objects.filter(email=request.POST['email'])) > 0:
        found = True
    context = {
        'found': found,
    }
    # if found == False:
    #     msg = "Email Available"
    # else:
    #     msg = "Email already taken"
    return render(request, 'partials/emailCheck.html', context)
