from django.shortcuts import render, redirect

def homeIndex(request): # Main Home Page
    return render(request, 'homeIndex.html')

def header(request): #partial render header
    return render(request, 'partial/header.html')