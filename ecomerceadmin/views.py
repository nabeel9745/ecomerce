from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'admin/home.html')

def viewsellers(request):
    return render(request,'admin/view sellers.html')    