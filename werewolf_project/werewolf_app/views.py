from django.shortcuts import render, redirect
from .models import User, Game, Role

def homeIndex(request): # Main Home Page
    return render(request, 'homeIndex.html')

def header(request): #partial render header
    context = {
        'user': User.objects.get(id=request.session['userID']),
    }
    return render(request, 'partial/header.html', context)