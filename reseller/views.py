from django.shortcuts import render

# Create your views here.

def addproject(request):
    return render(request,'reseller/add project.html')    

def home(request):
      return render(request,'admin/home.html')    