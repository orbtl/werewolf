from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Game, Role

def homeIndex(request): # Main Home Page
    if 'userID' not in request.session or request.session['userID'] == None:
        messages.error(request, "You must log in to view that page")
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['userID']),
    }
    return render(request, 'homeIndex.html', context)

def header(request): #partial render header
    context = {
        'user': User.objects.get(id=request.session['userID']),
    }
    return render(request, 'partial/header.html', context)

