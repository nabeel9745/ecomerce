from django.shortcuts import render

# Create your views here.

def customerregister(request):
    return render(request,'customerregister/customer register.html')

def login(request):
    return render(request,'login/login.html')

    