from django.shortcuts import render

# Create your views here.

def customerregister(request):
    return render(request,'common/customerregister.html')

def login(request):
    return render(request,'common/login.html')

def new(request):
    return render(request,'common/new.html')   